# Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

Link aplikasi heroku : `https://abzr-pbp-tugas2.herokuapp.com/`

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

![BAGAN-DJANGO](https://user-images.githubusercontent.com/94692166/190308162-ac56a2bc-3b0c-469e-8581-c9739f884122.png)

## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment digunakan agar kita bisa tetap melakukan development dengan tidak terjadinya bentrok antara python-python dengan versi yang berbeda di dalam komputer kita. Virtual environment melakukan isolasi lingkungan dari python yang digunakan dalam suatu directory yang sudah kita locate.

Kita bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tapi versi-versi python dan libraries yang digunakan harus kita perhatikan agar tidak terjadi bentrok antara versi-versi yang berbeda.

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

1. Melakukan migrasi terlebih dahulu dengan `python manage.py makemigrations` lalu `python manage.py migrate`
2. Membuat fungsi dalam `views.py` yang menerima parameter request dan mengembalikan render dengan context yang ada
3. Menambahkan iterasi dari list yang ada pada `views.py` dalam `katalog.html` untuk menampilkan katalog yang sudah ada di dalam folder fixtures
4. Menambah path di dalam `urls.py` dari katalog untuk fungsi `show_catalog` yang sudah dibuat di `views.py`
5. Menambah path `urls.py` dari katalog di dalam `urls.py` dari project_django
6. Add, commit, dan push perubahan-perubahan tersebut ke github
7. Membuat aplikasi baru di dalam website heroku dan memberi nama aplikasi tersebut
8. Menambahkan nama aplikasi dan API key sebagai secret variable di dalam repository secret
9. Website bisa di deploy

