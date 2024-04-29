# Dokumentasi Proyek Akhir Algoritma dan Struktur Data #
## Implementasi Algoritma dan Struktur Data pada Platform Sistem Informasi Pendidikan dan Pencarian Sekolah Pendidikan Sistem Informasi di Samarinda ##
### Anggota Kelompok ###
### •	Nyoman Arini Tri -2309116002 ###
### •	Hana Anastasya Wardah -2309116012 ###
### •	Widia Saputri -2309116019 ###
### •	Farhan Imanudin -2309116028 ###

# Daftar Isi #

- [Deskripsi Program](#deskripsi-program)
- [Implementasi Modul](#implementasi-modul)
- [Instalasi Modul](#instalasi-modul)
- [Struktur Program](#struktur-program)
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

- **PyMongo** : yaitu modul yang menghubungkan antara python dengan Mongodb yang merupakan Database berbasis Hosting/Server Online.

- **OS** : yaitu modul bawaan yang menyediakan akses ke fungsionalitads sistem operasi.

- **Time** : fungsi yang digunakan ialah sleep() yang berfungsi untuk menghentikan program untuk sementara dalam waktu tertentu, diatur dalam satuan detik.

- **PrettyTable** : yaitu modul yang digunakan untuk memanipulasi visual data yang akan ditampilkan dalam view.

- **SibApiV3Sdk** : yaitu modul yang digunakan untuk mengambil data dari API yang telah disediakan oleh Sendisblue.

- **Pwinput** : yaitu modul yang digunakan untuk mengambil inputan password tanpa menampilkan password yang diinputkan.

- **Dotenv** : yaitu modul yang digunakan untuk menghubungkan antara program dengan file .env yang berisi key - value dari MongoClient.

- **Random** : yaitu modul yang digunakan untuk mengambil data secara random.

- **DateTime** : yaitu modul yang digunakan untuk mengambil data tanggal dan waktu.


# Instalasi Modul #

# Struktur Program #
Konsep yang digunakan adalah MVC (Model, View, Controller). MVC adalah arsitektur pengelolaan program menjadi tiga bagian yaitu Model, View, Controller.
Berikut adalah penjelasan singkat tentang struktur program yang mengikuti konsep MVC (Model, View, Controller):

**Model:** Bagian ini bertanggung jawab untuk mengelola data dari aplikasi. Ini adalah bagian yang mengatur logika bisnis dan operasi database. Model berinteraksi dengan database, mengambil atau menyimpan data, serta melakukan validasi dan manipulasi data. Ini memisahkan bagian logika aplikasi dari tampilan dan kontrolnya.

**View:** Bagian ini bertanggung jawab untuk menampilkan informasi kepada pengguna dan mengatur tampilan antarmuka pengguna. Tampilan mengambil data dari model dan menampilkan informasi yang sesuai kepada pengguna dalam format yang tepat. Ini dapat berupa halaman web, bagian dari antarmuka pengguna, atau bahkan tampilan teks sederhana.

**Controller:** Bagian ini bertindak sebagai perantara antara model dan view. Ini menerima input dari pengguna, memprosesnya menggunakan logika aplikasi yang sesuai, dan kemudian memperbarui model atau tampilan sesuai dengan hasilnya. Kontroler bertanggung jawab untuk mengatur alur kerja aplikasi, mengelola permintaan pengguna, dan membuat keputusan berdasarkan input yang diterima.

# ERD DATABASE #

![PA SEM 2 fixx drawio](https://github.com/PA-A23-KELOMPOK-8/PA-A23-KELOMPOK-8/assets/144756754/75caccd2-ac42-47c8-9b9f-d0f2d829e5e8)

# Cara Penggunaan # 

