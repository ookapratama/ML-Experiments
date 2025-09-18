# Waiter Tips Prediction Project

<!-- !(https://i.ibb.co/L519V1y/plot1.png) -->

Proyek ini adalah studi kasus sederhana untuk membangun dan mengevaluasi model **Regresi Linear** yang bertujuan memprediksi besaran tips yang diberikan oleh pelanggan kepada pelayan. Model ini dilatih menggunakan dataset tips yang berisi informasi tentang total tagihan, waktu makan, hari, dan faktor lainnya.

## Ikhtisar Proyek

Tujuan utama dari proyek ini adalah untuk:
1.  **Membangun Model:** Melatih model regresi linear untuk memprediksi tips.
2.  **Mengevaluasi Kinerja:** Mengukur seberapa baik model dalam membuat prediksi.
3.  **Memahami Pentingnya Kualitas Data:** Mendemonstrasikan bagaimana kualitas data, bukan hanya kuantitas, sangat memengaruhi kinerja model.

## Dataset

Kami menggunakan dua dataset dalam proyek ini:

* `tips.csv`: Dataset asli yang berisi 244 baris data tips dari sebuah restoran. Dataset ini memiliki **korelasi alami** antara variabel `total_bill` dan `tip`, yang memungkinkan model untuk belajar dan berkinerja baik.
* `new_dataset.csv`: Versi modifikasi dari dataset tips yang diperluas menjadi 1000 baris, namun dengan data yang diisi secara acak.

**Analisis Dataset:**
Perbandingan kinerja model pada kedua dataset ini memberikan pelajaran penting: **Kualitas Data Jauh Lebih Penting dari Kuantitas Data.**

Model yang dilatih pada `tips.csv` asli menunjukkan nilai **R² sebesar 0.50**, yang berarti model mampu menjelaskan **50% dari variasi tips**. Sebaliknya, model yang dilatih pada `new_dataset.csv` menghasilkan nilai **R² negatif (-0.02)**. Ini membuktikan bahwa menambah data secara acak tanpa adanya korelasi logis akan merusak kemampuan model untuk belajar, menghasilkan kinerja yang lebih buruk daripada tebakan acak.

## Metodologi

1.  **Impor Library**: Menggunakan `pandas` untuk manipulasi data, `scikit-learn` untuk model dan metrik, serta `plotly` untuk visualisasi interaktif.
2.  **Data Preprocessing**: Mengubah variabel kategorikal (seperti `sex`, `day`, `smoker`, `time`) menjadi format numerik menggunakan **One-Hot Encoding** agar model dapat memprosesnya.
3.  **Pembagian Data**: Membagi dataset menjadi data pelatihan (80%) dan data pengujian (20%) untuk melatih dan mengevaluasi model secara terpisah.
4.  **Pelatihan Model**: Melatih model `LinearRegression` pada data pelatihan.
5.  **Evaluasi Model**: Mengukur kinerja model menggunakan metrik **Mean Squared Error (MSE)**, **Root Mean Squared Error (RMSE)**, dan **R-squared (R²)**.

## Hasil

**Kinerja Model (menggunakan `tips.csv`):**

* **R-squared (R²):** 0.50
* **Root Mean Squared Error (RMSE):** 1.15

Nilai R² = 0.50 menunjukkan bahwa model ini memiliki kekuatan prediksi yang baik. Angka RMSE = 1.15 berarti rata-rata kesalahan prediksi model sekitar $1.15 dari nilai tip yang sebenarnya, yang merupakan hasil yang sangat memuaskan untuk studi kasus ini.

## Visualisasi

!([scatter plot]https://github.com/ookapratama/ML-Experiments/tree/main/waiter%20tips%20prediction/screenshot/plot_scatter.png?raw=true)

* **Plot Prediksi vs. Nilai Aktual:** Menunjukkan seberapa dekat nilai prediksi dengan nilai sebenarnya. Titik-titik yang membentuk pola diagonal menunjukkan model yang akurat.
* **Plot Residual:** Menampilkan kesalahan prediksi. Jika titik-titik tersebar secara acak di sekitar sumbu horizontal (y=0), model dapat dianggap andal.