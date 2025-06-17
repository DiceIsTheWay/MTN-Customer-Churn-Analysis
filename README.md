# MTN-Customer-Churn-Analysis

## Repository Outline
```
1. README.md - Penjelasan gambaran umum project
2. DDL.txt - Syntax DDL untuk pembuatan table dan Syntax DML untuk melakukan insert data ke database.
3. GX_Data_Validation.ipynb - Notebook yang berisi validasi data dengan python Great Expextations (GX).
4. DAG.py - Program python untuk automasi data processing mulai dari fetch data dari PostgreSQL sampai load data ke Elasticsearch.
5. DAG_graph.jpg - Screenshot yang menampilkan alur graph dari DAG yang dibuat.
6. P2M3_Dais_data_raw.csv - Dataset raw yang digunakan dalam data processing.
7. P2M3_Dais_data_clean.csv - Dataset clean yang digunakan dalam data validation dan visualisasi data pada Elasticsearch Kibana.
8. /Images - Berisi file gambar screenshot dashboard yang telah dibuat menggunakan kibana.
```

## Problem Background
```
MTN adalah salah satu perusahaan telekomunikasi terbesar di Nigeria dan customer churn merupakan salah satu tantangan terbesar bagi perusahaan telekomunikasi. Dalam industri ini, pelanggan memiliki banyak pilihan operator, dan loyalitas pelanggan dapat dengan mudah menurun dengan adanya Harga layanan yang lebih murah, kualitas jaringan yang lebih baik, atau layanan pelanggan yang lebih superior yang bisa ditawarkan operator pesaing. Menurut salah satu artikel pada industri telekomunikasi terkenal memiliki churn rate yang relatif tinggi, dengan rata-rata berkisar antara 15-25% per tahun untuk layanan seluler (source: https://www.liputan6.com/feeds/read/5774834/churn-rate-adalah-pengertian-cara-menghitung-dan-strategi-menurunkannya?page=3). Oleh karena itu, diperlukan analisis untuk mengetahui pola perilaku pelanggan yang melakukan churn melalui visualisasi data pelanggan MTN pada Q1-2025 agar bisa didapatkan rekomendasi bisnis yang tepat untuk mencegah customer churn pada periode selanjutnya.
```

## Project Output
```
Saya merupakan seorang Data Analyst yang sedang membantu tim customer experience dan retensi pelanggan di MTN Nigeria. Report ini akan menghasilkan hasil analisis karakteristik pelanggan yang melakukan churn berdasarkan perilaku penggunaan layanan, keluhan, dan atribut demografis lainnya. Selain karakteristik perilaku pelanggan yang diberikan, ada juga saran-saran/rekomendasi bisnis untuk promosi atau strategi bisnis yang mungkin bisa dijadikan bahan pertimbangan tim customer retention dan marketing untuk mengurangi customer churn rate.
```

## Data
```
Dataset yang digunakan adalah MTN Nigeria Customer Churn yang bersuber dari kaggle. Dataset ini memiliki 17 kolom dan 974 baris, terdapat missing values pada kolom 'Reasons for Churn' tetapi missing value tersebut ada dikarenakan user yang tidak churn tidak mengisi kolom tersebut.
```

## Method
``` 
Pada project ini dilakukan proses automasi data process scheduling menggunakan airflow mulai loading data dari postgreSQL, data cleaning, hingga loading data ke Elasticsearch untuk selanjutnya proses visualisasi data untuk EDA, dan juga dilakukan data validation menggunakan Great Expectation terhadap data yang sudah dicleaning. 
```

## Stacks
```
Stacks yang digunakan adalah PostgreSQL, Visual Studio Code, Apache Airflow, Elasticsearch & Kibana, Docker, dan untuk library Python yang digunakan adalah:
- pandas
- datetime
- airflow
- psycopg2
- Elasticsearch
- great_expectations
```

## Reference
```
https://www.liputan6.com/feeds/read/5774834/churn-rate-adalah-pengertian-cara-menghitung-dan-strategi-menurunkannya?page=3
```