-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 24, 2024 at 08:11 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pendidikan`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_data`
--

CREATE TABLE `admin_data` (
  `ID_Admin_Data` int(11) NOT NULL,
  `Nama_Lengkap` varchar(35) NOT NULL,
  `Jenjang` varchar(3) NOT NULL,
  `Username` varchar(35) NOT NULL,
  `Password` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_data`
--

INSERT INTO `admin_data` (`ID_Admin_Data`, `Nama_Lengkap`, `Jenjang`, `Username`, `Password`) VALUES
(1, 'Admin Data SD', 'SD', 'datasd', 1111),
(2, 'Admin Data SMP', 'SMP', 'datasmp', 2222),
(3, 'Admin Data SMA', 'SMA', 'datasma', 3333),
(4, 'Admin Data SMK', 'SMK', 'datasmk', 4444);

-- --------------------------------------------------------

--
-- Table structure for table `admin_laporan`
--

CREATE TABLE `admin_laporan` (
  `ID_Admin_Laporan` int(11) NOT NULL,
  `Nama_Lengkap` varchar(35) NOT NULL,
  `Jenjang` varchar(3) NOT NULL,
  `Username` varchar(35) NOT NULL,
  `Password` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_laporan`
--

INSERT INTO `admin_laporan` (`ID_Admin_Laporan`, `Nama_Lengkap`, `Jenjang`, `Username`, `Password`) VALUES
(1, 'Admin Laporan SD', 'SD', 'laporansd', 1111),
(2, 'Admin Laporan SMP', 'SMP', 'laporansmp', 2222),
(3, 'Admin Laporan SMA', 'SMA', 'laporansma', 3333),
(4, 'Admin Laporan SMK', 'SMK', 'laporansmk', 4444);

-- --------------------------------------------------------

--
-- Table structure for table `admin_sekolah`
--

CREATE TABLE `admin_sekolah` (
  `ID_Admin_Sekolah` int(11) NOT NULL,
  `ID_Sekolah` int(11) DEFAULT NULL,
  `Nama_Lengkap` varchar(35) NOT NULL,
  `Username` varchar(35) NOT NULL,
  `Password` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_sekolah`
--

INSERT INTO `admin_sekolah` (`ID_Admin_Sekolah`, `ID_Sekolah`, `Nama_Lengkap`, `Username`, `Password`) VALUES
(1, 1, 'Admin SD 1', 'adminsd1', 1111),
(2, 2, 'Admin SD 2', 'adminsd2', 2222),
(3, 3, 'Admin SD 3', 'adminsd3', 3333),
(4, 4, 'Admin SD 4', 'adminsd4', 4444),
(5, 5, 'Admin SD 5', 'adminsd5', 5555),
(6, 6, 'Admin SD 6', 'adminsd6', 6666),
(7, 7, 'Admin SD 7', 'adminsd7', 7777),
(8, 8, 'Admin SD 8', 'adminsd8', 8888),
(9, 9, 'Admin SD 9', 'adminsd9', 9999),
(10, 10, 'Admin SD 10', 'adminsd10', 1010),
(11, 11, 'Admin SMP 1', 'adminsmp1', 1112),
(12, 12, 'Admin SMP 2', 'adminsmp2', 1222),
(13, 13, 'Admin SMP 3', 'adminsmp3', 1333),
(14, 14, 'Admin SMP 4', 'adminsmp4', 1444),
(15, 15, 'Admin SMP 5', 'adminsmp5', 1555),
(16, 16, 'Admin SMP 6', 'adminsmp6', 1666),
(17, 17, 'Admin SMP 7', 'adminsmp7', 1777),
(18, 18, 'Admin SMP 8', 'adminsmp8', 1888),
(19, 19, 'Admin SMP 9', 'adminsmp9', 1999),
(20, 20, 'Admin SMP 10', 'adminsmp10', 2000),
(21, 21, 'Admin SMA 1', 'adminsma1', 2111),
(22, 22, 'Admin SMA 2', 'adminsma2', 2223),
(23, 23, 'Admin SMA 3', 'adminsma3', 2333),
(24, 24, 'Admin SMA 4', 'adminsma4', 2444),
(25, 25, 'Admin SMA 5', 'adminsma5', 2555),
(26, 26, 'Admin SMA 6', 'adminsma6', 2666),
(27, 27, 'Admin SMA 7', 'adminsma7', 2777),
(28, 28, 'Admin SMA 8', 'adminsma8', 2888),
(29, 29, 'Admin SMA 9', 'adminsma9', 2999),
(30, 30, 'Admin SMA 10', 'adminsma10', 3000),
(31, 31, 'Admin SMK 1', 'adminsmk1', 3111),
(32, 32, 'Admin SMK 2', 'adminsmk2', 3222),
(33, 33, 'Admin SMK 3', 'adminsmk3', 3334),
(34, 34, 'Admin SMK 4', 'adminsmk4', 3444),
(35, 35, 'Admin SMK 5', 'adminsmk5', 3555),
(36, 36, 'Admin SMK 6', 'adminsmk6', 3666),
(37, 37, 'Admin SMK 7', 'adminsmk7', 3777),
(38, 38, 'Admin SMK 8', 'adminsmk8', 3888),
(39, 39, 'Admin SMK 9', 'adminsmk9', 3999),
(40, 40, 'Admin SMK 10', 'adminsmk10', 4000);

-- --------------------------------------------------------

--
-- Table structure for table `akun_user`
--

CREATE TABLE `akun_user` (
  `ID_Akun_User` int(11) NOT NULL,
  `ID_Sekolah` int(11) DEFAULT NULL,
  `Nama_Lengkap` varchar(35) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Username` varchar(35) NOT NULL,
  `Password` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `akun_user`
--

INSERT INTO `akun_user` (`ID_Akun_User`, `ID_Sekolah`, `Nama_Lengkap`, `Email`, `Username`, `Password`) VALUES
(1, 1, 'Ali Budiarto', 'ali.budiarto@sekolah1.com', 'alibudi', 1234),
(2, 2, 'Budi Cahyadi', 'budi.cahyadi@sekolah2.com', 'budicah', 2345),
(3, 3, 'Citra Dewi', 'citra.dewi@sekolah3.com', 'citradew', 3456),
(4, 4, 'Dewi Astuti', 'dewi.astuti@sekolah4.com', 'dewiast', 4567),
(5, 5, 'Eko Suharjo', 'eko.suharjo@sekolah5.com', 'ekosuha', 5678),
(6, 6, 'Fahri Irawan', 'fahri.irawan@sekolah6.com', 'fahriir', 6789),
(7, 7, 'Gina Mahendra', 'gina.mahendra@sekolah7.com', 'ginamah', 7890),
(8, 8, 'Hani Putri', 'hani.putri@sekolah8.com', 'haniput', 8901),
(9, 9, 'Indah Puspita', 'indah.puspita@sekolah9.com', 'indahpu', 9012),
(10, 10, 'Joko Waluyo', 'joko.waluyo@sekolah10.com', 'jokowal', 1023),
(11, 11, 'Kartika Sari', 'kartika.sari@sekolah11.com', 'kartiks', 1123),
(12, 12, 'Lukman Hakim', 'lukman.hakim@sekolah12.com', 'lukmanh', 1224),
(13, 13, 'Mira Kusuma', 'mira.kusuma@sekolah13.com', 'mirakus', 1325),
(14, 14, 'Nina Rosita', 'nina.rosita@sekolah14.com', 'ninaros', 1426),
(15, 15, 'Omar Said', 'omar.said@sekolah15.com', 'omarsai', 1527),
(16, 16, 'Putri Anjani', 'putri.anjani@sekolah16.com', 'putrian', 1628),
(17, 17, 'Rizki Hamdani', 'rizki.hamdani@sekolah17.com', 'rizkiha', 1729),
(18, 18, 'Sari Wijaya', 'sari.wijaya@sekolah18.com', 'sariwij', 1830),
(19, 19, 'Tio Baskoro', 'tio.baskoro@sekolah19.com', 'tiobask', 1931),
(20, 20, 'Umar Abdullah', 'umar.abdullah@sekolah20.com', 'umarabd', 2032),
(21, 21, 'Vina Mariana', 'vina.mariana@sekolah21.com', 'vinamar', 2132),
(22, 22, 'Wahyu Setiawan', 'wahyu.setiawan@sekolah22.com', 'wahyuset', 2243),
(23, 23, 'Xena Valentia', 'xena.valentia@sekolah23.com', 'xenaval', 2354),
(24, 24, 'Yudi Raharjo', 'yudi.raharjo@sekolah24.com', 'yudirah', 2465),
(25, 25, 'Zahra Nabila', 'zahra.nabila@sekolah25.com', 'zahranab', 2576),
(26, 26, 'Amanda Putri', 'amanda.putri@sekolah26.com', 'amandapu', 2687),
(27, 27, 'Bayu Kurniawan', 'bayu.kurniawan@sekolah27.com', 'bayukur', 2798),
(28, 28, 'Cindy Lestari', 'cindy.lestari@sekolah28.com', 'cindyles', 2809),
(29, 29, 'Denny Wijaya', 'denny.wijaya@sekolah29.com', 'dennywi', 2910),
(30, 30, 'Elisa Kurniawati', 'elisa.kurniawati@sekolah30.com', 'elisakur', 3021),
(31, 31, 'Fajar Nugraha', 'fajar.nugraha@sekolah31.com', 'fajarnug', 3132),
(32, 32, 'Gita Safitri', 'gita.safitri@sekolah32.com', 'gitasaf', 3243),
(33, 33, 'Hendra Surya', 'hendra.surya@sekolah33.com', 'hendrasu', 3354),
(34, 34, 'Intan Permatasari', 'intan.permatasari@sekolah34.com', 'intanper', 3465),
(35, 35, 'Jaya Pratama', 'jaya.pratama@sekolah35.com', 'jayapra', 3576),
(36, 36, 'Kevin Ardianto', 'kevin.ardianto@sekolah36.com', 'kevinard', 3687),
(37, 37, 'Lia Anggraini', 'lia.anggraini@sekolah37.com', 'liaangg', 3798),
(38, 38, 'Maulana Ikhsan', 'maulana.ikhsan@sekolah38.com', 'maulanai', 3809),
(39, 39, 'Nadia Zaskia', 'nadia.zaskia@sekolah39.com', 'nadiazas', 3910),
(40, 40, 'Oki Setiawan', 'oki.setiawan@sekolah40.com', 'okiset', 4021);

-- --------------------------------------------------------

--
-- Table structure for table `laporan`
--

CREATE TABLE `laporan` (
  `ID_Laporan` int(11) NOT NULL,
  `ID_Admin_Laporan` int(11) DEFAULT NULL,
  `ID_Akun_User` int(11) DEFAULT NULL,
  `Nama_Sekolah` varchar(50) NOT NULL,
  `Tanggal_Dibuat` datetime NOT NULL,
  `Status` varchar(25) NOT NULL DEFAULT 'Menunggu',
  `Isi_Laporan` varchar(355) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `laporan`
--

INSERT INTO `laporan` (`ID_Laporan`, `ID_Admin_Laporan`, `ID_Akun_User`, `Nama_Sekolah`, `Tanggal_Dibuat`, `Status`, `Isi_Laporan`) VALUES
(1, 1, 1, 'SD NEGERI 001 Samarinda Ulu', '2024-04-07 00:00:00', 'Menunggu', 'Laporan pengeluaran bulan Januari'),
(2, 1, 2, 'SD Negeri 002 Samarinda Utara', '2024-04-08 00:00:00', 'Diproses', 'Laporan acara olahraga tahunan'),
(3, 1, 3, 'SD Negeri 003 Sungai Kunjang', '2024-04-09 00:00:00', 'Selesai', 'Laporan penilaian akhir semester'),
(4, 1, 4, 'SD Negeri 004 Palaran', '2024-04-16 00:00:00', 'Menunggu', 'Laporan pembelian buku perpustakaan'),
(5, 1, 5, 'SD Negeri 005 Sungai Kunjang', '2024-04-17 00:00:00', 'Diproses', 'Laporan kegiatan baca buku'),
(6, 1, 6, 'SD Negeri 006 Sungai Pinang', '2024-04-18 00:00:00', 'Selesai', 'Laporan donasi seragam sekolah'),
(7, 1, 7, 'SD Negeri 007 Samarinda Kota', '2024-04-25 00:00:00', 'Menunggu', 'Laporan kegiatan hari kartini'),
(8, 1, 8, 'SD Negeri 008 Loa Janan Ilir', '2024-04-26 00:00:00', 'Diproses', 'Laporan pengembangan laboratorium IPA'),
(9, 1, 9, 'SD Negeri 009 Sambutan', '2024-04-27 00:00:00', 'Selesai', 'Laporan penanaman pohon lingkungan sekolah'),
(10, 1, 10, 'SD Negeri 010 Samarinda Seberang', '2024-04-28 00:00:00', 'Menunggu', 'Laporan program bimbingan konseling'),
(11, 2, 11, 'SMP Negeri 1 Samarinda', '2024-04-10 00:00:00', 'Menunggu', 'Laporan kegiatan ekstrakurikuler'),
(12, 2, 12, 'SMP Negeri 2 Samarinda', '2024-04-11 00:00:00', 'Diproses', 'Laporan pembangunan fasilitas baru'),
(13, 2, 13, 'SMP Negeri 3 Samarinda', '2024-04-19 00:00:00', 'Menunggu', 'Laporan pertukaran pelajar'),
(14, 2, 14, 'SMP Negeri 4 Samarinda', '2024-04-20 00:00:00', 'Diproses', 'Laporan kejuaraan olahraga'),
(15, 2, 15, 'SMP Negeri 5 Samarinda', '2024-04-29 00:00:00', 'Diproses', 'Laporan proyek ilmiah remaja'),
(16, 2, 16, 'SMP Negeri 6 Samarinda', '2024-04-30 00:00:00', 'Selesai', 'Laporan kegiatan sosial kemasyarakatan'),
(17, 2, 17, 'SMP Negeri 7 Samarinda', '2024-05-05 00:00:00', 'Menunggu', 'Laporan kegiatan bulan bahasa'),
(18, 2, 18, 'SMP Negeri 8 Samarinda', '2024-05-06 00:00:00', 'Diproses', 'Laporan turnamen sepak bola antar kelas'),
(19, 2, 19, 'SMP Negeri 9 Samarinda', '2024-05-07 00:00:00', 'Selesai', 'Laporan workshop jurnalistik sekolah'),
(20, 2, 20, 'SMP Negeri 10 Samarinda', '2024-05-08 00:00:00', 'Menunggu', 'Laporan pameran sains dan teknologi'),
(21, 3, 21, 'SMA Negeri 1 Samarinda', '2024-04-12 00:00:00', 'Selesai', 'Laporan kunjungan industri'),
(22, 3, 22, 'SMA Negeri 2 Samarinda', '2024-04-13 00:00:00', 'Menunggu', 'Laporan kegiatan pramuka'),
(23, 3, 23, 'SMA Negeri 3 Samarinda', '2024-04-21 00:00:00', 'Selesai', 'Laporan seminar karir'),
(24, 3, 24, 'SMA Negeri 4 Samarinda', '2024-04-22 00:00:00', 'Menunggu', 'Laporan workshop seni'),
(25, 3, 25, 'SMA Negeri 5 Samarinda', '2024-05-01 00:00:00', 'Menunggu', 'Laporan kunjungan museum sejarah'),
(26, 3, 26, 'SMA Negeri 6 Samarinda', '2024-05-02 00:00:00', 'Diproses', 'Laporan proyek kewirausahaan siswa'),
(27, 3, 27, 'SMA Negeri 7 Samarinda', '2024-05-09 00:00:00', 'Diproses', 'Laporan kegiatan studi lapangan geografi'),
(28, 3, 28, 'SMA Negeri 8 Samarinda', '2024-05-10 00:00:00', 'Selesai', 'Laporan festival band sekolah'),
(29, 3, 29, 'SMA Negeri 9 Samarinda', '2024-05-11 00:00:00', 'Menunggu', 'Laporan program pertukaran pelajar internasional'),
(30, 3, 30, 'SMA Negeri 10 Samarinda', '2024-05-12 00:00:00', 'Diproses', 'Laporan kegiatan persiapan ujian nasional'),
(31, 4, 31, 'SMK Negeri 1 Samarinda', '2024-04-14 00:00:00', 'Diproses', 'Laporan praktik kerja lapangan'),
(32, 4, 32, 'SMK Negeri 2 Samarinda', '2024-04-15 00:00:00', 'Selesai', 'Laporan hasil ujian kompetensi keahlian'),
(33, 4, 33, 'SMK Negeri 3 Samarinda', '2024-04-23 00:00:00', 'Diproses', 'Laporan pameran karya siswa'),
(34, 4, 34, 'SMK Negeri 4 Samarinda', '2024-04-24 00:00:00', 'Selesai', 'Laporan hasil lomba desain grafis'),
(35, 4, 35, 'SMK Negeri 5 Samarinda', '2024-05-03 00:00:00', 'Selesai', 'Laporan praktik industri kerjasama dengan perusahaan'),
(36, 4, 36, 'SMK Negeri 6 Samarinda', '2024-05-04 00:00:00', 'Menunggu', 'Laporan kegiatan unit produksi sekolah'),
(37, 4, 37, 'SMK Negeri 7 Samarinda', '2024-05-13 00:00:00', 'Selesai', 'Laporan pelatihan keahlian otomotif'),
(38, 4, 38, 'SMK Negeri 8 Samarinda', '2024-05-14 00:00:00', 'Menunggu', 'Laporan kegiatan kewirausahaan siswa'),
(39, 4, 39, 'SMK Negeri 9 Samarinda', '2024-05-15 00:00:00', 'Diproses', 'Laporan proyek pembuatan aplikasi mobile'),
(40, 4, 40, 'SMK Negeri 10 Samarinda', '2024-05-16 00:00:00', 'Selesai', 'Laporan hasil uji kompetensi kejuruan');

-- --------------------------------------------------------

--
-- Table structure for table `rating_dan_ulasan`
--

CREATE TABLE `rating_dan_ulasan` (
  `ID_Rating_dan_Ulasan` int(11) NOT NULL,
  `ID_Sekolah` int(11) DEFAULT NULL,
  `ID_Akun_User` int(11) DEFAULT NULL,
  `Tanggal_Diberikan` datetime NOT NULL,
  `Rating` int(1) NOT NULL,
  `Ulasan` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `rating_dan_ulasan`
--

INSERT INTO `rating_dan_ulasan` (`ID_Rating_dan_Ulasan`, `ID_Sekolah`, `ID_Akun_User`, `Tanggal_Diberikan`, `Rating`, `Ulasan`) VALUES
(1, 1, 1, '2024-04-07 10:00:00', 5, 'Sekolah sangat bagus dan guru-gurunya kompeten.'),
(2, 2, 2, '2024-04-07 11:00:00', 4, 'Fasilitas lengkap, tapi kegiatan ekstrakurikuler kurang.'),
(3, 3, 3, '2024-04-07 12:00:00', 3, 'Lingkungan sekolah nyaman, namun perlu peningkatan pada kualitas pengajaran.'),
(4, 4, 4, '2024-04-07 13:00:00', 5, 'Sekolah dengan akademik yang sangat baik.'),
(5, 5, 5, '2024-04-07 14:00:00', 4, 'Sekolah bagus, namun akses ke lokasi agak sulit.'),
(6, 6, 1, '2024-04-08 10:00:00', 5, 'Pengalaman belajar yang menyenangkan dengan banyak kegiatan.'),
(7, 7, 2, '2024-04-08 11:00:00', 4, 'Kurikulumnya up to date, namun kantin perlu diperbaiki.'),
(8, 8, 3, '2024-04-08 12:00:00', 2, 'Kelas terlalu padat, perlu ditambah ruang kelas baru.'),
(9, 9, 4, '2024-04-08 13:00:00', 5, 'Guru-gurunya sangat membantu dan peduli.'),
(10, 10, 5, '2024-04-08 14:00:00', 4, 'Sarana olahraga lengkap, tapi perlu penambahan buku di perpustakaan.'),
(11, 11, 6, '2024-04-09 10:00:00', 3, 'Program bimbingan konseling membantu, tapi fasilitas olahraga kurang.'),
(12, 12, 7, '2024-04-09 11:00:00', 4, 'Sekolahnya bersih dan teratur, tapi perlu lebih banyak ekstrakurikuler.'),
(13, 13, 8, '2024-04-09 12:00:00', 5, 'Metode pengajaran guru sangat efektif dan inovatif.'),
(14, 14, 9, '2024-04-09 13:00:00', 2, 'Perlu penambahan laboratorium sains dan komputer.'),
(15, 15, 10, '2024-04-09 14:00:00', 4, 'Keamanan sekolah bagus, namun akses transportasi umum kurang.'),
(16, 16, 6, '2024-04-10 10:00:00', 5, 'Sekolah hebat dengan banyak kegiatan positif untuk siswa.'),
(17, 17, 7, '2024-04-10 11:00:00', 3, 'Perpustakaannya luas, namun koleksi bukunya belum lengkap.'),
(18, 18, 8, '2024-04-10 12:00:00', 4, 'Guru-guru sangat mendukung pengembangan minat dan bakat siswa.'),
(19, 19, 9, '2024-04-10 13:00:00', 1, 'Sering terjadi banjir ketika hujan, drainase perlu diperbaiki.'),
(20, 20, 10, '2024-04-10 14:00:00', 4, 'Siswa mendapat banyak peluang untuk lomba dan kompetisi.'),
(21, 21, 11, '2024-04-11 10:00:00', 5, 'Sekolah memberikan banyak fasilitas untuk mendukung belajar.'),
(22, 22, 12, '2024-04-11 11:00:00', 4, 'Lingkungan sekolah sangat kondusif untuk pembelajaran.'),
(23, 23, 13, '2024-04-12 10:00:00', 3, 'Fasilitas memadai tapi kurang varietas ekstrakurikuler.'),
(24, 24, 14, '2024-04-12 11:00:00', 5, 'Sangat puas dengan kualitas guru dan materi pengajaran.'),
(25, 25, 15, '2024-04-12 12:00:00', 4, 'Lokasi strategis dan mudah dijangkau.'),
(26, 26, 16, '2024-04-12 13:00:00', 2, 'Kelas terlalu padat, perlu perhatian lebih dari manajemen.'),
(27, 27, 17, '2024-04-12 14:00:00', 5, 'Program akademik sangat baik, mendukung pengembangan siswa.'),
(28, 28, 18, '2024-04-13 10:00:00', 4, 'Aktivitas luar kelas banyak dan bermanfaat.'),
(29, 29, 19, '2024-04-13 11:00:00', 3, 'Sarana prasarana cukup lengkap, tapi beberapa sudah tua.'),
(30, 30, 20, '2024-04-13 12:00:00', 4, 'Kantin bersih, makanan sehat dan variatif.'),
(31, 31, 21, '2024-04-13 13:00:00', 5, 'Pembelajaran inovatif dan kreatif, sangat menyenangkan.'),
(32, 32, 22, '2024-04-13 14:00:00', 4, 'Guru sangat peduli dan membantu semua siswa.'),
(33, 33, 23, '2024-04-14 10:00:00', 3, 'Perlu peningkatan fasilitas olahraga.'),
(34, 34, 24, '2024-04-14 11:00:00', 2, 'Administrasi sering lambat dalam menanggapi pertanyaan atau masalah.'),
(35, 35, 25, '2024-04-14 12:00:00', 4, 'Lingkungan sekolah sangat mendukung untuk belajar.'),
(36, 36, 26, '2024-04-14 13:00:00', 5, 'Sekolah menawarkan banyak program ekstrakurikuler dan klub.'),
(37, 37, 27, '2024-04-14 14:00:00', 3, 'Butuh lebih banyak ruang hijau dan area bermain.'),
(38, 38, 28, '2024-04-15 10:00:00', 4, 'Sekolah memiliki banyak laboratorium yang dilengkapi dengan baik.'),
(39, 39, 29, '2024-04-15 11:00:00', 2, 'Perlu lebih banyak buku referensi di perpustakaan.'),
(40, 40, 30, '2024-04-15 12:00:00', 5, 'Pendekatan pengajaran yang baik, siswa diajak aktif.');

-- --------------------------------------------------------

--
-- Table structure for table `sekolah`
--

CREATE TABLE `sekolah` (
  `ID_Sekolah` int(11) NOT NULL,
  `ID_Admin_Data` int(11) DEFAULT NULL,
  `Nama_Sekolah` varchar(50) NOT NULL,
  `Nomor_Induk_Sekolah` int(8) NOT NULL,
  `Akreditas` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sekolah`
--

INSERT INTO `sekolah` (`ID_Sekolah`, `ID_Admin_Data`, `Nama_Sekolah`, `Nomor_Induk_Sekolah`, `Akreditas`) VALUES
(1, 1, 'SD NEGERI 001 Samarinda Ulu', 30401096, 'A'),
(2, 1, 'SD Negeri 002 Samarinda Utara', 30401351, 'B'),
(3, 1, 'SD Negeri 003 Sungai Kunjang', 30401143, 'A'),
(4, 1, 'SD Negeri 004 Palaran', 30401093, 'A'),
(5, 1, 'SD Negeri 005 Sungai Kunjang', 30401132, 'B'),
(6, 1, 'SD Negeri 006 Sungai Pinang', 30401369, 'C'),
(7, 1, 'SD Negeri 007 Samarinda Kota', 30401139, 'B'),
(8, 1, 'SD Negeri 008 Loa Janan Ilir', 30400986, 'A'),
(9, 1, 'SD Negeri 009 Sambutan', 30400958, 'B'),
(10, 1, 'SD Negeri 010 Samarinda Seberang', 30401188, 'B'),
(11, 2, 'SMP Negeri 1 Samarinda', 30401025, 'A'),
(12, 2, 'SMP Negeri 2 Samarinda', 30403007, 'A'),
(13, 2, 'SMP Negeri 3 Samarinda', 30401046, 'A'),
(14, 2, 'SMP Negeri 4 Samarinda', 30401032, 'A'),
(15, 2, 'SMP Negeri 5 Samarinda', 30401033, 'A'),
(16, 2, 'SMP Negeri 6 Samarinda', 30401034, 'A'),
(17, 2, 'SMP Negeri 7 Samarinda', 30401035, 'A'),
(18, 2, 'SMP Negeri 8 Samarinda', 30401036, 'A'),
(19, 2, 'SMP Negeri 9 Samarinda', 30401048, 'A'),
(20, 2, 'SMP Negeri 10 Samarinda', 30401026, 'A'),
(21, 3, 'SMA Negeri 1 Samarinda', 30401066, 'A'),
(22, 3, 'SMA Negeri 2 Samarinda', 30401059, 'A'),
(23, 3, 'SMA Negeri 3 Samarinda', 30401058, 'A'),
(24, 3, 'SMA Negeri 4 Samarinda', 30401050, 'A'),
(25, 3, 'SMA Negeri 5 Samarinda', 30401051, 'A'),
(26, 3, 'SMA Negeri 6 Samarinda', 30401052, 'A'),
(27, 3, 'SMA Negeri 7 Samarinda', 30401053, 'A'),
(28, 3, 'SMA Negeri 8 Samarinda', 30401054, 'A'),
(29, 3, 'SMA Negeri 9 Samarinda', 30401055, 'A'),
(30, 3, 'SMA Negeri 10 Samarinda', 30401067, 'A'),
(31, 4, 'SMK Negeri 1 Samarinda', 30401089, 'A'),
(32, 4, 'SMK Negeri 2 Samarinda', 30401081, 'A'),
(33, 4, 'SMK Negeri 3 Samarinda', 30401080, 'A'),
(34, 4, 'SMK Negeri 4 Samarinda', 30401079, 'A'),
(35, 4, 'SMK Negeri 5 Samarinda', 30401071, 'B'),
(36, 4, 'SMK Negeri 6 Samarinda', 30401072, 'A'),
(37, 4, 'SMK Negeri 7 Samarinda', 30403017, 'A'),
(38, 4, 'SMK Negeri 8 Samarinda', 30404238, 'B'),
(39, 4, 'SMK Negeri 9 Samarinda', 30404605, 'B'),
(40, 4, 'SMK Negeri 10 Samarinda', 30404272, 'B');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_data`
--
ALTER TABLE `admin_data`
  ADD PRIMARY KEY (`ID_Admin_Data`);

--
-- Indexes for table `admin_laporan`
--
ALTER TABLE `admin_laporan`
  ADD PRIMARY KEY (`ID_Admin_Laporan`);

--
-- Indexes for table `admin_sekolah`
--
ALTER TABLE `admin_sekolah`
  ADD PRIMARY KEY (`ID_Admin_Sekolah`),
  ADD KEY `fk_admin_sekolah` (`ID_Sekolah`);

--
-- Indexes for table `akun_user`
--
ALTER TABLE `akun_user`
  ADD PRIMARY KEY (`ID_Akun_User`),
  ADD KEY `fk_akun_user` (`ID_Sekolah`);

--
-- Indexes for table `laporan`
--
ALTER TABLE `laporan`
  ADD PRIMARY KEY (`ID_Laporan`),
  ADD KEY `fk_laporan_user` (`ID_Akun_User`),
  ADD KEY `fk_admin_laporan` (`ID_Admin_Laporan`);

--
-- Indexes for table `rating_dan_ulasan`
--
ALTER TABLE `rating_dan_ulasan`
  ADD PRIMARY KEY (`ID_Rating_dan_Ulasan`),
  ADD KEY `fk_rating_sekolah` (`ID_Sekolah`),
  ADD KEY `fk_rating_user` (`ID_Akun_User`);

--
-- Indexes for table `sekolah`
--
ALTER TABLE `sekolah`
  ADD PRIMARY KEY (`ID_Sekolah`),
  ADD KEY `fk_admin_Data` (`ID_Admin_Data`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_data`
--
ALTER TABLE `admin_data`
  MODIFY `ID_Admin_Data` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `admin_laporan`
--
ALTER TABLE `admin_laporan`
  MODIFY `ID_Admin_Laporan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `admin_sekolah`
--
ALTER TABLE `admin_sekolah`
  MODIFY `ID_Admin_Sekolah` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `akun_user`
--
ALTER TABLE `akun_user`
  MODIFY `ID_Akun_User` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `laporan`
--
ALTER TABLE `laporan`
  MODIFY `ID_Laporan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `rating_dan_ulasan`
--
ALTER TABLE `rating_dan_ulasan`
  MODIFY `ID_Rating_dan_Ulasan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `sekolah`
--
ALTER TABLE `sekolah`
  MODIFY `ID_Sekolah` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin_sekolah`
--
ALTER TABLE `admin_sekolah`
  ADD CONSTRAINT `fk_admin_sekolah` FOREIGN KEY (`ID_Sekolah`) REFERENCES `sekolah` (`ID_Sekolah`) ON DELETE SET NULL ON UPDATE SET NULL;

--
-- Constraints for table `akun_user`
--
ALTER TABLE `akun_user`
  ADD CONSTRAINT `fk_akun_user` FOREIGN KEY (`ID_Sekolah`) REFERENCES `sekolah` (`ID_Sekolah`) ON DELETE SET NULL ON UPDATE SET NULL;

--
-- Constraints for table `laporan`
--
ALTER TABLE `laporan`
  ADD CONSTRAINT `fk_admin_laporan` FOREIGN KEY (`ID_Admin_Laporan`) REFERENCES `admin_laporan` (`ID_Admin_Laporan`) ON DELETE SET NULL ON UPDATE SET NULL,
  ADD CONSTRAINT `fk_laporan_user` FOREIGN KEY (`ID_Akun_User`) REFERENCES `akun_user` (`ID_Akun_User`) ON DELETE SET NULL ON UPDATE SET NULL;

--
-- Constraints for table `rating_dan_ulasan`
--
ALTER TABLE `rating_dan_ulasan`
  ADD CONSTRAINT `fk_rating_sekolah` FOREIGN KEY (`ID_Sekolah`) REFERENCES `sekolah` (`ID_Sekolah`) ON DELETE SET NULL ON UPDATE SET NULL,
  ADD CONSTRAINT `fk_rating_user` FOREIGN KEY (`ID_Akun_User`) REFERENCES `akun_user` (`ID_Akun_User`) ON DELETE SET NULL ON UPDATE SET NULL;

--
-- Constraints for table `sekolah`
--
ALTER TABLE `sekolah`
  ADD CONSTRAINT `fk_admin_Data` FOREIGN KEY (`ID_Admin_Data`) REFERENCES `admin_data` (`ID_Admin_Data`) ON DELETE SET NULL ON UPDATE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
