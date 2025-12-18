import os
import zipfile
from pathlib import Path

import gdown
from dotenv import load_dotenv

# =========================
# LOAD ENV (EXPLICIT)
# =========================
ROOT_DIR = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH)

FOLDER_ID = os.getenv("GOOGLE_DRIVE_FOLDER_ID")
ZIP_NAME = os.getenv("DATASET_ZIP_NAME")

if not FOLDER_ID or not ZIP_NAME:
    raise ValueError("Missing required environment variables")

# =========================
# PATH CONFIG
# =========================
BASE_DIR = Path(__file__).resolve().parent
DOWNLOAD_DIR = BASE_DIR / "downloads"
ZIP_PATH = DOWNLOAD_DIR / ZIP_NAME
EXTRACT_DIR = BASE_DIR / "dataset"

# print(ZIP_PATH.exists())

def extract_zip():
  print("📦 Extracting dataset...")
  EXTRACT_DIR.mkdir(parents=True, exist_ok=True)
  with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
      zip_ref.extractall(EXTRACT_DIR)
  print("✅ Extraction complete")


def main():
  # 1️⃣ Dataset sudah ada
  if EXTRACT_DIR.exists() and any(EXTRACT_DIR.iterdir()):
      print("✅ Dataset already extracted. Nothing to do.")
      return

  DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

  # 2️⃣ ZIP sudah ada → langsung extract
  if ZIP_PATH.exists():
      print("📁 Zip file already exists. Skipping download.")
      extract_zip()
      return

  # 3️⃣ ZIP belum ada → download
  print("⬇️  Downloading dataset from Google Drive...")
  gdown.download_folder(
      id=FOLDER_ID,
      output=str(DOWNLOAD_DIR),
      quiet=False,
      use_cookies=False,
  )

  if not ZIP_PATH.exists():
      raise FileNotFoundError(f"{ZIP_NAME} not found after download")

  extract_zip()


if __name__ == "__main__":
  main()
