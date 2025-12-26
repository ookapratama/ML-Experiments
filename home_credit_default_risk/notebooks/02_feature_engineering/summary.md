# ⚙️ Final Summary — Feature Engineering

## 🎯 Tujuan Feature Engineering
Feature engineering dilakukan untuk mengubah data mentah dan hasil Exploratory Data Analysis (EDA) menjadi fitur-fitur yang:
- Lebih representatif terhadap risiko gagal bayar
- Lebih stabil secara statistik
- Mudah dipelajari dan diinterpretasikan oleh model Machine Learning (khususnya Logistic Regression)

Tahap ini merupakan jembatan antara pemahaman data (EDA) dan proses pemodelan.

---

## 🧩 Input Data
- Dataset utama: `application_train.csv`
- Dataset telah melalui:
  - Validasi makna kolom
  - Seleksi fitur relevan
  - Analisis hubungan fitur dengan TARGET (EDA 3 & 4)

Tidak ada proses modeling yang dilakukan pada tahap ini.

---

## 🔑 Feature Engineering yang Dilakukan

### 1️⃣ Employment Status & Duration
- Dibuat flag status bekerja berdasarkan nilai khusus pada `DAYS_EMPLOYED`
- Durasi kerja dikonversi ke satuan tahun

**Fitur utama:**
- `FLAG_EMPLOYED`
- `EMPLOYED_YEARS`

📌 *Stabilitas pekerjaan merupakan salah satu indikator risiko terkuat.*

---

### 2️⃣ Transformasi Umur
- Umur dihitung dalam satuan tahun dari `DAYS_BIRTH`

**Fitur:**
- `AGE_YEARS`

📌 *Lebih mudah diinterpretasikan dan stabil untuk model.*

---

### 3️⃣ Rasio Finansial (Credit Risk Core Features)
Dibuat rasio untuk merepresentasikan beban finansial relatif terhadap kemampuan bayar.

**Fitur:**
- `CREDIT_INCOME_RATIO`
- `ANNUITY_INCOME_RATIO`

📌 *Rasio lebih informatif dibanding nilai absolut.*

---

### 4️⃣ Log Transformation
Dilakukan transformasi log untuk fitur numerik dengan distribusi skewed.

**Fitur:**
- `LOG_INCOME`
- `LOG_CREDIT`
- `LOG_ANNUITY`

📌 *Meningkatkan stabilitas dan linearitas hubungan dengan TARGET.*

---

### 5️⃣ Beban Keluarga
Jumlah tanggungan dikaitkan dengan tingkat pendapatan.

**Fitur:**
- `FAMILY_BURDEN`

📌 *Efek moderat namun konsisten secara bisnis.*

---

### 6️⃣ Encoding Fitur Kategorikal
Fitur kategorikal dipilih berdasarkan hasil EDA 4 dan di-encode menggunakan One-Hot Encoding.

**Fitur kategorikal utama:**
- Education Type
- Income Type
- Occupation Type
- Housing Type
- Asset Ownership (Car & Realty)

📌 Missing value dipertahankan sebagai sinyal tambahan.

---

### 7️⃣ Feature Cleanup
- Kolom mentah yang telah digantikan maknanya dihapus
- Kolom ID tidak disertakan dalam modeling

Dataset akhir berisi fitur numerik, rasio, flag, dan fitur kategorikal ter-encode.

---

## 🧠 Output Akhir Feature Engineering
Setelah tahap ini, dataset memiliki:
- Fitur risiko berbasis rasio finansial
- Flag bisnis yang bermakna
- Distribusi fitur yang lebih stabil
- Format yang siap digunakan untuk pemodelan

Dataset dinyatakan **modeling-ready**.

---

## 📌 Kesimpulan
Feature engineering dilakukan dengan menekankan stabilitas finansial, kapasitas pembayaran, dan karakteristik sosio-ekonomi nasabah. Fitur-fitur yang dihasilkan tidak hanya meningkatkan performa model, tetapi juga tetap dapat dijelaskan secara bisnis.

---

## 🔜 Langkah Selanjutnya
Tahap berikutnya adalah **Modeling**, dimulai dengan:
- Logistic Regression sebagai baseline model
- Evaluasi menggunakan ROC-AUC dan metrik terkait
