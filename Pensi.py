# Modul
import os
import mysql.connector
from prettytable import PrettyTable
import math
import datetime
import re


# Database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pendidikan"
)
cursor = mydb.cursor()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def connect_to_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pendidikan"
    )



# Linked List untuk menyimpan admin yang sedang login
class LoggedInAdmins:
    def __init__(self):
        self.head = None

    # Menambahkan admin yang sedang login ke dalam linked list
    def add_admin(self, admin_id, admin_type):
        new_node = AdminNode(admin_id, admin_type)
        new_node.next = self.head
        self.head = new_node

    # Menghapus admin yang sedang login dari linked list
    def remove_admin(self, admin_id):
        current = self.head
        previous = None
        while current:
            if current.data[0] == admin_id:  # Cek apakah ID admin pada node saat ini sama dengan admin yang akan dihapus
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

# Node untuk menyimpan informasi admin yang sedang login
class AdminNode:
    def __init__(self, data, admin_type):
        self.data = (data, admin_type)
        self.next = None








# Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def clear(self):
        self.head = None
    
        
    def quickSort(self, data):
        if len(data) <= 1:
            return data
        else:
            pivot = data[0]

            less_than_pivot = [x for x in data[1:] if x <= pivot]
            greater_than_pivot = [x for x in data[1:] if x > pivot]

            return self.quickSort(less_than_pivot) + [pivot] + self.quickSort(greater_than_pivot)

    def jumpSearchNIS(self, nis):
        current = self.head
        daftarNIS = []
        
        while current:
            daftarNIS.append(current.data["Nomor_Induk_Sekolah"])
            current = current.next
        
        daftarNIS = self.quickSort(daftarNIS)
        
        n = len(daftarNIS)
        step = int(math.sqrt(n))
        prev = 0
        
        # Konversi nis ke integer
        nis = int(nis)
        
        while prev < n and daftarNIS[min(step, n) - 1] < nis:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return None

        while daftarNIS[prev] < nis:
            prev += 1
            if prev == min(step, n):
                return None
        
        if daftarNIS[prev] == nis:
            current = self.head
            while current:
                if current.data["Nomor_Induk_Sekolah"] == nis:
                    return current
                current = current.next
        else:
            return False


                        
    def jumpSearchAkreditasi(self, akreditasi):
        current = self.head
        daftarAkre = []
        
        while current:
            daftarAkre.append(current.data["Akreditas"])
            current = current.next
        
        daftarAkre = self.quickSort(daftarAkre)
        
        n = len(daftarAkre)
        step = int(math.sqrt(n))
        prev = 0
        
        while prev < n and daftarAkre[min(step, n) - 1] < akreditasi:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return None

        while daftarAkre[prev] < akreditasi:
            prev += 1
            if prev == min(step, n):
                return None
        
        if daftarAkre[prev] == akreditasi:
            current = self.head
            while current:
                if current.data["Akreditas"] == akreditasi:
                    return current
                current = current.next
        else:
            return False

    def jumpSearchID(self, id_sekolah):
        current = self.head
        daftarID = []
        
        while current:
            daftarID.append(current.data["ID_Sekolah"])
            current = current.next
        
        daftarID = self.quickSort(daftarID)
        
        n = len(daftarID)
        step = int(math.sqrt(n))
        prev = 0
        
        # Konversi id_sekolah ke integer
        id_sekolah = int(id_sekolah)
        
        while prev < n and daftarID[min(step, n) - 1] < id_sekolah:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return None

        while daftarID[prev] < id_sekolah:
            prev += 1
            if prev == min(step, n):
                return None
        
        if daftarID[prev] == id_sekolah:
            current = self.head
            while current:
                if current.data["ID_Sekolah"] == id_sekolah:
                    return current
                current = current.next
        else:
            return False

    def jumpSearchNamaSekolah(self, nama_sekolah):
            current = self.head
            daftarNamaSekolah = []
            
            while current:
                daftarNamaSekolah.append(current.data["Nama_Sekolah"])
                current = current.next
            
            daftarNamaSekolah = self.quickSort(daftarNamaSekolah)
            
            n = len(daftarNamaSekolah)
            step = int(math.sqrt(n))
            prev = 0
            
            while prev < n and daftarNamaSekolah[min(step, n) - 1] < nama_sekolah:
                prev = step
                step += int(math.sqrt(n))
                if prev >= n:
                    return None

            while daftarNamaSekolah[prev] < nama_sekolah:
                prev += 1
                if prev == min(step, n):
                    return None
            
            if daftarNamaSekolah[prev] == nama_sekolah:
                current = self.head
                while current:
                    if current.data["Nama_Sekolah"] == nama_sekolah:
                        return current
                    current = current.next
            else:
                return False





logged_in_admins = LoggedInAdmins()
sekolahLinkedList = LinkedList()


def ambilDataSekolah():
    try:
        sekolahLinkedList.clear()
        query = "SELECT * FROM sekolah"
        cursor.execute(query)
        hasil = cursor.fetchall()
        for kolom in hasil:
            dataSekolah = {
                "ID_Sekolah":kolom[0],
                "ID_Admin_Data":kolom[1],
                "Nama_Sekolah":kolom[2],
                "Nomor_Induk_Sekolah":kolom[3],
                "Akreditas":kolom[4]
            }
            sekolahLinkedList.insert(dataSekolah)
    except mysql.connector.Error as err:
        print("=======================")
        print(f"Error MySQL: {err.msg}")
        print("=======================")
        input("Tekan enter untuk melanjutkan...")
        

def ambilDataSekolahSimpan(sekolahLinkedList):
    try:
        # Membuat koneksi ke database
        connection = connect_to_mysql()
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            
            # Mengambil data sekolah dari tabel sekolah
            cursor.execute("SELECT * FROM sekolah")
            data_sekolah = cursor.fetchall()

            # Memasukkan data sekolah ke dalam sekolahLinkedList
            for sekolah in data_sekolah:
                sekolahLinkedList.insert(sekolah)

            # Menutup kursor dan koneksi
            cursor.close()
            connection.close()
            print("==============================")
            print("|Data sekolah berhasil dimuat|")
            print("==============================")
    except mysql.connector.Error as error:
        print("Error:", error)







# Fungsi untuk login admin
def loginAdmin(admin_type):
    clear()
    print("================================================")
    print("===               LOGIN ADMIN                ===")
    print("================================================")
    try:
        if admin_type == "admin_data":
            id = input("ID Admin Data: ")
            password = input("Password: ")
            # Query ke database untuk memeriksa keberadaan admin data dengan ID dan password yang sesuai
            query = "SELECT * FROM admin_data WHERE ID_Admin_Data = %s AND Password = %s"
            cursor.execute(query, (id, password))
        elif admin_type == "admin_sekolah":
            id = input("ID Admin Sekolah: ")
            username = input("Username: ")
            password = input("Password: ")
            # Query ke database untuk memeriksa keberadaan admin sekolah dengan ID, username, dan password yang sesuai
            query = "SELECT * FROM admin_sekolah WHERE ID_Admin_Sekolah = %s AND Username = %s AND Password = %s"
            cursor.execute(query, (id, username, password))
        elif admin_type == "admin_laporan":
            id = input("ID Admin Laporan: ")
            password = input("Password: ")
            # Query ke database untuk memeriksa keberadaan admin laporan dengan ID dan password yang sesuai
            query = "SELECT * FROM admin_laporan WHERE ID_Admin_Laporan = %s AND Password = %s"
            cursor.execute(query, (id, password))
        else:
            print("Jenis admin tidak valid.")
            return

        result = cursor.fetchone()
        if result:
            print("=======================")
            print("|    Login berhasil!  |")
            print("=======================")
            input("Tekan Enter untuk  lanjut")
            logged_in_admins.add_admin(result[0], admin_type)  # Menyimpan informasi admin yang sedang login
            clear()
            if admin_type == "admin_data":
                menuAdminData()  # Memanggil menu admin data jika login berhasil
            elif admin_type == "admin_sekolah":
                menuAdminSekolah(id)  # Memanggil menu admin sekolah jika login berhasil
            elif admin_type == "admin_laporan":
                menuAdminLaporan()  # Memanggil menu admin laporan jika login berhasil
        else:
            print("ID atau password salah.")
    except ValueError as ve:
        print("Terjadi kesalahan:", ve)
    except KeyboardInterrupt:
        print("Login dibatalkan.")
    except Exception as e:
        print("Terjadi kesalahan saat login:", e)


# Fungsi untuk menampilkan menu pilihan admin
def menuLoginAdmin():
    while True:
        try:
            print("======================================================================================")
            print("|                               Pilih Menu Login Admin                               |")
            print("======================================================================================")
            print("|                                  1. Admin Data                                     |")
            print("|                                  2. Admin Sekolah                                  |")
            print("|                                  3. Admin Laporan                                  |")
            print("|                                  0. Keluar                                         |")
            print("======================================================================================")
            print("\n")
            pilihan = int(input("Masukkan Pilihan: "))
            if pilihan == 1:
                loginAdmin("admin_data")
            elif pilihan == 2:
                login_admin_sekolah = input("Sudah punya akun? (y/t) :")
                if login_admin_sekolah == "y":
                    loginAdmin("admin_sekolah")
                elif login_admin_sekolah == "t":
                    buat_akun_admin_sekolah = input("Apakah ingin buat akun? (y/t):")
                    if buat_akun_admin_sekolah == "y":
                        buatAkunAdminSekolah()
                    elif buat_akun_admin_sekolah == "t":
                        main()
                    else:
                        print("========================================")
                        print("|Pilihan tidak valid. Silakan coba lagi|")
                        print("========================================")
                        print("\n")
                else:
                    print("========================================")
                    print("|Pilihan tidak valid. Silakan coba lagi|")
                    print("========================================")
                    print("\n")
            elif pilihan == 3:
                loginAdmin("admin_laporan")
            elif pilihan == 0:
                break
            else:
                print("========================================")
                print("|Pilihan tidak valid. Silakan coba lagi|")
                print("========================================")
                print("\n")
        except ValueError:
            print("==========================================")
            print("|Masukkan angka yang valid.              |")
            print("==========================================")
            input("Tekan enter untuk lanjut")
        except KeyboardInterrupt:
            print("================================================")
            print("|Program berhenti karena Anda menekan Ctrl+C. |")
            print("================================================")
            input("Tekan enter untuk lanjut")
        except Exception as e:
            if str(e) == "'^Z'":
                print("=============================================")
                print("|Program berhenti karena Anda menekan Ctrl+Z|")
                print("=============================================")
            else:
                print("=================================================")
                print("|Terjadi kesalahan:", e)
                print("=================================================")
            input("Tekan enter untuk lanjut")






def buatAkunAdminSekolah():
    while True:
        try:
            clear()
            print("===============================================================")
            print("=============== Buat Akun Baru Admin Sekolah ==================")
            print("===============================================================")
            print("\n")
            
            # Meminta input ID Sekolah, Nama Lengkap, Username, dan Password dari pengguna
            id_sekolah = int(input("ID Sekolah: "))
            nama_lengkap = input("Nama Lengkap: ")
            username = input("Username: ")
            password = int(input("Password: "))  # Ubah menjadi int sesuai dengan tipe data kolom Password

            # Periksa keberadaan ID Sekolah dalam tabel sekolah
            cursor.execute("SELECT * FROM sekolah WHERE ID_Sekolah = %s", (id_sekolah,))
            result = cursor.fetchone()
            if result:
                # ID Sekolah ditemukan, lanjutkan proses penyisipan data admin sekolah
                query = "INSERT INTO admin_sekolah (ID_Sekolah, Nama_Lengkap, Username, Password) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (id_sekolah, nama_lengkap, username, password))
                mydb.commit()
                print("===================================")
                print("Akun Admin Sekolah berhasil dibuat!")
                print("===================================")
                print("\n")
                input("Tekan Enter untuk kembali ke menu...")
                main()
            else:
                # ID Sekolah tidak ditemukan, tampilkan pesan kesalahan
                print("===============================================================")
                print("ID Sekolah tidak valid. Silakan masukkan ID Sekolah yang valid.")
                print("===============================================================")
                input("Tekan Enter untuk kembali ke menu...")
                main()
        except ValueError:
            print("==========================================")
            print("|Masukkan angka yang valid.              |")
            print("==========================================")
            input("Tekan enter untuk lanjut")
        except KeyboardInterrupt:
            print("================================================")
            print("|Program berhenti karena Anda menekan Ctrl+C. |")
            print("================================================")
            input("Tekan enter untuk lanjut")
        except Exception as e:
            if str(e) == "'^Z'":
                print("=============================================")
                print("|Program berhenti karena Anda menekan Ctrl+Z|")
                print("=============================================")
            else:
                print("=================================================")
                print("|Terjadi kesalahan:", e)
                print("=================================================")
            input("Tekan enter untuk lanjut")







# Fungsi untuk menampilkan menu admin data
def menuAdminData():
    while True:
        try:
            print("===============================================================")
            print("|                       MENU ADMIN DATA                       |")
            print("===============================================================")
            print("|                  1. Tambah Data Sekolah                     |")
            print("|                  2. Lihat Data Sekolah                      |")
            print("|                  3. Perbarui Data Sekolah                   |")
            print("|                  4. Hapus Data Sekolah                      |")
            print("|                  5. Sorting                                 |")
            print("|                  6. Searching                               |")
            print("|                  0. Keluar                                  |")
            print("===============================================================")
            print("\n")
            pilihan = int(input("Masukkan Pilihan: "))
            if pilihan == 1:
                tambahDataSekolah()
            elif pilihan == 2:
                AdminlihatDataSekolah()
            elif pilihan == 3:
                perbaruiDataSekolahSemua()
            elif pilihan == 4:
                hapusDataSekolah()
            elif pilihan == 5:
                AdminsortingDataSekolah()
            elif pilihan == 6:
                AdminsearchingDataSekolah(sekolahLinkedList)

            elif pilihan == 0:
                break
            else:
                print("=======================================")
                print("Pilihan tidak valid. Silakan coba lagi.")
                print("=======================================")
                input("Tekan Enter untuk lanjut...")
        except ValueError:
            print("==========================================")
            print("|Masukkan angka yang valid.              |")
            print("==========================================")
            input("Tekan enter untuk lanjut")
        except KeyboardInterrupt:
            print("================================================")
            print("|Program berhenti karena Anda menekan Ctrl+C. |")
            print("================================================")
            input("Tekan enter untuk lanjut")
        except Exception as e:
            if str(e) == "'^Z'":
                print("=============================================")
                print("|Program berhenti karena Anda menekan Ctrl+Z|")
                print("=============================================")
            else:
                print("=================================================")
                print("|Terjadi kesalahan:", e)
                print("=================================================")
            input("Tekan enter untuk lanjut")
            
            
def tambahDataSekolah():
    while True:
        clear()
        print("=======================================================")
        print("|               Tambah Data Sekolah                   |")
        print("=======================================================")
        print("\n")
        nama_sekolah = input("Masukkan Nama Sekolah: ")
        nomor_induk_sekolah = input("Masukkan Nomor Induk Sekolah: ")
        akreditasi = input("Masukkan Akreditasi Sekolah (A/B/C): ")

        if akreditasi.strip().upper() not in ['A', 'B', 'C']:
            print("Akreditasi hanya bisa 'A', 'B', atau 'C'. Silakan coba lagi.")
            continue

        query = "INSERT INTO sekolah (Nama_Sekolah, Nomor_Induk_Sekolah, Akreditas) VALUES (%s, %s, %s)"
        cursor.execute(query, (nama_sekolah, nomor_induk_sekolah, akreditasi))
        mydb.commit()
        print("==================================")
        print("Data sekolah berhasil ditambahkan.")
        print("===================================")
 


def AdminlihatDataSekolah():
    clear()
    print("Data Sekolah:")
    query = "SELECT ID_Sekolah, ID_Admin_Data, Nama_Sekolah, Nomor_Induk_Sekolah, Akreditas FROM sekolah"
    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        # Membuat linked list untuk menyimpan data sekolah
        sekolah_list = LinkedList()

        # Menambahkan data sekolah ke dalam linked list
        for row in result:
            sekolah_list.insert(row)

        # Menampilkan data sekolah menggunakan PrettyTable dengan urutan terbalik
        table = PrettyTable(["ID Sekolah", "ID Admin Data", "Nama Sekolah", "Nomor Induk Sekolah", "Akreditasi"])
        current = sekolah_list.head

        # Menambahkan setiap baris data ke tabel dalam urutan terbalik
        rows = []
        while current:
            rows.append(current.data)
            current = current.next

        # Menambahkan baris data dari belakang ke depan ke dalam tabel
        for row in reversed(rows):
            table.add_row(row)

        print(table)
        input("Tekan Enter untuk lanjut...")
    else:
        print("=============================")
        print("Data sekolah tidak ditemukan.")
        print("=============================")



def perbaruiDataSekolahSemua():
    while True:
        clear()
        print("==============================================================")
        print("|                  Perbarui Data Sekolah                     |")
        print("==============================================================")
        print("\n")
        id_sekolah = input("Masukkan ID Sekolah yang ingin diperbarui (0 untuk batal): ")
        
        if id_sekolah == '0':
            break

        # Periksa apakah ID Sekolah valid
        query = "SELECT * FROM sekolah WHERE ID_Sekolah = %s"
        cursor.execute(query, (id_sekolah,))
        result = cursor.fetchone()

        if result:
            # ID Sekolah valid, tampilkan data saat ini
            print("==============================================================")
            print("Data Sekolah saat ini:")
            print("ID Sekolah:", result[0])
            print("Nama Sekolah:", result[2])
            print("Nomor Induk Sekolah:", result[3])
            print("Akreditasi:", result[4])
            print("==============================================================")

            # Meminta pengguna untuk memasukkan data baru
            nama_sekolah_baru = input("Masukkan Nama Sekolah baru (biarkan kosong untuk mempertahankan nilai saat ini): ")
            nomor_induk_sekolah_baru = input("Masukkan Nomor Induk Sekolah baru (biarkan kosong untuk mempertahankan nilai saat ini): ")
            akreditasi_baru = input("Masukkan Akreditasi Sekolah baru (biarkan kosong untuk mempertahankan nilai saat ini): ")

            if akreditasi_baru.strip().upper() not in ['A', 'B', 'C']:
                print("Akreditasi hanya bisa 'A', 'B', atau 'C'.")
                continue

            if nama_sekolah_baru.strip():
                nama_sekolah = nama_sekolah_baru
            else:
                nama_sekolah = result[2]

            if nomor_induk_sekolah_baru.strip():
                nomor_induk_sekolah = nomor_induk_sekolah_baru
            else:
                nomor_induk_sekolah = result[3]

            if akreditasi_baru.strip():
                akreditasi = akreditasi_baru
            else:
                akreditasi = result[4]

            # Lakukan update data jika ada perubahan
            if (nama_sekolah != result[2]) or (nomor_induk_sekolah != result[3]) or (akreditasi != result[4]):
                query = "UPDATE sekolah SET Nama_Sekolah = %s, Nomor_Induk_Sekolah = %s, Akreditas = %s WHERE ID_Sekolah = %s"
                cursor.execute(query, (nama_sekolah, nomor_induk_sekolah, akreditasi, id_sekolah))
                mydb.commit()
                print("=================================")
                print("Data Sekolah berhasil diperbarui!")
                print("=================================")
                print("\n")
                input("Tekan Enter untuk lanjut...")
                break
            else:
                print("===============================================================")
                print("Tidak ada perubahan yang dilakukan. Tidak ada data yang diperbarui.")
                print("===============================================================")
                input("Tekan Enter untuk lanjut...")
                break
        else:
            print("==========================================")
            print("ID Sekolah tidak valid. Silakan coba lagi.")
            print("==========================================")
            input("Tekan Enter untuk lanjut...")
            continue



def hapusDataSekolah():
    id_sekolah = input("Masukkan ID Sekolah yang akan dihapus: ")
    query = "DELETE FROM sekolah WHERE ID_Sekolah = %s"
    cursor.execute(query, (id_sekolah,))
    mydb.commit()
    print("===============================")
    print("Data sekolah berhasil dihapus.")
    print("===============================")
    print("\n")
    input("Tekan Enter untuk lanjut...")

def AdminsortingDataSekolah():
    while True:
        clear()
        print("================================================")
        print("|                     SORTING                  |")
        print("================================================")
        print("|            1. Nomor Induk Sekolah            |")
        print("|            2. Akreditasi                     |")
        print("|            3. ID Sekolah                     |")
        print("|            0. Kembali                        |")
        print("================================================")
        print("\n")
        sort_choice = int(input("Masukkan Pilihan: "))
        
        if sort_choice == 0:
            break
        elif sort_choice in [1, 2, 3]:
            while True:
                print("===================")
                print("|   Pilih Urutan  |")
                print("|1. Ascending     |")
                print("|2. Descending    |")
                print("===================")
                
                order_choice = int(input("Masukkan Pilihan: "))
                
                if order_choice == 1:
                    sort_order = "DESC"
                    break
                elif order_choice == 2:
                    sort_order = "ASC"
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
            
            # Lakukan sorting
            if sort_choice == 1:
                sorted_list = urutkanDataSekolahNIS(sort_order)
            elif sort_choice == 2:
                sorted_list = urutkanDataSekolahAkredetasi(sort_order)
            elif sort_choice == 3:
                sorted_list = urutkanDataSekolahID(sort_order)
        else:
            print("=======================================")
            print("Pilihan tidak valid. Silakan coba lagi.")
            print("=======================================")
            input("Tekan Enter untuk lanjut...")

def urutkanDataSekolahNIS(sort_order):
    clear()
    ambilDataSekolah()
    daftarNIS = []
    current = sekolahLinkedList.head
    while current:
        daftarNIS.append(current.data["Nomor_Induk_Sekolah"])
        current = current.next
    
    if sort_order == "DESC":
        daftarNISterurut = sekolahLinkedList.quickSort(daftarNIS)
    elif sort_order == "ASC":
        daftarNISterurut = sekolahLinkedList.quickSort(daftarNIS)
        daftarNISterurut.reverse() 
    else:
        print("============================")
        print("Arah pengurutan tidak valid.")
        print("============================")
        return
    
    tabel = PrettyTable()
    tabel.field_names = ["ID Sekolah", "ID Admin Data", "Nama Sekolah", "Nomor Induk Sekolah", "Akreditas"]
    
    for NIS in daftarNISterurut:
        node = sekolahLinkedList.jumpSearchNIS(NIS)
        if node:
            data = node.data
            tabel.add_row([data["ID_Sekolah"], data["ID_Admin_Data"], data["Nama_Sekolah"], data["Nomor_Induk_Sekolah"], data["Akreditas"]])
    clear()
    print(tabel)
    input("Tekan enter untuk melanjutkan...")

    
def urutkanDataSekolahAkredetasi(sort_order):
    clear()
    ambilDataSekolah()
    daftarAkre = []
    current = sekolahLinkedList.head
    while current:
        daftarAkre.append(current.data["Akreditas"])
        current = current.next
    
    if sort_order == "ASC":
        daftarAkreterurut = sekolahLinkedList.quickSort(daftarAkre)
    elif sort_order == "DESC":
        daftarAkreterurut = sekolahLinkedList.quickSort(daftarAkre)
        daftarAkreterurut.reverse()
    else:
        print("============================")
        print("Arah pengurutan tidak valid.")
        print("============================")
        return
    
    tabel = PrettyTable()
    tabel.field_names = ["ID Sekolah", "ID Admin Data", "Nama Sekolah", "Nomor Induk Sekolah", "Akreditas"]
    
    for Akre in daftarAkreterurut:
        node = sekolahLinkedList.jumpSearchAkreditasi(Akre)
        if node:
            data = node.data
            tabel.add_row([data["ID_Sekolah"], data["ID_Admin_Data"], data["Nama_Sekolah"], data["Nomor_Induk_Sekolah"], data["Akreditas"]])
    clear()
    print(tabel)
    input("Tekan enter untuk melanjutkan...")
    
def urutkanDataSekolahID(sort_order):
    clear()
    ambilDataSekolah()
    daftarID = []
    current = sekolahLinkedList.head
    while current:
        daftarID.append(current.data["ID_Sekolah"])
        current = current.next
    
    # Periksa arah pengurutan dan sesuaikan metode pemanggilan quickSort()
    if sort_order == "DESC":
        daftarIDterurut = sekolahLinkedList.quickSort(daftarID)
    elif sort_order == "ASC":
        daftarIDterurut = sekolahLinkedList.quickSort(daftarID)
        daftarIDterurut.reverse()
    else:
        print("============================")
        print("Arah pengurutan tidak valid.")
        print("============================")
        return
    
    tabel = PrettyTable()
    tabel.field_names = ["ID Sekolah", "ID Admin Data", "Nama Sekolah", "Nomor Induk Sekolah", "Akreditas"]
    
    for ID in daftarIDterurut:
        node = sekolahLinkedList.jumpSearchID(ID)
        if node:
            data = node.data
            tabel.add_row([data["ID_Sekolah"], data["ID_Admin_Data"], data["Nama_Sekolah"], data["Nomor_Induk_Sekolah"], data["Akreditas"]])
    clear()
    print(tabel)
    input("Tekan enter untuk melanjutkan...")



def AdminsearchingDataSekolah(sekolahLinkedList):
    while True:
        
        clear()
        ambilDataSekolahSimpan(sekolahLinkedList)
        print("===========================================================")
        print("|                       SEARCHING                         |")
        print("===========================================================")
        print("|                1. Nomor Induk Sekolah                   |")
        print("|                2. Akreditasi                            |")
        print("|                3. ID Sekolah                            |")
        print("|                4. Nama Sekolah                          |")
        print("|                0. Kembali                               |")
        print("===========================================================")
        print("\n")
        search_choice = int(input("Masukkan Pilihan: "))

        if search_choice == 0:
            break
        elif search_choice == 1:
            keyword = input("Masukkan nomor induk sekolah yang ingin dicari: ")
            if sekolahLinkedList.head is not None:
                search_result = sekolahLinkedList.jumpSearchNIS(keyword)
                if search_result:
                    print("================================================================")
                    print("Hasil Pencarian:")
                    print("ID Sekolah:", search_result.data["ID_Sekolah"])
                    print("Nama Sekolah:", search_result.data["Nama_Sekolah"])
                    print("Nomor Induk Sekolah:", search_result.data["Nomor_Induk_Sekolah"])
                    print("Akreditasi:", search_result.data["Akreditas"])
                    print("================================================================")
                else:
                    print("====================================")
                    print("Nomor induk sekolah tidak ditemukan.")
                    print("====================================")
            else:
                print("=======================================")
                print("Tidak ada data sekolah yang dimasukkan.")
                print("=======================================")
                
        elif search_choice == 2:
            keyword = input("Masukkan akreditasi yang ingin dicari: ")
            if sekolahLinkedList.head is not None:
                search_result = sekolahLinkedList.jumpSearchAkreditasi(keyword)
                if search_result:
                    print("================================================================")
                    print("Hasil Pencarian:")
                    print("ID Sekolah:", search_result.data["ID_Sekolah"])
                    print("Nama Sekolah:", search_result.data["Nama_Sekolah"])
                    print("Nomor Induk Sekolah:", search_result.data["Nomor_Induk_Sekolah"])
                    print("Akreditasi:", search_result.data["Akreditas"])
                    print("================================================================")
                else:
                    print("==========================")
                    print("Akreditas tidak ditemukan.")
                    print("==========================")
            else:
                print("=======================================")
                print("Tidak ada data sekolah yang dimasukkan.")
                print("=======================================")
        elif search_choice == 3:
            keyword = input("Masukkan ID sekolah yang ingin dicari: ")
            if sekolahLinkedList.head is not None:
                search_result = sekolahLinkedList.jumpSearchID(keyword)
                if search_result:
                    print("Hasil Pencarian:")
                    print("ID Sekolah:", search_result.data["ID_Sekolah"])
                    print("Nama Sekolah:", search_result.data["Nama_Sekolah"])
                    print("Nomor Induk Sekolah:", search_result.data["Nomor_Induk_Sekolah"])
                    print("Akreditasi:", search_result.data["Akreditas"])
                else:
                    print("===========================")
                    print("ID sekolah tidak ditemukan.")
                    print("===========================")
            else:
                print("Tidak ada data sekolah yang dimasukkan.")
        elif search_choice == 4:
            keyword = input("Masukkan nama sekolah yang ingin dicari: ")
            if sekolahLinkedList.head is not None:
                search_result = sekolahLinkedList.jumpSearchNamaSekolah(keyword) 
                if search_result:
                    print("Hasil Pencarian:")
                    print("ID Sekolah:", search_result.data["ID_Sekolah"])
                    print("Nama Sekolah:", search_result.data["Nama_Sekolah"])
                    print("Nomor Induk Sekolah:", search_result.data["Nomor_Induk_Sekolah"])
                    print("Akreditasi:", search_result.data["Akreditas"])
                else:
                    print("Nama sekolah tidak ditemukan.")
            else:
                print("Tidak ada data sekolah yang dimasukkan.")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        input("Tekan Enter untuk kembali...")









# Fungsi untuk menampilkan menu admin sekolah
def menuAdminSekolah(id):
    while True:
        
        print("==================================================")
        print("|              MENU ADMIN SEKOLAH                |")
        print("==================================================")
        print("|            1. Lihat Data Sekolah               |")
        print("|            2. Lihat Data Admin Sekolah         |")
        print("|            3. Perbarui Data Admin Anda         |")
        print("|            4. Perbarui Data Sekolah Anda       |")
        print("|            0. Kembali                          |")                       
        print("==================================================")
        print("\n")
        pilihan = int(input("Masukkan Pilihan: "))
        if pilihan == 1:
            lihatDataSekolah()
        elif pilihan == 2:
            lihatDataAdminSekolah(id)
        elif pilihan == 3:
            perbaruiDataAdminSekolah(id)
        elif pilihan == 4:
            perbaruiDataSekolahSendiri(id)
        elif pilihan == 0:
            break
        else:
            
            print("=======================================")
            print("Pilihan tidak valid. Silakan coba lagi.")
            print("=======================================")
            
def lihatDataSekolah():
    print("Data Sekolah:")
    query = "SELECT ID_Sekolah, Nama_Sekolah, Nomor_Induk_Sekolah, Akreditas FROM sekolah"
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        # Menampilkan data sekolah menggunakan PrettyTable
        table = PrettyTable(["ID Sekolah", "Nama Sekolah", "Nomor Induk Sekolah", "Akreditasi"])
        for row in result:
            table.add_row(row)
        print(table)
    else:
        print("=============================")
        print("Data sekolah tidak ditemukan.")
        print("=============================")
    input("Tekan enter untuk melanjutkan...")
    
def lihatDataAdminSekolah(id):
    query = "SELECT ID_Admin_Sekolah, ID_Sekolah, Nama_Lengkap, Username, Password FROM admin_sekolah WHERE ID_Admin_Sekolah = %s"
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    if result:
        # Menampilkan data admin sekolah
        print("==========================================")
        print("|           Data Admin Sekolah           |")
        print("==========================================")
        print(f"ID Admin Sekolah: {result[0]}")
        print(f"ID Sekolah: {result[1]}")
        print(f"Nama Lengkap: {result[2]}")
        print(f" Username: {result[3]}")
        print(f"Password: {result[4]}")
    else:
        print("===================================")
        print("Data admin sekolah tidak ditemukan.")
        print("===================================")


def perbaruiDataAdminSekolah(id):
    clear()
    current = logged_in_admins.head
    if current:
        admin_id = id
        # Lakukan perbaruan data admin sesuai dengan ID admin yang sedang login
        query = "SELECT * FROM admin_sekolah WHERE ID_Admin_Sekolah = %s"
        cursor.execute(query, (admin_id,))
        result = cursor.fetchone()
        if result:
            print("=========================")
            print("|Data Admin Sekolah Anda|")
            print("=========================")
            print(f"ID Admin Sekolah: {result[0]}")
            print(f"ID Sekolah: {result[1]}")
            print(f"Nama Lengkap: {result[2]}")
            print(f"Username: {result[3]}")
            print(f"Password: {result[4]}")
            print("\n")
            new_username = input("Masukkan Username Baru (kosongkan jika tidak ingin mengubah): ")
            new_fullname = input("Masukkan Nama Lengkap Baru (kosongkan jika tidak ingin mengubah): ")
            new_password = input("Masukkan Password Baru (kosongkan jika tidak ingin mengubah): ")
            if new_username or new_fullname or new_password:
                # Lakukan perbaruan data admin sekolah jika ada input baru
                query = "UPDATE admin_sekolah SET"
                if new_username:
                    query += " Username = %s,"
                if new_fullname:
                    query += " Nama_Lengkap = %s,"
                if new_password:
                    query += " Password = %s,"
                query = query.rstrip(",") + " WHERE ID_Admin_Sekolah = %s"
                data = []
                if new_username:
                    data.append(new_username)
                if new_fullname:
                    data.append(new_fullname)
                if new_password:
                    data.append(new_password)
                data.append(admin_id)
                cursor.execute(query, tuple(data))
                mydb.commit()
                print("=======================================")
                print("Data admin sekolah berhasil diperbarui.")
                print("=======================================")
                input("tekan enter untuk lanjut...")
            else:
                print("===================================")
                print("Tidak ada perubahan yang dilakukan.")
                print("===================================")
                input("tekan enter untuk lanjut...")
        else:
            print("===================================")
            print("Data admin sekolah tidak ditemukan.")
            print("===================================")
            input("tekan enter untuk lanjut...")
    else:
        print("==================================")
        print("Tidak ada admin yang sedang login.")
        print("==================================")
        input("tekan enter untuk lanjut...")

def perbaruiDataSekolahSendiri(id):
    clear()
    current = logged_in_admins.head
    if current:
        admin_id = id
        # Lakukan perbaruan data sekolah sesuai dengan ID admin yang sedang login
        query = "SELECT ID_Sekolah FROM admin_sekolah WHERE ID_Admin_Sekolah = %s"
        cursor.execute(query, (admin_id,))
        result = cursor.fetchone()
        if result:
            school_id = result[0]  # Ambil sekolah dari admin yang sedang login
            query = "SELECT * FROM sekolah WHERE ID_Sekolah = %s"
            cursor.execute(query, (school_id,))
            school_data = cursor.fetchone()
            if school_data:
                print("============================================")
                print("|            Data Sekolah Anda             |")
                print("============================================")
                print(f"ID Sekolah: {school_data[0]}")
                print(f"Nama Sekolah: {school_data[2]}")
                print(f"Nomor Induk Sekolah: {school_data[3]}")
                print(f"Akreditasi: {school_data[4]}")
                print("\n")
                new_school_name = input("Masukkan Nama Sekolah Baru (kosongkan jika tidak ingin mengubah): ")
                new_school_number = input("Masukkan Nomor Induk Sekolah Baru (kosongkan jika tidak ingin mengubah): ")
                new_accreditation = input("Masukkan Akreditasi Baru (A/B/C) (kosongkan jika tidak ingin mengubah): ").upper()

                if new_accreditation and new_accreditation not in ['A', 'B', 'C']:
                    print("Akreditasi hanya bisa 'A', 'B', atau 'C'. Silakan coba lagi.")
                    input("Tekan Enter untuk lanjut...")
                    return

                if new_school_name or new_school_number or new_accreditation:
                    query = "UPDATE sekolah SET"
                    if new_school_name:
                        query += " Nama_Sekolah = %s,"
                    if new_school_number:
                        query += " Nomor_Induk_Sekolah = %s,"
                    if new_accreditation:
                        query += " Akreditas = %s,"
                    query = query.rstrip(",") + " WHERE ID_Sekolah = %s"
                    data = []
                    if new_school_name:
                        data.append(new_school_name)
                    if new_school_number:
                        data.append(new_school_number)
                    if new_accreditation:
                        data.append(new_accreditation)
                    data.append(school_id)
                    cursor.execute(query, tuple(data))
                    mydb.commit()
                    print("=======================================")
                    print("    Data sekolah berhasil diperbarui   ")
                    print("=======================================")
                    input("Tekan Enter untuk lanjut...")
                else:
                    print("===================================")
                    print("Tidak ada perubahan yang dilakukan.")
                    print("===================================")
                    input("Tekan Enter untuk lanjut...")
            else:
                print("===================================")
                print("    Data sekolah tidak ditemukan   ")
                print("===================================")
                input("Tekan Enter untuk lanjut...")
        else:
            print("===================================")
            print("Data admin sekolah tidak ditemukan.")
            print("===================================")
            input("Tekan Enter untuk lanjut...")
    else:
        print("==================================")
        print("Tidak ada admin yang sedang login.")
        print("==================================")
        input("Tekan Enter untuk lanjut...")








# Fungsi untuk menampilkan menu admin laporan
def menuAdminLaporan():
    while True:
        clear()
        print("=========================================")
        print("|            MENU ADMIN LAPORAN         |")
        print("=========================================")
        print("|           1. Lihat Laporan            |")
        print("|           2. Update Status Laporan    |")
        print("|           0. Kembali                  |")
        print("=========================================")
        print("\n")
        pilihan = int(input("Masukkan Pilihan: "))
        if pilihan == 1:
            lihatLaporan()
        elif pilihan == 2:
            updateStatusLaporan()
        elif pilihan == 0:
            break
        else:
            print("=======================================")
            print("Pilihan tidak valid. Silakan coba lagi.")
            print("=======================================")
            input("tekan enter untuk lanjut...")
            

def lihatLaporan():
    clear()
    print("Daftar Laporan:\n")
    # Query ke database untuk mengambil data laporan
    query = "SELECT ID_Laporan, Nama_Sekolah, Tanggal_Dibuat, Status, Isi_Laporan FROM laporan"
    cursor.execute(query)
    result = cursor.fetchall()
    
    if result:
        # Menampilkan data laporan menggunakan loop
        for laporan in result:
            print(f"ID Laporan: {laporan[0]}")
            print(f"Nama Sekolah: {laporan[1]}")
            print(f"Tanggal Dibuat: {laporan[2]}")
            print(f"Status: {laporan[3]}")
            print(f"Isi Laporan: {laporan[4]}")
            print("--------------------")
    else:
        print("=================================")
        print("Tidak ada laporan yang ditemukan.")
        print("=================================")
    input("Tekan Enter untuk kembali...")


def updateStatusLaporan():
    clear()
    print("Update Status Laporan:\n")
    id_laporan = input("Masukkan ID Laporan yang akan diperbarui statusnya: ")
    
    # Periksa apakah ID laporan valid
    query = "SELECT * FROM laporan WHERE ID_Laporan = %s"
    cursor.execute(query, (id_laporan,))
    result = cursor.fetchone()
    
    if result:
        print("=================================")
        print(f"Status saat ini: {result[5]}")
        print("=================================")
        new_status = input("Masukkan status baru ('Diproses' atau 'Selesai'): ").capitalize()
        
        # Periksa apakah status yang dimasukkan valid
        if new_status == "Diproses" or new_status == "Selesai":
            # Lakukan update status laporan
            query = "UPDATE laporan SET Status = %s WHERE ID_Laporan = %s"
            cursor.execute(query, (new_status, id_laporan))
            mydb.commit()
            print("===================================")
            print("Status laporan berhasil diperbarui.")
            print("===================================")
        else:
            print("===============================================================")
            print("Status tidak valid. Silakan masukkan 'Diproses' atau 'Selesai'.")
            print("===============================================================")
    else:
        print("==========================================")
        print("ID Laporan tidak valid. Silakan coba lagi.")
        print("==========================================")
    input("Tekan Enter untuk kembali...")



















# Fungsi untuk menampilkan menu pilihan untuk melihat data sekolah
def UserlihatDataSekolah():
    while True:
        clear()
        print("===================================")
        print("|       Menu Lihat Data Sekolah   |")
        print("===================================")
        print("|           1. Sorting            |")
        print("|           2. Searching          |")
        print("|           3. Lihat Data Sekolah |")
        print("|           0. Kembali            |")
        print("===================================")
        pilihan = int(input("Masukkan Pilihan: "))
        if pilihan == 1:
            UsersortingDataSekolah()
        elif pilihan == 2:
            UsersearchingDataSekolah(sekolahLinkedList)
        elif pilihan == 3:
            lihatDataSekolah()

        elif pilihan == 0:
            break
        else:
            print("=======================================")
            print("Pilihan tidak valid. Silakan coba lagi.")
            print("=======================================")


def UsersortingDataSekolah():
    while True:
        clear()
        print("================================================")
        print("|                     SORTING                  |")
        print("================================================")
        print("|            1. Nomor Induk Sekolah            |")
        print("|            2. Akreditasi                     |")
        print("|            3. kembali                        |")
        print("================================================")
        print("\n")
        sort_choice = int(input("Masukkan Pilihan: "))
        
        if sort_choice == 0:
            break
        elif sort_choice in [1, 2]:
            while True:
                print("===================")
                print("|   Pilih Urutan  |")
                print("|1. Ascending     |")
                print("|2. Descending    |")
                print("===================")
                order_choice = int(input("Masukkan Pilihan: "))
                
                if order_choice == 1:
                    sort_order = "DESC"
                    break
                elif order_choice == 2:
                    sort_order = "ASC"
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
            
            # Lakukan sorting
            if sort_choice == 1:
                sorted_list = urutkanDataSekolahNIS(sort_order)
            elif sort_choice == 2:
                sorted_list = urutkanDataSekolahAkredetasi(sort_order)
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


def UsersearchingDataSekolah(sekolahLinkedList):
    while True:
        
        clear()
        ambilDataSekolahSimpan(sekolahLinkedList)
        print("===========================================================")
        print("|                       SEARCHING                         |")
        print("===========================================================")
        print("|                1. Nomor Induk Sekolah                   |")
        print("|                2. Nama Sekolah                          |")
        print("|                0. Kembali                               |")
        print("===========================================================")
        search_choice = int(input("Masukkan Pilihan: "))

        if search_choice == 0:
            break
        elif search_choice == 1:
            keyword = input("Masukkan nomor induk sekolah yang ingin dicari: ")
            if sekolahLinkedList.head is not None:
                search_result = sekolahLinkedList.jumpSearchNIS(keyword)
                if search_result:
                    print("===============================================================")
                    print("Hasil Pencarian:")
                    print("ID Sekolah:", search_result.data["ID_Sekolah"])
                    print("Nama Sekolah:", search_result.data["Nama_Sekolah"])
                    print("Nomor Induk Sekolah:", search_result.data["Nomor_Induk_Sekolah"])
                    print("Akreditasi:", search_result.data["Akreditas"])
                    print("===============================================================")
                else:
                    print("====================================")
                    print("Nomor induk sekolah tidak ditemukan.")
                    print("====================================")
            else:
                print("=======================================")
                print("Tidak ada data sekolah yang dimasukkan.")
                print("=======================================")
                
        elif search_choice == 2:
            keyword = input("Masukkan nama sekolah yang ingin dicari: ")
            if sekolahLinkedList.head is not None:
                search_result = sekolahLinkedList.jumpSearchNamaSekolah(keyword) 
                if search_result:
                    print("=============================================================")
                    print("Hasil Pencarian:")
                    print("ID Sekolah:", search_result.data["ID_Sekolah"])
                    print("Nama Sekolah:", search_result.data["Nama_Sekolah"])
                    print("Nomor Induk Sekolah:", search_result.data["Nomor_Induk_Sekolah"])
                    print("Akreditasi:", search_result.data["Akreditas"])
                    print("=============================================================")
                else:
                    print("=============================")
                    print("Nama sekolah tidak ditemukan.")
                    print("=============================")
            else:
                print("=======================================")
                print("Tidak ada data sekolah yang dimasukkan.")
                print("=======================================")
        else:
            print("=======================================")
            print("Pilihan tidak valid. Silakan coba lagi.")
            print("=======================================")

        input("Tekan Enter untuk kembali...")











# Fungsi untuk menampilkan menu login user
def menuLoginUser():
    while True:
        clear()
        print("================================================")
        print("|               OPSI LOGIN USER                |")
        print("================================================")
        print("|            1. Lihat Data Sekolah             |")
        print("|            2. Login Akun User                |")
        print("|            0. Kembali                        |")
        print("================================================")
        print("\n")
        pilihan = int(input("Masukkan Pilihan: "))
        if pilihan == 1:
            UserlihatDataSekolah()
        elif pilihan == 2:
            opsilogin = input("Ingin login? (y/t) :")
            if opsilogin.lower()== "y":
                loginAkunUser()
            elif opsilogin.lower()== "t":
                opsibuatakun = input("Apa ingin buat akun? (y/t) :")
                if opsibuatakun.lower() == "y":
                    buatAkunUser()
                elif opsibuatakun.lower() == "t":
                    UserlihatDataSekolah()
                else:
                    print("silakan masukkan y atau t")
            else:
                print("silakan masukkan y atau t")
        elif pilihan == 0:
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")



def loginAkunUser():
    clear()
    print("================================================")
    print("===                LOGIN USER                ===")
    print("================================================")
    
    # Meminta input email dan password dari pengguna
    email = input("Email: ")
    password = input("Password: ")
    
    # Query ke database untuk memeriksa keberadaan akun user dengan email dan password yang sesuai
    query = "SELECT * FROM akun_user WHERE Email = %s AND Password = %s"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()
    
    if result:
        print("===============")
        print("Login berhasil!")
        print("===============")
        input("tekan enter untuk lanjut...")
        menuUserOptions()  # Memanggil menu pilihan user jika login berhasil
    else:
        print("Email atau password salah.")
        # Meminta pengguna apakah ingin mencoba login lagi atau membuat akun baru
        pilihan = input("Coba lagi? (y/t): ")
        if pilihan.lower() == 'y':
            loginAkunUser()
        elif pilihan.lower() == 't':
            menuLoginUser()
        else:
            print("====================")
            print("Pilihan tidak valid.")
            print("====================")



def buatAkunUser():
    clear()
    print("================================================")
    print("===              BUAT AKUN USER              ===")
    print("================================================")
    
    # Meminta input email, username, nama lengkap, dan password dari pengguna
    email = input("Email: ")
    username = input("Username: ")
    nama_lengkap = input("Nama Lengkap: ")
    password = input("Password: ")
    
    # Pemeriksaan format email menggunakan regular expression
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_pattern, email):
        print("Format email tidak valid. Mohon masukkan email yang valid.")
        # Meminta pengguna apakah ingin mencoba membuat akun lagi atau kembali ke menu utama
        pilihan = input("Coba lagi? (y/n): ")
        if pilihan.lower() == 'y':
            buatAkunUser()
        elif pilihan.lower() == 'n':
            UserlihatDataSekolah()
        else:
            print("====================")
            print("Pilihan tidak valid.")
            print("====================")
    else:
        # Query ke database untuk memeriksa keberadaan email
        query = "SELECT * FROM akun_user WHERE Email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        
        if result:
            print("Email sudah terdaftar. Silakan gunakan email lain.")
            # Meminta pengguna apakah ingin mencoba membuat akun lagi atau kembali ke menu utama
            pilihan = input("Coba lagi? (y/n): ")
            if pilihan.lower() == 'y':
                buatAkunUser()
            elif pilihan.lower() == 'n':
                UserlihatDataSekolah()
            else:
                print("====================")
                print("Pilihan tidak valid.")
                print("====================")
        else:
            # Menyimpan data akun baru ke database
            query = "INSERT INTO akun_user (Email, Username, Nama_Lengkap, Password) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (email, username, nama_lengkap, password))
            mydb.commit()
            print("=====================")
            print("Akun berhasil dibuat!")
            print("=====================")
            input("tekan enter untuk lanjut")
            main()








# Fungsi untuk menampilkan menu pilihan user setelah login
def menuUserOptions():
    while True:
        clear()
        print("================================================")
        print("|                   MENU USER                  |")
        print("================================================")
        print("|             1. Lihat Data Sekolah            |")
        print("|             2. Berikan Rating dan Ulasan     |")
        print("|             3. Laporkan Sekolah              |")
        print("|             0. Kembali                       |")
        print("================================================")
        pilihan = int(input("Masukkan Pilihan: "))
        if pilihan == 1:
            UserlihatDataSekolah()
        elif pilihan == 2:
            berikanRatingUlasan()
        elif pilihan == 3:
            laporkanSekolah()
        elif pilihan == 0:
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def berikanRatingUlasan():
    clear()
    lihatDataSekolah()
    print("\n")
    print("================================================")
    print("           Berikan Rating dan Ulasan           |")
    print("================================================")

    
    # Meminta input ID Sekolah
    id_sekolah = input("Masukkan ID Sekolah yang ingin Anda berikan rating dan ulasan: ")

    # Memeriksa keberadaan ID Sekolah dalam database
    cursor.execute("SELECT ID_Sekolah FROM sekolah WHERE ID_Sekolah = %s", (id_sekolah,))
    result = cursor.fetchone()

    if not result:
        print("=======================")
        print("ID Sekolah tidak valid.")
        print("=======================")
        input("Tekan Enter untuk kembali...")
        return

    # Meminta input rating dari pengguna (1-5)
    while True:
        try:
            rating = int(input("Masukkan rating (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Rating harus dalam rentang 1-5.")
        except ValueError:
            print("Masukkan angka.")

    # Meminta input ulasan dari pengguna (maksimal 200 kata)
    ulasan = input("Masukkan ulasan (maksimal 355 huruf): ")
    while len(ulasan.split()) > 355:
        print("Ulasan terlalu panjang. Harap masukkan ulasan dengan maksimal 200 kata.")
        ulasan = input("Masukkan ulasan (maksimal 355 huruf): ")

    # Mendapatkan tanggal saat ini
    tanggal_diberikan = datetime.datetime.now()

    # Menyimpan rating dan ulasan ke database
    insert_query = "INSERT INTO rating_dan_ulasan (ID_Sekolah, Tanggal_Diberikan, Rating, Ulasan) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (id_sekolah, tanggal_diberikan, rating, ulasan))
    mydb.commit()  # Melakukan commit untuk menyimpan perubahan

    # Menampilkan pesan bahwa rating dan ulasan telah diberikan
    print("=========================================================")
    print("Rating dan ulasan mu akan menjadi penilaian buat kami :D ")
    print("=========================================================")
    input("Tekan Enter untuk kembali ke menu...")








def laporkanSekolah():
    clear()
    lihatDataSekolah()
    print("\n")
    print("=========================================")
    print("|           Laporkan Sekolah             ")
    print("=========================================")

    # Meminta input ID Sekolah
    id_sekolah = input("Masukkan ID Sekolah yang ingin dilaporkan: ")

    # Memeriksa keberadaan ID Sekolah dalam database
    cursor.execute("SELECT ID_Sekolah FROM sekolah WHERE ID_Sekolah = %s", (id_sekolah,))
    result = cursor.fetchone()

    if not result:
        print("=======================")
        print("ID Sekolah tidak valid.")
        print("=======================")
        input("Tekan Enter untuk kembali...")
        return

    # Meminta input isi laporan dari pengguna (maksimal 355 karakter)
    isi_laporan = input("Masukkan isi laporan (maksimal 355 karakter): ")
    while len(isi_laporan) > 355:
        print("Isi laporan terlalu panjang. Harap masukkan isi laporan dengan maksimal 355 karakter.")
        isi_laporan = input("Masukkan isi laporan (maksimal 355 karakter): ")

    # Mendapatkan tanggal saat ini
    tanggal_dibuat = datetime.datetime.now()

    # Mengambil nama sekolah dari tabel sekolah
    cursor.execute("SELECT Nama_Sekolah FROM sekolah WHERE ID_Sekolah = %s", (id_sekolah,))
    nama_sekolah = cursor.fetchone()[0]

    # Menyimpan laporan ke database dengan status "Menunggu"
    insert_query = "INSERT INTO laporan (Nama_Sekolah, Tanggal_Dibuat, Isi_Laporan, Status) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (nama_sekolah, tanggal_dibuat, isi_laporan, "Menunggu"))
    mydb.commit()  # Melakukan commit untuk menyimpan perubahan

    # Menampilkan pesan bahwa laporan telah disimpan bersama dengan nama sekolah
    print("=======================")
    print("Laporan telah disimpan.")
    print("=======================")
    input("Tekan Enter untuk kembali ke menu...")







# Fungsi untuk menampilkan menu utama
def main():
    while True:
        try:
            clear()
            print("==============================")
            print("|      Selamat Datang!       |")
            print("|Pilih jenis pengguna        |")
            print("|1. Admin                    |")
            print("|2. User                     |")
            print("|3. Keluar                   |")
            print("==============================")
            pilihan = int(input("Masukkan Pilihan: "))
            if pilihan == 1:
                menuLoginAdmin()
            elif pilihan == 2:
                menuLoginUser()
            elif pilihan == 3:
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("==========================")
            print("Masukkan angka yang valid.")
            print("==========================")
            input("tekan enter untuk lanjut")
        except KeyboardInterrupt:
            print("============================================")
            print("Program berhenti karena Anda menekan Ctrl+C.")
            print("============================================")
            input("tekan enter untuk lanjut")
        except Exception as e:
            print("===========================================")
            print("Program berhenti karena Anda menekan Ctrl+Z", e)
            print("===========================================")
            input("tekan enter untuk lanjut")


if __name__ == "__main__":
    main()