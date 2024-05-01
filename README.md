# Dokumentasi Proyek Akhir Algoritma dan Struktur Data #
## Implementasi Algoritma dan Struktur Data pada Platform Sistem Informasi Pendidikan dan Pencarian Sekolah Pendidikan Sistem Informasi di Samarinda ##
### Anggota Kelompok ###

**•	Nyoman Arini Trirahayu** -2309116002

**•	Hana Anastasya Wardah** -2309116012

**•	Widia Saputri** -2309116019

**•	Farhan Imanudin** -2309116028

## Daftar Isi ##

- [Deskripsi Program](#deskripsi-program)
- [Implementasi Modul](#implementasi-modul)
- [Instalasi Modul](#instalasi-modul)
- [Struktur Program](#struktur-program)
- [ERD Database](#erd-database)
  - [ERDISH](#erdish)
  - [Entitas](#entitas)
  - [Relasi](#relasi)
  - [Kardinalitas](#kardinalitas)
- [Fitur dalam Program](#fitur-dalam-program)
- [Fungsional](#fungsional)
- [Cara Penggunaan](#cara-penggunaan)
  - [Opsi Awal](#opsi-awal)
  - [Tampilan Admin](#tampilan-admin)
  - [Tampilan User](#tampilan-user)


## Deskripsi Program ##
PENSI didesain untuk mengakomodasi kebutuhan berbagai pemangku kepentingan (stakeholders) dalam konteks sistem informasi sekolah di Samarinda. PENSI dirancang untuk mengatasi tantangan tersebut dengan menyediakan solusi yang efisien dan terpadu dalam mendapatkan informasi tentang sekolah-sekolah di Samarinda. Melalui fitur-fitur seperti pencarian sekolah, pengurutan, ulasan, dan pelaporan kekurangan, PENSI diharapkan dapat membantu masyarakat Samarinda dalam memperoleh informasi yang lengkap dan akurat tentang sekolah, sementara pihak sekolah dapat memanfaatkan umpan balik untuk terus meningkatkan kualitas pendidikan yang mereka tawarkan

## Implementasi Modul ##

Adapun Modul yang digunakan dalam Project ini adalah :

- **OS** : yaitu modul bawaan yang menyediakan akses ke fungsionalitads sistem operasi.
  
- **Mysql.connector** : yaitu modul yang menyediakan antarmuka untuk berinteraksi dengan database MySQL. Dengan menggunakan modul ini, Anda dapat terhubung ke database MySQL, mengeksekusi perintah SQL, dan melakukan operasi lain seperti menyisipkan, memperbarui, atau menghapus data.

- **PrettyTable** : yaitu modul yang digunakan untuk memanipulasi visual data yang akan ditampilkan dalam view.

- **Math** : yaitu modul yang menyediakan fungsi matematika yang diperlukan untuk melakukan operasi matematika lanjutan. Anda dapat menggunakan modul ini untuk menghitung akar kuadrat, logaritma, trigonometri, dan operasi matematika lainnya.

- **DateTime** : yaitu modul yang digunakan untuk mengambil data tanggal dan waktu.


## Instalasi Modul ##

 `pip install mysql-connector-python`

 `pip install prettytable`
  
 `pip install pwinput`
  
 `pip install math`
  
 `pip install python-Date-Time`
  

## Struktur Program ##
-

## ERD DATABASE ##

![PA SEM 2 fixx drawio (2) drawio](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/f60f9e63-19fa-4e9d-bfd8-a830afbaa60e)

## ERDISH ##
• Setiap admin sekolah harus memiliki satu dan hanya satu sekolah setiap sekolah harus 
dimiliki oleh satu dan hanya satu admin sekolah.

• Setiap admin data harus mendata banyak sekolah dan banyak sekolah didata oleh satu 
dan hanya satu admin data.

• Setiap sekolah dapat mendapat banyak rating dan ulasan dan banyak rating dan ulasan 
dapat didapat oleh satu dan hanya satu sekolah.

• Setiap akun user dapat memberi banyak rating dan ulasan dan setiap banyak rating dan 
ulasan dapat diberi oleh satu dan hanya satu akun user.

• Setiap akun user dapat memberi banyak laporan dan setiap banyak laporan dapat diberi 
oleh satu dan hanya satu akun user.

• Setiap admin laporan harus menindak banyak laporan dan setiap banyak laporan harus 
ditindak oleh satu dan hanya satu admin laporan.

## ENTITAS ##
Entitas yang ada dalam sistem informasi sekolah (PENSI) terdapat 8 entitas
• Admin Sekolah: Bertanggung jawab atas manajemen dan pengelolaan profil 
sekolah di aplikasi PENSI. Mereka dapat memperbarui informasi sekolah, seperti 
kontak, alamat, dan detail lainnya. Atributnya: fk ID_Sekolah, Username, 
Nama_Lengkap, pk ID_Admin_Sekolah, Password.

• Sekolah: Merupakan lembaga pendidikan di Samarinda yang diinformasikan dalam 
aplikasi PENSI. Sekolah-sekolah ini memiliki profilnya sendiri dalam aplikasi, 
yang mencakup informasi seperti kontak, alamat, dan detail lainnya. Melalui entitas 
sekolah, pengguna dapat mencari dan mengetahui informasi terkait sekolah-sekolah 
di Samarinda. Atributnya: Nomor_Induk_Sekolah, pk ID_Dekolah, fk 
ID_Admin_Data, Nama_Sekolah, Akreditas.

• Admin Data: Bertanggung jawab atas manajemen data sekolah secara umum dalam 
aplikasi PENSI. Mereka memiliki kewenangan untuk memperbarui dan mengelola 
informasi tentang sekolah-sekolah di Samarinda. Atributnya: pk ID_Admin_Data, 
Username, Password, Nama_Lengkap, Jenjang (SD, SMP, SMA, SMK).

• Akun User: Merupakan pengguna aplikasi PENSI yang memiliki akun terdaftar. 
Mereka dapat melakukan lebih banyak interaksi dalam aplikasi, seperti memberikan 
ulasan, memberi rating, dan melaporkan kekurangan/pelanggaran. 
Atributnya: pk ID_Akun_User, Username, Password, Email, Nama_Lengkap.

• Rating dan Ulasan: Fungsi: Menyimpan feedback atau ulasan yang diberikan oleh 
pengguna tentang pengalaman mereka dengan sekolah tertentu. Rating dan ulasan 
membantu calon siswa dan orang tua dalam membuat keputusan yang lebih baik 
dalam memilih sekolah. Atributnya: pk ID_Rating_dan_Ulasan, fk ID_Akun_User, 
fk ID_Sekolah, Tanggal_Diberikan, Ulasan, Rating.

• Laporan: Menyimpan laporan yang dibuat oleh pengguna tentang kekurangan atau 
pelanggaran yang mereka temui dalam proses pembelajaran di sekolah. Laporan ini 
membantu sekolah dalam meningkatkan kualitas pendidikan dan memperbaiki 
masalah yang ada. Atributnya: Status, pk ID_Laporan, fk ID_Akun_User, 
Nama_Sekolah, Tanggal_Dibuat, fk Admin_Laporan, Isi_Laporan.

• Admin Laporan: Fungsi: Bertanggung jawab atas penanganan laporan yang masuk 
dalam aplikasi PENSI. Mereka memiliki kewenangan untuk menangani laporan 
yang dibuat oleh pengguna dan mengambil tindakan yang diperlukan untuk 
memperbaiki masalah yang dilaporkan. Atributnya: Jenjang(SD, SMP, SMA, 
SMK), Username, pk ID_Admin_Laporan, Password, Nama_Lengkap.

## RELASI ##
Relasi sistem informasi sekolah PENSI adalah sebagai berikut, 

• Admin Sekolah - Sekolah (Milik): Hubungan ini menunjukkan bahwa setiap 
sekolah dimiliki oleh satu dan hanya satu admin sekolah tertentu. Admin sekolah 
memiliki kendali penuh atas manajemen dan pengelolaan sekolah yang mereka 
kelola dalam aplikasi PENSI.

• Admin Data - Sekolah (Data): Ini menunjukkan bahwa setiap admin data 
bertanggung jawab atas pengumpulan informasi dan pembaruan data dari banyak 
sekolah di aplikasi PENSI. Setiap sekolah didata oleh satu admin data tertentu untuk 
memastikan konsistensi dan akurasi informasi.

• Sekolah - Rating dan Ulasan (Dapat): Ini menunjukkan bahwa setiap sekolah 
mendapat banyak rating dan ulasan dari pengguna dalam aplikasi PENSI. 
Sebaliknya, setiap rating dan ulasan didapat oleh satu sekolah tertentu.

• Akun User - Rating dan Ulasan (Beri): Ini menunjukkan bahwa setiap akun user 
memiliki kemampuan untuk memberikan banyak rating dan ulasan tentang sekolahsekolah di aplikasi PENSI. Sebaliknya, setiap rating dan ulasan diberikan oleh satu 
dan hanya satu akun user tertentu.

• Akun User - Laporan (Buat): Ini menunjukkan bahwa setiap akun user memiliki 
kemampuan untuk membuat banyak laporan tentang kekurangan atau pelanggaran 
yang mereka temui dalam aplikasi PENSI. Sebaliknya, setiap laporan dibuat oleh 
satu dan hanya satu akun user tertentu.

• Admin Laporan - Laporan (Tindak): Ini menunjukkan bahwa setiap admin laporan
memiliki tanggung jawab untuk menindak laporan yang masuk terkait sekolah yang 
mereka kelola dalam aplikasi PENSI. Sebaliknya, setiap laporan harus ditindak oleh 
satu dan hanya satu admin laporan tertentu untuk memastikan tindakan yang 
diperlukan diambil dengan tepat.

## KARDINALITAS ##
Kardinalitas yang digunakan antara lain:

### 1. One to One (satu ke satu) ###
• Admin Sekolah – Sekolah: Kardinalitas ini mandatory, karena setiap sekolah 
harus memiliki satu admin sekolah yang bertanggung jawab atas manajemen dan 
pengelolaan profil sekolah.

### 2. One to Many (satu ke banyak) ###
• Admin Data – Sekolah: Kardinalitas ini mandatory, karena setiap sekolah harus 
didata oleh minimal satu admin data, namun satu admin data dapat mendata 
banyak sekolah.

• Sekolah - Rating dan Ulasan: Kardinalitas ini optional, karena tidak semua user 
anonim harus membuat akun user. Namun, jika mereka memilih untuk membuat 
akun, setiap user anonim hanya dapat membuat satu akun user.

• Akun User - Rating dan Ulasan: Kardinalitas ini optional, karena tidak semua 
sekolah harus memiliki rating dan ulasan. Namun, jika ada, setiap sekolah dapat 
menerima banyak rating dan ulasan.

• Akun User – Laporan: Kardinalitas ini optional, karena tidak semua akun user 
harus memberikan rating dan ulasan. Namun, jika ada, setiap akun user dapat 
memberikan banyak rating dan ulasan.

• Admin Laporan – Laporan: Kardinalitas ini mandatory, karena admin laporan 
harus menindak lapor

## FLOWCHART

* Menu Admin Laporan
![PA ASD 1-Halaman-1 revisi drawio](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/31e571a3-0709-40e2-984f-2713e24bd649)
* Menu Admin Data
![PA ASD 1-Halaman-2 drawio](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/92db1c5e-2759-4d6b-aefd-8e80801e3afe)
* Menu Sorting dan Searching Admin Data
![PA ASD 1-Halaman-3 drawio](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/e7f079d4-8cfe-4dc5-96c8-7f137c94af9b)
* Menu Admin Sekolah
![PA ASD 1-Halaman-4 drawio](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/b4be86d3-8fef-4ef2-adc8-3a166becd895)
* Menu Admin Laporan
![PA ASD 1-Halaman-5 drawio](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/81893a97-205d-4606-9eae-b5f398d34239)
* Menu User
![PA ASD 1-Halaman-6 drawio](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/50b68735-c9e9-46bc-b814-5bd843dc79ae)
* Menu User Pilihan 1
![PA ASD 1-Halaman-7 drawio](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/6691eb17-71fd-4502-bb14-1efdb54e5a8f)

## FITUR DALAM PROGRAM 

### Admin Data 
1. Tambah Data Sekolah: Opsi ini digunakan admin data untuk menambahkan data tentang sebuah sekolah ke dalam sistem.
2. Lihat Data Sekolah: Pengguna dapat melihat daftar sekolah yang telah dimasukkan ke dalam sistem.
3. Perbarui Data Sekolah: Opsi ini digunakan admin data untuk memperbarui informasi tentang sebuah sekolah yang telah ada dalam sistem.
4. Hapus Data Sekolah: admin data dapat menghapus informasi tentang sebuah sekolah dari sistem.
5. Shorting: Opsi ini digunakan pengguna untuk mengurutkan daftar sekolah berdasarkan kriteria tertentu sesuai Nama Sekolah, ID sekolah atau akreditasi sekolah secara ascending dan discanding.
6. Searching: admin data dapat mencari sekolah berdasarkan kriteria tertentu, seperti nama sekolah atau akreditasi.
0. Keluar: Opsi ini memungkinkan admin data untuk Kembali ke menu utama.

### Admin Sekolah
1. Lihat Data Sekolah: Opsi ini memungkinkan admin sekolah untuk melihat daftar sekolah yang terdaftar dalam sistem.
2. Lihat Data Admin Sekolah: Admin sekolah dapat melihat informasi tentang informasi data admin sekolahnya yang terdaftar dalam sistem.
3. Perbarui Data Admin Anda: Admin sekolah dapat menggunakan opsi ini untuk memperbarui informasi mereka sendiri, seperti nama, alamat email, atau kata sandi.
4. Perbarui Data Sekolah Anda: Admin sekolah dapat menggunakan opsi ini untuk memperbarui informasi tentang sekolah mereka, seperti Nama Sekolah, Nomor Induk Sekolah dan Akreditasi Sekolah.
0. Kembali: Opsi ini memungkinkan admin sekolah untuk kembali ke menu utama.

### User 
1. Lihat Data Sekolah: Pengguna dapat melihat informasi tentang sekolah yang terdaftar dalam sistem, termasuk detailnya seperti nama sekolah, alamat, dan informasi lainnya.
2. Login Akun User: Pengguna dapat masuk ke dalam akun mereka dengan menyediakan informasi login yang valid, seperti email dan password mereka.
0. Kembali: Opsi ini memungkinkan pengguna untuk kembali ke menu utama.

### Akun User
1. Lihat Data Sekolah: Pengguna dapat melihat informasi tentang sekolah yang terdaftar dalam sistem.
2. Berikan Rating dan Ulasan: Pengguna dapat memberikan rating dan ulasan untuk sekolah yang mereka kunjungi atau yang mereka ketahui.
3. Laporkan Sekolah: Pengguna dapat melaporkan sekolah jika mereka mengalami masalah atau menemukan kekurangan dalam pelayanan atau fasilitasnya.
0. Kembali: Opsi ini memungkinkan pengguna untuk kembali ke menu utama.


## Fungsional

1. CRUD Sekolah, admin dapat melakukan penambahan data baru ke dalam sistem, melihat data yang sudha ada di dalam sistem, memperbarui data yang sudah ada di dalam sistem, dan menghapus data yang ada di dalam sistem.
2. Registrasi Admin Sekolah, Admin Sekolah dapat melakukan registrasi dengan memasukan id sekolahnya jadi setiap satu sekolah harus memilki satu admin sekolah.
3. Login/Registrasi User, pengguna atau user di sini dapat melakukan registrasi jika belum memilki akun agar bisa memberikan rating?ulasan dan laporan ke pada sekolah tersebut.
4. Admin Sekolah, Admin sekolah dapat melihat datanya pribadi dan dapat melakukan pembaruan data sekolahnya sendiri serta data pribadinya sendiri dengan pengawasan dari admin data.
5. User, pengguna atau user dapat melihat sekolah tanpa harus login dulu, jadi pengguna dapat melakukan seraching dan sorting data sekolah tanpa harus login terlebih dahulu.

## Cara Penggunaan 
### Opsi Awal 

Ketika program pertama kali dijalankan user akan ditampilkan empat opsi awal yaitu "Admin", “User” dan "Keluar. Admin adalah opsi untuk masuk kedalam menu menu admin, lalu “User” adalah opsi untuk masuk kedalam menu user, dan opsi “keluar” untuk menutup program.
![1 Menu awal](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/b52fc549-9a03-44de-a2ed-23a8229a9539)



### Menu Login Admin
Pada saat memilih pilihan admin, akan terdapat menu login admin yang terdiri dari, “Admin Data”, “Admin Sekolah”, “Admin Laporan”, dan “Keluar”.

![2 menu admin](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/25cf71f3-51e6-4906-b78e-565570836059)


### Admin Data

Apabila memilih pilihan 1, Admin Data akan diarahkan untuk memasukkan ID Admin Data dan Password. 

![3 login admin data](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/da21abe7-9219-4d8f-b197-e69918085d6c)


### Menu Admin Data

Apabila telah sukses login sebagai Admin Data, akan terdapat Menu Admin Data yang terdiri dari: “Tambah Data Sekolah”, “Lihat Data Sekolah”, “Perbarui Data Sekolah”, “Hapus Data Sekolah”, “Sorting”, “Searching”, dan “Keluar”.

![4 menu admin data opsi 1](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/ecf86625-4408-4367-8bfc-9df68ff8bbfa)


### Tambah Data Sekolah

Opsi Tambah Data Sekolah digunakan untuk menambahkan data sekolah dengan memasukkan data sekolah yaitu: Nama Sekolah, Nomor Induk Sekolah, dan Akreditasi Sekolah.

![4 menu admin data opsi 1](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/2e3792ab-feeb-4392-8d36-e10cea4a7d11)


### Lihat Data Sekolah
Opsi Lihat Data Sekolah digunakan untuk melihat data sekolah yang terdiri dari: “ID Sekolah”, “ID Admin Data”, “Nama Sekolah”, “Nomor Induk Sekolah”, dan “Akreditasi”. 

![WhatsApp Image 2024-05-01 at 21 38 49_a06bfb36](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/8924cd05-4dae-4448-9f8c-9f5c359bd48c)


### Perbarui Data Sekolah
Opsi Perbarui Data Sekolah digunakan jika ingin memperbarui data sekolah dan akan langsung diarahkan untuk memasukkan ID Sekolah yang ingin diperbarui. Setelah memasukan ID Sekolah, akan ditampilkan Data Sekolah saat ini dan dapat memasukkan data sekolah yang ingin diperbarui.


### Hapus Data Sekolah

Opsi Hapus Data Sekolah digunakan untuk menghapus data sekolah dengan memasukkan ID sekolah yang ingin dihapus.

![5 menu admin data opsi 4](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/4c75ac5d-c038-49ea-bb21-c55d08939348)


### Sorting
Opsi sorting digunakan untuk mengurutkan sekolah yang terdapat opsi: “Nomor Induk Sekolah”, “Akreditasi”, “ID Sekolah” dan “Kembali”.

## Opsi Nomor Induk Sekolah akan menampilkan pilihan “Ascending” atau “Descending”
Opsi “Ascending” digunakan untuk mengurutkan dari terkecil hingga terbesar.

![6 menu admin data opsi 5 pil 1](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/06958f1c-849d-4ba5-a140-d381e66b96a5)

Opsi “Descending” digunakan untuk mengurutkan dari terbesar hingga terkecil.

![7 menu admin data opsi 5 pil 2](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/f674cf8c-3976-4d0d-a874-b4c14dea3762)


## Opsi Akreditasi akan menampilkan pilihan “Ascending” atau “Descending”
Opsi “Ascending” digunakan untuk mengurutkan dari A-Z.

![7 menu admin data opsi 5 pil 2](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/74f0e758-96ae-43ef-8d0b-3465f02c51ef)

Opsi “Descending” digunakan untuk mengurutkan dari Z-A.

<img width="618" alt="Screenshot 2024-05-01 221117" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/c2a3b241-4d18-43a0-976a-b0c4af5500f8">

OpsI ID Sekolah akan menampilkan pilihan “Ascending” atau “Descending”

![8 menu admin data opsi 5 pil 3](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/f2c710c6-12a1-4744-a57b-0bc3f70b6c9d)

Opsi “Ascending” digunakan untuk mengurutkan dari terkecil hingga terbesar.
Opsi “Descending” digunakan untuk mengurutkan dari terbesar hingga terkecil.

Opsi Kembali gunakan untuk kembali menuju Menu Admin Sekolah.
 
### Searching
Opsi Searching digunakan untuk mencari sekolah yang terdapat opsi: “Nomor Induk Sekolah”, “Akreditasi”, “ID Sekolah”, “Nama Sekolah”, dan “Kembali”.
Apabila memilih opsi 1, Nomor Induk Sekolah akan diarahkan untuk memasukkan Nomor Induk Sekolah yang ingin dicari.

![9 menu admin data opsi 6 pil 1](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/bc6d8591-99e2-4845-8301-5c3741e44f5e)

Apabila memilih opsi 2, Akreditasi akan diarahkan untuk memasukkan Akreditasi yang ingin dicari.

![10 menu admin data opsi 6 pil 2](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/93205a6f-1222-447d-b12c-7f7698d9eb12)

Apabila memilih opsi 3, ID Sekolah akan diarahkan untuk memasukkan ID Sekolah yang ingin dicari.

![11 menu admin data opsi 6 pil 3](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/c9e61576-81e3-451d-b458-9190a5093411)

Apabila memilih opsi 4, Nama Sekolah akan diarahkan untuk memasukkan Nama Sekolah yang ingin dicari.

![12 menu admin data opsi 6 pil 4](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/1f13565d-2ef3-4d69-b911-d831fc01f4d6)

Opsi Kembali gunakan untuk kembali menuju Menu Admin Sekolah.

### Keluar 
Opsi Keluar digunakan untuk keluar menuju Menu Login Admin.

### Admin Sekolah

Apabila memilih pilihan 2, Admin Sekolah akan mendapatkan pertanyaan “Sudah punya akun?” dengan pilihan jawaban “y” atau “t“.

Apabila memasukkan “y”, akan diarahkan untuk mengisi ID Admin Sekolah, Username, dan Password. 

![13 menu sekolah ngga punya akun ngga mau buat akun](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/d5541cad-acff-42b7-89ea-97c968618d0a)

### Menu Admin Sekolah

Apabila telah sukses login sebagai Admin Sekolah, akan terdapat Menu Admin Data yang terdiri dari: “Lihat Data Sekolah”, “Lihat Data Admin Sekolah”, “Perbarui Data Admin Anda”, “Perbarui Data Sekolah Anda”, dan “Keluar”.

<img width="351" alt="Screenshot 2024-05-01 220010" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/5dda516f-c897-4c75-8762-763d7bf0a2af">

### Lihat Data Sekolah
Opsi Lihat Data Sekolah digunakan untuk menampilkan Data Sekolah yang terdiri dari: “ID Sekolah”, “Nama Sekolah”, “Nomor Induk Sekolah”, dan “Akreditasi”.

![15 admin sekolah opsi 1](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/b7889d12-5d30-44dc-beef-eecea00f70d4)

### Lihat Data Admin Sekolah
Opsi Lihat Data Admin Sekolah digunakan untuk melihat Data Admin Sekolah yang sedang login.

![16 admin sekolah opsi 2](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/d5922023-7170-4df9-8ee2-9158a05e31dd)

### Perbarui Data Admin Sekolah Anda

Opsi Perbarui Data Admin Sekolah digunakan jika ingin memperbarui data Admin sekolah yang sedang login yang terdiri dari: ID Admin Sekolah, ID Sekolah, Nama Lengkap, Username, dan Password. Dan akan diarahkan untuk memasukkan data yang ingin diubah.

![17 admin sekolah opsi 3](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/198c93a4-821f-4a18-976a-65bd2a87c5ce)


### Perbaru Data Sekolah Anda

Opsi Perbarui Data Sekolah digunakan jika ingin memperbarui data sekolah admin yang sedang login yang terdiri dari: ID Sekolah, Nama Sekolah, Nomor Induk Sekolah, dan Akreditasi. Dan akan diarahkan untuk memasukkan data yang ingin diubah.

![18 admin sekolah opsi 4](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/f051cb2c-d255-4edb-9982-7d7b2a1932e0)


### Kembali
Opsi Kembali digunakan untuk kembali ke Menu Login Admin

Apabila memasukkan “t” akan terdapat pertanyaan “Apakah ingin buat akun?” dengan opsi jawaban “y” atau “t”.

Apabila memasukkan “y”, akan diarahkan untuk membuat Akun Admin Sekolah dengan mengisi ID Sekolah, Nama Lengkap, Username, dan Password. Pastikan sekolah telah didata.

Apabila memasukkan “t”, akan langsung kembali pada Menu Awal.

![19 menu admin sekolah ngga punya akun mau buat akun](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/f4b92161-43c0-45d3-b6cf-a67f73df65d4)

### Menu Admin Laporan
Apabila memilih pilihan 3, Admin Laporan akan diarahkan untuk memasukkan ID Admin Laporan dan Password. 

![21 login admin laporan](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/0154ca50-f89d-434f-8a55-bb7f7e1c9506)

Apabila telah sukses login sebagai Admin Laporan, akan terdapat Menu Admin Laporan yang terdiri dari: “Lihat Laporan”, “Update Status Laporan”, dan “Kembali”.

### Lihat Laporan
Opsi Lihat Laporan digunakan untuk melihat data daftar laporan yang terdiri dari: “ID Laporan”, “Nama Sekolah”, “Tanggal Dibuat”, “Status”, dan “Isi Laporan”.

<img width="363" alt="Screenshot 2024-05-01 214833" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/dac60b3a-47ab-479c-9cc4-283d01e39e5d">

### Update Status Laporan
Opsi Update Status Laporan digunakan untuk mengganti status laporan menjadi “Diproses” atau “Selesai”.

![22 admin laporan opsi 1](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/d1e00b80-675a-433d-a7b4-8dfd7f81787c)

![23 admin laporan opsi 2](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/67976049-8c45-454f-9f11-33ada190c5a3)

### Kembali
Opsi Kembali digunakan untuk kembali menuju Menu Login Admin.

### Menu User
Dengan memilih opsi “User”, pengguna akan diarahkan ke beberapa menu regular bagi user.

<img width="341" alt="Screenshot 2024-05-01 192828" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/bc78a60a-24fe-4247-9f83-a02535fa3909">

### Lihat Data Sekolah 

Opsi Lihat Data Sekolah program akan menampilkan daftar sekolah yang di dalam nya berisi menu Sorting, Searching, Lihat Data Sekolah dan Kembali ke menu User.

<img width="243" alt="Screenshot 2024-05-01 192856" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/989c1ec1-95fe-4d8b-a7e9-2f42017c53b6">

Jika memilih opsi sorting akan diberikan opsi sorting berdasarkan Nomor Induk Sekolah, Akreditasi. dan bisa melakukan sorting berdasarkan Ascending dan Descanding. 

<img width="329" alt="Screenshot 2024-05-01 193007" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/5990212a-5b51-4d11-b7ae-68b1c192838c">

### Sorting Sekolah

Apabila memilih Sorting Sekolah berdasarkan Nomor Induk Sekolah (Ascending)

<img width="656" alt="Screenshot 2024-05-01 193145" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/af1d7c00-59c0-4323-8920-fe2f0cb92a0a">

Apabila memilih Sorting Sekolah berdasarkan Nomor Induk Sekolah (Descending)

<img width="649" alt="Screenshot 2024-05-01 193252" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/b6f49265-2fba-47aa-98e8-7fc584392aa1">

Opsi Sorting Sekolah berdasarkan Akreditasi Sekolah (Ascending)

<img width="330" alt="Screenshot 2024-05-01 193412" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/e43aae4a-9ea3-4b8d-93bc-eddbf9ffbca5">


<img width="627" alt="Screenshot 2024-05-01 193526" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/998a194c-46de-42aa-8598-5efcf712bffe">

Opsi Sorting Sekolah berdasarkan Akreditasi Sekolah (Descending)

<img width="330" alt="Screenshot 2024-05-01 194402" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/89040324-b0c6-430c-8c85-a7c9145c67e8">


<img width="623" alt="Screenshot 2024-05-01 194348" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/ab1dbbfd-0a20-4bca-af2b-b3ab2384f81c">

### Searching Sekolah 

Apabila memilih opsi Searching berdasarkan Nomor Induk Sekolah, Nama Sekolah, dan opsi kembali. 

<img width="396" alt="Screenshot 2024-05-01 193954" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/9ac035cf-7844-411f-ae23-84977831c366">

Apabila Searching Sekolah Berdasarkan Nomor Induk Sekolah, akan diminta input Nomor Induk Sekolah dengan Output ID Sekolah, Nama Sekolah, Nomor Induk Sekolah, dan Akreditas 

<img width="422" alt="Screenshot 2024-05-01 194613" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/d93b16a9-a0bc-416e-90cc-79cdf78424e2">

Apabila Searching Sekolah Berdasarkan Nama Sekolah, akan diminta input Nama Sekolah dengan Output ID Sekolah, Nama Sekolah, Nomor Induk Sekolah, dan Akreditas 

<img width="415" alt="Screenshot 2024-05-01 194849" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/d4219b4e-a766-4de6-930d-be95dafbf6d5">

### Lihat Data Sekolah 

Menu Lihat Data Sekolah, akan menampilkan data data sekolah seperti ID Sekolah, Nama Sekolah, Nomor Induk Sekolah, dan Akreditasi Sekolah. 

<img width="245" alt="Screenshot 2024-05-01 195032" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/5cace6b6-deff-4c21-9f9f-477410c41306">

<img width="555" alt="Screenshot 2024-05-01 195057" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/43576f15-bb28-4856-a207-7471accb3036">

### Login Akun User (y)

Selanjutnya ketika memilih opsi Login Akun User akan ditanya "Ingin Login? (y/t)" jika memilih "y" akan diminta untuk input Email,dan Password.

<img width="319" alt="Screenshot 2024-05-01 195445" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/868f6ea6-9de5-45c1-a9d9-ca823f40231a">

<img width="324" alt="Screenshot 2024-05-01 195542" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/61e09121-a1f8-4849-a48a-8d6d7ff2bbd2">

Setelah berhasil login, maka akan masuk ke menu User yaitu, LIhat Data Sekolah, Berikan Rating dan Ulasan, Lporkan Sekolah, dan Kembali. 
Jika memilih Lihat Data Sekolah maka akan seperti menu sebelumnya yang menampilkan data data sekolah.

<img width="322" alt="Screenshot 2024-05-01 195919" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/d1dc83cb-8d63-494e-b4b0-3bf95e4f7b1c">

### Rating dan Ulasan
Opsi berikan rating dan ulasan, akan diminta input, ID Sekolah, masukkan rating (1-5), dan masukkan ulasan.

<img width="727" alt="Screenshot 2024-05-01 201704" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/b4829934-50f7-4c2a-bd01-cf5d2d226856">

### Laporkan Sekolah
Opsi Laporkan Sekolah , akan diminta masukkan ID Sekolah yang akan dilaporkan, masukkan isi laporan.


### Menu Login User (t)

Apabila pada menu Login Akun User memilih "t" akan diberikan opsi "Apa ingin  buat akun? (y/t)" jika "y" maka akan diminta input Email, Username, Nama Lengkap, dan Password.

<img width="332" alt="Screenshot 2024-05-01 200521" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/9149242e-a2f1-4688-922b-0b50761f20db">

<img width="320" alt="Screenshot 2024-05-01 200607" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/2e96dc2f-567a-4e84-9396-0e40d111411a">

Lalu setelah berhasil membuat akun user, akan masuk ke menu seperti menu akun user yang sudah memiliki akun sebelumnya. 

<img width="217" alt="Screenshot 2024-05-01 200615" src="https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/3fc0d877-76ee-4b40-ab20-1c526fda5c27">

### Program Selesai. 










