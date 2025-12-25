# 📊 Final Summary — Exploratory Data Analysis (EDA)

## 🎯 Tujuan EDA
Exploratory Data Analysis (EDA) dilakukan untuk memahami struktur, kualitas, dan makna data Home Credit, serta menentukan fitur-fitur yang relevan sebagai dasar proses feature engineering dan pemodelan risiko kredit.

---

## 🧩 EDA 1 — Data Overview & Quality Check

### Aktivitas
- Memeriksa ukuran dataset (jumlah baris dan kolom)
- Mengidentifikasi tipe data (numerik dan kategorikal)
- Mengecek proporsi missing value pada setiap fitur

### Temuan Utama
- Dataset berskala besar dengan kombinasi fitur numerik dan kategorikal
- Banyak fitur memiliki missing value, khususnya pada data sosio-ekonomi
- Missing value tidak serta-merta menunjukkan kesalahan data

### Keputusan
- Tidak melakukan penghapusan kolom secara langsung
- Seluruh fitur dianggap sebagai kandidat awal
- Analisis missing value dilanjutkan pada tahap berikutnya

---

## 🧩 EDA 2 — Validasi Makna Kolom & Anomali Data

### Aktivitas
- Mencocokkan nilai data dengan deskripsi kolom (data dictionary)
- Mengidentifikasi nilai anomali, encoding khusus, dan flag sistem
- Menganalisis missing value sebagai potensi informasi

### Temuan Utama
- Nilai negatif pada `DAYS_BIRTH` merupakan encoding umur dalam satuan hari
- Nilai ekstrem `DAYS_EMPLOYED = 365243` menandakan nasabah tidak bekerja
- Missing value pada fitur kategorikal mengandung informasi bisnis

### Keputusan
- Tidak menghapus nilai anomali tanpa konteks bisnis
- Membuat flag khusus untuk kondisi tertentu (misalnya unemployed)
- Dataset dinyatakan valid secara semantik

---

## 🧩 EDA 3 — Numerical Features vs TARGET

### Fitur yang Dianalisis
- Age (`DAYS_BIRTH`)
- Income (`AMT_INCOME_TOTAL`)
- Credit Amount (`AMT_CREDIT`)
- Employment Duration (`DAYS_EMPLOYED`)
- Family Size (`CNT_FAM_MEMBERS`, `CNT_CHILDREN`)

### Temuan Utama
- Nasabah lebih muda memiliki risiko gagal bayar lebih tinggi
- Pendapatan rendah berkorelasi dengan default rate yang lebih tinggi
- Durasi pekerjaan pendek merupakan indikator risiko yang sangat kuat
- Jumlah tanggungan memiliki pengaruh lemah namun konsisten

### Keputusan
- Menggunakan Age, Income, dan Employment Duration sebagai fitur utama
- Menerapkan transformasi log untuk fitur dengan distribusi skewed
- Mempertahankan fitur jumlah tanggungan dengan ekspektasi koefisien kecil

---

## 🧩 EDA 4 — Categorical Features vs TARGET

### Fitur Utama
- Education Type
- Income Type
- Occupation Type
- Housing Type
- Asset Ownership (Car & Realty)

### Temuan Utama
- Pendidikan rendah dan income tidak stabil memiliki default rate lebih tinggi
- Jenis pekerjaan tertentu (misalnya laborers) berisiko lebih tinggi
- Kepemilikan aset berkorelasi dengan stabilitas finansial
- Perbedaan risiko antar kategori terlihat jelas

### Keputusan
- Fitur kategorikal dinilai sangat relevan untuk pemodelan
- Missing value pada fitur kategorikal dipertahankan
- Strategi encoding ditentukan pada tahap feature engineering

---

## 🧠 Kesimpulan Akhir EDA

Setelah melalui seluruh tahapan EDA:
- Struktur dan kualitas data telah dipahami
- Makna dan konteks setiap fitur telah divalidasi
- Fitur-fitur relevan telah diidentifikasi
- Strategi transformasi dan perlakuan data telah ditentukan

EDA ini menjadi dasar yang kuat untuk melakukan feature engineering dan pemodelan risiko kredit secara sistematis dan dapat dipertanggungjawabkan secara bisnis.

---

## 🔜 Langkah Selanjutnya
Tahap berikutnya adalah **Feature Engineering**, yang mencakup:
- Pembuatan fitur rasio (misalnya credit-to-income)
- Pembuatan flag risiko
- Penentuan strategi encoding yang sesuai untuk model
