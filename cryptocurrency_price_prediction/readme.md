# Proyek Prediksi Harga Cryptocurrency

<p align="center">
  <img src="https://github.com/ookapratama/ML-Experiments/blob/main/cryptocurrency_price_prediction/screenshot/thumbnail.jpeg" alt="Visualisasi Utama Proyek" width="800"/>
</p>

Proyek ini adalah studi kasus untuk membangun dan mengevaluasi model **Machine Learning** yang mampu memprediksi harga cryptocurrency. Model ini dilatih menggunakan data historis harga, volume, dan metrik pasar lainnya untuk membuat prakiraan harga **30 hari** ke depan. Proyek ini mendemonstrasikan alur kerja lengkap dari analisis data eksplorasi (EDA), analisis statistik, hingga pelatihan dan evaluasi model.

---

## Ikhtisar Proyek

Tujuan utama dari proyek ini adalah:
1.  **Membangun Model:** Melatih model _time series forecasting_ untuk memprediksi harga cryptocurrency.
2.  **Mengevaluasi Kinerja:** Mengukur akurasi model menggunakan metrik standar seperti MAE, RMSE, dan MAPE.
3.  **Visualisasi Hasil:** Menyajikan data historis, analisis, dan hasil prediksi dalam bentuk visual yang mudah dipahami.

---

## Metodologi

1.  **Analisis Data Eksplorasi (EDA):** Tahap awal untuk memahami karakteristik data cryptocurrency, termasuk tren harga, volume perdagangan, dan distribusi keuntungan harian.

2.  **Analisis Statistik:** Melakukan analisis lebih dalam untuk mengidentifikasi pola, seperti:
    * **Moving Averages:** Menggunakan rata-rata bergerak 7-hari dan 30-hari untuk mengidentifikasi tren.
    * **Rolling Volatility:** Mengukur fluktuasi harga untuk menilai risiko pasar.
    * **Korelasi Harga vs Volume:** Menganalisis hubungan antara harga dan volume.

3.  **Konfigurasi Model:** Menggunakan model **Ensemble** untuk menggabungkan prediksi dari beberapa model lain demi hasil yang lebih akurat. Model dikonfigurasi untuk memprediksi harga dalam horizon **30 hari** ke depan.

4.  **Pelatihan dan Evaluasi:** Data dibagi menjadi set pelatihan (949 hari) dan pengujian (50 hari). Kinerja model diukur menggunakan metrik akurasi standar.

---

## Hasil dan Performa Model

Model **Ensemble** yang dilatih menunjukkan performa yang sangat baik dalam memprediksi harga cryptocurrency. Metrik akurasi yang diperoleh adalah:

* **MAE (Mean Absolute Error):** $$4,713.45
* **RMSE (Root Mean Squared Error):** $$5,760.20
* **MAPE (Mean Absolute Percentage Error):** 4.19%

Nilai **MAPE 4.19%** menunjukkan bahwa rata-rata kesalahan prediksi model hanya sekitar 4.19% dari harga sebenarnya, yang merupakan hasil **sangat memuaskan** untuk prediksi di pasar keuangan yang volatil.

<br>

**Hasil Evaluasi:**
![Metrik Akurasi Model](https://github.com/ookapratama/ML-Experiments/blob/main/cryptocurrency_price_prediction/screenshot/eval_acc_metrics.png)
Grafik di atas membandingkan harga aktual (biru) dan harga prediksi (merah), menunjukkan seberapa dekat perkiraan model dengan pergerakan pasar yang sebenarnya. Plot residual menunjukkan kesalahan prediksi yang tersebar acak, menandakan model yang andal tanpa bias yang signifikan.

---

## Visualisasi

### 1. Analisis Data Eksplorasi (EDA)
![EDA Visual](https://github.com/ookapratama/ML-Experiments/blob/main/cryptocurrency_price_prediction/screenshot/eda_visual.png)
Visualisasi ini memberikan gambaran umum data, termasuk pergerakan harga dan volume dari waktu ke waktu, distribusi harga, serta volatilitas harian.

---

### 2. Analisis Statistik
![Statistik Analisis](https://github.com/ookapratama/ML-Experiments/blob/main/cryptocurrency_price_prediction/screenshot/statistic_analysis.png)
Menampilkan analisis yang lebih mendalam, seperti rata-rata bergerak, volatilitas bergulir, dan hubungan antara harga dan volume.

---

### 3. Prediksi Harga 30 Hari
![Prediksi Visual](https://github.com/ookapratama/ML-Experiments/blob/main/cryptocurrency_price_prediction/screenshot/prediction_visual.png)
Grafik utama yang menunjukkan hasil prediksi model. Garis putus-putus merah adalah prakiraan harga untuk 30 hari ke depan, dikelilingi oleh area merah muda yang merepresentasikan **Confidence Interval**, atau rentang ketidakpastian prediksi.