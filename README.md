# Dokumentasi Proyek Akhir Algoritma dan Struktur Data #
## Implementasi Algoritma dan Struktur Data pada Platform Sistem Informasi Pendidikan dan Pencarian Sekolah Pendidikan Sistem Informasi di Samarinda ##
### Anggota Kelompok ###
### •	Nyoman Arini Trirahayu -2309116002 ###
### •	Hana Anastasya Wardah -2309116012 ###
### •	Widia Saputri -2309116019 ###
### •	Farhan Imanudin -2309116028 ###

# Daftar Isi #

- [Deskripsi Program](#deskripsi-program)
- [Implementasi Modul](#implementasi-modul)
- [Instalasi Modul](#instalasi-modul)
- [Struktur Program](#struktur-program)
- [ERD Database](#erd-database)
  - [ERDISH](#erdish)
  - [Entitas](#entitas)
  - [Relasi](#relasi)
  - [Kardinalitas](#kardinalitas)
- [Cara Penggunaan](#cara-penggunaan)
  - [Opsi Awal](#opsi-awal)
  - [Tampilan User](#tampilan-user)
  - [Tampilan Admin](#tampilan-admin)
- [Penjelasan Program](#penjelasan-program)
  - [Model](#model)
  - [View](#view)
  - [Controller](#controller)


# Deskripsi Program # 
PENSI didesain untuk mengakomodasi kebutuhan berbagai pemangku kepentingan (stakeholders) dalam konteks sistem informasi sekolah di Samarinda. PENSI dirancang untuk mengatasi tantangan tersebut dengan menyediakan solusi yang efisien dan terpadu dalam mendapatkan informasi tentang sekolah-sekolah di Samarinda. Melalui fitur-fitur seperti pencarian sekolah, pengurutan, ulasan, dan pelaporan kekurangan, PENSI diharapkan dapat membantu masyarakat Samarinda dalam memperoleh informasi yang lengkap dan akurat tentang sekolah, sementara pihak sekolah dapat memanfaatkan umpan balik untuk terus meningkatkan kualitas pendidikan yang mereka tawarkan

# Implementasi Modul #

Adapun Modul yang digunakan dalam Project ini adalah :

- **OS** : yaitu modul bawaan yang menyediakan akses ke fungsionalitads sistem operasi.
  
- **mysql.connector** : yaitu modul yang menyediakan antarmuka untuk berinteraksi dengan database MySQL. Dengan menggunakan modul ini, Anda dapat terhubung ke database MySQL, mengeksekusi perintah SQL, dan melakukan operasi lain seperti menyisipkan, memperbarui, atau menghapus data.

- **PrettyTable** : yaitu modul yang digunakan untuk memanipulasi visual data yang akan ditampilkan dalam view.

- **math** : Modul ini menyediakan fungsi matematika yang diperlukan untuk melakukan operasi matematika lanjutan. Anda dapat menggunakan modul ini untuk menghitung akar kuadrat, logaritma, trigonometri, dan operasi matematika lainnya.

- **DateTime** : yaitu modul yang digunakan untuk mengambil data tanggal dan waktu.


# Instalasi Modul #

* `pip install mysql-connector-python`

* `pip install prettytable`
  
* `pip install pwinput`
  
* `pip install math`
  
* `pip install python-Date-Time`
  

# Struktur Program #
Konsep yang digunakan adalah MVC (Model, View, Controller). MVC adalah arsitektur pengelolaan program menjadi tiga bagian yaitu Model, View, Controller.
Berikut adalah penjelasan singkat tentang struktur program yang mengikuti konsep MVC (Model, View, Controller):

**Model:** Bagian ini bertanggung jawab untuk mengelola data dari aplikasi. Ini adalah bagian yang mengatur logika bisnis dan operasi database. Model berinteraksi dengan database, mengambil atau menyimpan data, serta melakukan validasi dan manipulasi data. Ini memisahkan bagian logika aplikasi dari tampilan dan kontrolnya.

**View:** Bagian ini bertanggung jawab untuk menampilkan informasi kepada pengguna dan mengatur tampilan antarmuka pengguna. Tampilan mengambil data dari model dan menampilkan informasi yang sesuai kepada pengguna dalam format yang tepat. Ini dapat berupa halaman web, bagian dari antarmuka pengguna, atau bahkan tampilan teks sederhana.

**Controller:** Bagian ini bertindak sebagai perantara antara model dan view. Ini menerima input dari pengguna, memprosesnya menggunakan logika aplikasi yang sesuai, dan kemudian memperbarui model atau tampilan sesuai dengan hasilnya. Kontroler bertanggung jawab untuk mengatur alur kerja aplikasi, mengelola permintaan pengguna, dan membuat keputusan berdasarkan input yang diterima.

# ERD DATABASE #

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

# FLOWCHART #
![PA ASD 1-Halaman-1 revisi drawio](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/31e571a3-0709-40e2-984f-2713e24bd649)
![PA ASD 1-Halaman-2 drawio](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/92db1c5e-2759-4d6b-aefd-8e80801e3afe)
![PA ASD 1-Halaman-3 drawio](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/e7f079d4-8cfe-4dc5-96c8-7f137c94af9b)
![PA ASD 1-Halaman-4 drawio](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/b4be86d3-8fef-4ef2-adc8-3a166becd895)
![PA ASD 1-Halaman-5 drawio](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/81893a97-205d-4606-9eae-b5f398d34239)
![PA ASD 1-Halaman-6 drawio](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/50b68735-c9e9-46bc-b814-5bd843dc79ae)
![PA ASD 1-Halaman-7 drawio](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/6691eb17-71fd-4502-bb14-1efdb54e5a8f)

# Cara Penggunaan # 
### Opsi Awal ###

