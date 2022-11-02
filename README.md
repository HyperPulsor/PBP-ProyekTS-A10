# Proyek Tengah Semester Mata Kuliah Pemrograman Berbasis Platform (PBP) - Membuat Website menggunakan Framework Django (Berkelompok)
## Nama Anggota Kelompok Kelompok A10
1. Amanda Nadhifah Zahra Andini - 2106637246
2. Annisa Az Zahra - 2106701242
3. Caroline Esther Ulibasa Panggabean - 2106751915
4. Jihan Hanifah Yasmin - 2106701955
5. Rakan Fasya Athhar Rayyan - 2106750950
6. Rangga Yudhistira Brata - 2106751051
7. Vinsensius Ferdinando - 2106751221

## Tautan Aplikasi Heroku
[🛍 App Page Medsos UMKM - A10](https://medsos-umkm.herokuapp.com/)

## Cerita Aplikasi
Berangkat dari rencana pemerintah untuk membangkitkan ekonomi nasional pasca pandemi COVID-19. Kemudian, berkaitan juga dengan topik *Digitalisation and Innovation* pada G20 digital agenda yang bertujuan untuk membantu suatu negara memanfaatkan transformasi digital. Pemanfaatan transformasi digital tersebut yaitu sebagai media penciptaan lapangan kerja dan keberlangsungan bisnis. Aplikasi yang kelompok kami rencanakan adalah suatu aplikasi yang mempertemukan para pelaku usaha mikro kecil dan menengah (UMKM) dengan para pembeli. Harapannya aplikasi ini dapat membantu para pelaku UMKM untuk mengembangkan usahanya dengan menjangkau lebih banyak *customer*. Sebab jangkauan yang lebih luas kepada para calon *customer* akan membantu para pelaku UMKM untuk bisa meningkatkan pendapatan dan mengembangkan usahanya.
User aplikasi ini adalah pelaku UMKM dan calon *customer*. Pelaku UMKM dapat mempromosikan usahanya dengan memposting profil usaha yang mereka jalankan serta produk atau jasa yang mereka tawarkan. Sementara itu, calon *customer* dapat mengakses produk tersebut melalui redirect link ke e-commerce masing masing pelaku UMKM. 

	
## Daftar Fitur yang ingin Diimplementasi
### 1. Fitur Login, Logout & Register
Pada fitur ini akan terdapat tiga role untuk user yakni buyer, seller, dan admin. Ketiga role tersebut akan mengisi form di halaman Login untuk mengakses fitur di dalam website. Melalui bagian Login juga akan dilakukan autentikasi dan autorisasi terhadap user. Pada bagian register, user juga akan mengisi data dirinya sesuai dengan role masing-masing, user diberikan pilihan untuk mendaftar sebagai buyer atau seller. 

**Input Form Login:**
- Username / Email
- Password

**Input Form Register Buyer:**
- Nama
- Username
- Email
- Password

**Input Form Register Seller:**
- Nama
- Username
- Email
- Password
- Nama Usaha
- Kategori Usaha (Dropdown Kategori)
- Deskripsi Singkat Usaha
- Alamat Usaha 
- Kontak Pribadi / Usaha
- Link Toko atau Kontak untuk Redirect ke Halaman Pembelian (Platform E-commerce atau WA Bisnis)


### 2. Halaman Profil User
User dengan Role Seller dan Buyer dapat melihat dan mengubah profilnya masing-masing di halaman ini. Bagian yang dapat diubah adalah username, email, dan passsword berdasarkan input yang telah diberikan ketika user mengisi form register berdasarkan role-nya masing-masing.

### 3. Fitur add product katalog dan edit catalog untuk Seller
User dengan role Seller dapat menambahkan produk ke katalog tokonya masing-masing dengan mengisi form terkait produk yang ingin ditambahkan. Kemudian seller juga dapat mengubah katalog dengan menghapus produk yang diinginkan.

**Input Form Produk:**
- Nama Produk
- Kategori Produk
- Harga Produk
- Gambar Produk (>1 gambar)
- Deskripsi lengkap produk
- Link Redirect Produk

### 4. Fitur add FAQ, validasi barang yang dijual seller, dan add kategori produk untuk Admin
User dengan role Admin dapat mengisi form untuk menambahkan tampilan FAQ di landing page, kemudian melakukan validasi tiap produk yang diposting oleh Seller dengan klik button approve atau tidak sebelum produk ditampilkan di website, serta add kategori produk di website.

**Input Form FAQ:**
- Pertanyaan
- Jawaban atas Pertanyaan

### 5. Menampilkan daftar barang, toko dan kategori produk, serta fitur search untuk buyer di landing page
Daftar kategori yang dibuat admin, toko dan daftar produk yang dibuat oleh seller, serta fitur search yang dapat digunakan oleh buyer untuk mencari toko dan produk yang mereka inginkan.

### 6. Menampilkan card produk dan detail produk dan implementasi fitur bookmark toko atau produk untuk buyer
Detail tiap produk yang telah dibuat oleh seller akan ditampilkan ketika buyer meng-klik button di card produk untuk menuju ke halaman detail produk. Pada card akan ditampilkan foto pertama yang diupload oleh buyer sebagai thumbnail representasi dari tiap produk.

### 7. Fitur forum diskusi antara seller dan buyer
Pada fitur forum masing-masing user dapat memilih topik (filter) yang ingin mereka baca dan diskusikan. Buyer dan Seller dapat saling berinteraksi memposting pendapat mereka, bertanya, menjawab, dan lainnya dengan mengisi form. Selain itu user juga dapat melakukan sorting berdasarkan forum terbaru (waktu posting). Khusus untuk user dengan role admin, admin dapat menghapus forum yang tidak pantas. 

**Input Form Forum Diskusi:**
- Judul topik diskusi
- Isi pesan diskusi

### Role Pengguna
1. User Guest (Belum Login):
- Melihat landing page
- Melihat kategori, toko, dan produk
- Membuat akun sebagai seller atau buyer

2. User Buyer (Login):
- Melihat landing page
- Melihat kategori, toko, dan produk
- Melakukan bookmark terhadap produk yang menarik
- Mengedit profil diri
- Melakukan diskusi di forum dan memanfaatkan fitur di forum
- Melakukan pencarian terhadap kategori, toko, atau produk yang menarik

3. User Seller (Login):
- Melihat landing page
- Melihat kategori, toko, dan produk
- Mengedit profil diri dan informasi toko 
- Melakukan diskusi di forum dan memanfaatkan fitur di forum
- Mengedit katalog produk dan menambahkan produk ke katalog

4. Admin:
- Melihat landing page
- Melihat kategori, toko, dan produk
- Mengedit profil diri dan informasi toko 
- Menyetujui forum yang akan diposting oleh seller atau buyer dan produk yang akan diposting oleh seller
- Menghapus forum atau produk yang tidak pantas
- Menambahkan FAQ pada landing page

## Referensi
> https://developers.bri.co.id/id/news/digitalisasi-umkm-dongkrak-pendapatan-umkm-di-2022

> https://www.oecd.org/g20/topics/

> https://gitlab.com/muhammad.haqqi01/c06-pts-pbp/-/blob/master/README.md



