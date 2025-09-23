# Future Sales Prediction Project

## Ikhtisar Proyek

Proyek ini adalah studi kasus sederhana untuk membangun dan mengevaluasi model **Regresi Linear** yang bertujuan memprediksi penjualan di masa depan. Model ini dilatih menggunakan data iklan historis yang mencakup pengeluaran di **TV, radio, dan koran** untuk memprediksi nilai penjualan (`Sales`).

## Fitur dan Fungsionalitas

-   **Analisis Data Eksploratif (EDA)**: Pemahaman mendalam tentang dataset.
-   **Pra-pemrosesan Data**: Memisahkan fitur (`TV`, `Radio`, `Newspaper`) dan target (`Sales`).
-   **Pelatihan Model**: Membangun dan melatih model regresi linear.
-   **Evaluasi Model**: Mengukur kinerja model.
-   **Visualisasi Hasil**: Menggunakan Plotly untuk memvisualisasikan prediksi dan kesalahan model.

## Metodologi

1.  **Impor Library**: Menggunakan `pandas` untuk manipulasi data dan `scikit-learn` untuk model.
2.  **Pra-pemrosesan Data**: Mengidentifikasi variabel fitur (`X`) dan variabel target (`y`).
3.  **Pembagian Data**: Membagi data menjadi 80% untuk pelatihan dan 20% untuk pengujian.
4.  **Pelatihan dan Evaluasi Model**: Melatih model `LinearRegression` dan mengevaluasi kinerjanya.

## Hasil

**Kinerja Model :**

* **R-squared (R²):** 0.91
* **Root Mean Squared Error (RMSE):** 1.71

Nilai R² = 0.91 indikator yang sangat kuat bahwa model Anda berhasil dalam memprediksi data. menunjukkan bahwa model ini memiliki kekuatan prediksi yang baik. Nilai RMSE 1.71 ini berarti rata-rata kesalahan prediksi model Anda adalah 1.71 unit penjualan. Misalnya, jika data penjualan Anda dalam ribuan dollar, maka rata-rata kesalahan model adalah $1,710.

* **Hasil Evaluasi:** Menunjukkan seberapa akurat model yang kita gunakan dalam memprediksi hasil sales ke depannya.
![Hasil evaluasi](https://github.com/ookapratama/ML-Experiments/blob/main/future_sales_prediction/screenshot/score.png)

## Visualisasi

* **Plot Prediksi vs. Nilai Aktual:** Menunjukkan seberapa dekat nilai prediksi dengan nilai sebenarnya. Titik-titik yang membentuk pola diagonal menunjukkan model yang akurat.
![scatter plot](https://github.com/ookapratama/ML-Experiments/blob/main/future_sales_prediction/screenshot/plot_scatter.png)

* **Plot Residual:** Menampilkan kesalahan prediksi. Jika titik-titik tersebar secara acak di sekitar sumbu horizontal (y=0), model dapat dianggap andal.
![scatter residual](https://github.com/ookapratama/ML-Experiments/blob/main/future_sales_prediction/screenshot/plot_residual.png)

