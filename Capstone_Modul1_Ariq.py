from datetime import datetime

list_pasien = [{'id':10001,'nama': 'Agus Wijaya', 'usia': 28, 'jenis_kelamin': 'Pria', 'alamat': 'Jl. Sudirman No. 123, Jakarta, Indonesia', 'pekerjaan': 'Manajer Proyek', 'tanggal_registrasi': '2022-06-12','kunjungan':[]},
{'id':10002,'nama': 'Ratna Susilo', 'usia': 34, 'jenis_kelamin': 'Wanita', 'alamat': 'Jl. Gajah Mada No. 456, Surabaya, Indonesia', 'pekerjaan': 'Analisis Data', 'tanggal_registrasi': '2020-09-08','kunjungan':[]},
{'id':10003,'nama': 'Siti Rahayu', 'usia': 42, 'jenis_kelamin': 'Wanita', 'alamat': 'Jl. Imam Bonjol No. 789, Bandung, Indonesia', 'pekerjaan': 'Guru', 'tanggal_registrasi': '2019-03-21','kunjungan':[]},
{'id':10004,'nama': 'Budi Santoso', 'usia': 21, 'jenis_kelamin': 'Pria', 'alamat': 'Jl. Pemuda No. 987, Yogyakarta, Indonesia', 'pekerjaan': 'Desainer Grafis', 'tanggal_registrasi': '2023-01-05','kunjungan':[]},
{'id':10005,'nama': 'Dewi Utami', 'usia': 47, 'jenis_kelamin': 'Wanita', 'alamat': 'Jl. Diponegoro No. 321, Medan, Indonesia', 'pekerjaan': 'Akuntan', 'tanggal_registrasi': '2021-11-16','kunjungan':[]}]

def main_menu():
    menu = input('''
Selamat Datang di Database Rumah Sakit Alamanda
1. Menampilkan Data Pasien
2. Menambahkan Pasien Baru
3. Mengupdate Data Pasien
4. Menghapus Data Pasien
5. Sorting Data Pasien
6. Menambahkan Kunjungan Pasien
7. Menu Dokter
Masukkan angka Menu yang ingin dijalankan :''')
    
    if menu == '1':
        menu1()
    elif menu == '2':
        menu2()
    else:
        main_menu()

def menu1():
    menu = input('''
Menampilkan Data Pasien
1. Menampilkan Seluruh Data Pasien
2. Mencari Data Pasien (Nomor Pasien)
3. Kembali Ke Menu Awal
Masukkan angka Menu yang ingin dijalankan :''')
    
    if menu == '1':
        display()
    elif menu == '2':
        id = int(input('Masukkan Nomor Pasien yang ingin dilihat : '))
        display(id)
    elif menu == '3':
        main_menu()
    else:
        print('Menu Tidak Tersedia')
        menu1()

def display(id = 0):
    if len(list_pasien) != 0:
        if id == 0:
            print()
            print("Daftar Pasien")
            print()
            print("Nomor | Nama \t \t | Usia  | Jenis Kelamin | Alamat \t \t \t \t \t | Pekerjaan \t \t | Tanggal Registrasi \t | Kunjungan")
            for i in list_pasien:
                print(f'{i["id"]} | {i["nama"]} \t | {i["usia"]} \t | {i["jenis_kelamin"]} \t | {i["alamat"]} \t | {i["pekerjaan"]:<15} \t | {i["tanggal_registrasi"]} \t \t | {i["kunjungan"]}')
            print()
        else :
            checkData = False
            for i in list_pasien:
                if i["id"] == id:
                    checkData = True
            if checkData == True:
                print()
                print("Daftar Pasien")
                print()
                print("Nomor | Nama \t \t | Usia  | Jenis Kelamin | Alamat \t \t \t \t \t | Pekerjaan \t \t | Tanggal Registrasi \t | Kunjungan")
                for i in list_pasien:
                    if i["id"] == id:
                        print(f'{i["id"]} | {i["nama"]} \t | {i["usia"]} \t | {i["jenis_kelamin"]} \t | {i["alamat"]} \t | {i["pekerjaan"]:<15} \t | {i["tanggal_registrasi"]} \t \t | {i["kunjungan"]}')
                print()
            else :
                print(f"Data Pasien dengan nomor {id} Tidak Ada")
    else :
        print("Data Pasien Tidak Ada")
    main_menu()

def menu2():
    print()
    tambah_nama = input("Masukkan Nama Pasien : ")
    tambah_usia = int(input("Masukkan Usia Pasien : "))
    
    konfirmasi_input = True
    # untuk mengecek inputan "Pria atau Wanita"
    while konfirmasi_input :
        tambah_kelamin = input("Masukkan Jenis Kelamin Pasien (Pria/Wanita) : ")
        if tambah_kelamin.lower() == 'pria' or tambah_kelamin.lower() == 'wanita'  :
            konfirmasi_input = False
        else :
            print("Jenis kelamin tidak sesuai")

    tambah_alamat = input("Masukkan Alamat Pasien : ")
    tambah_pekerjaan = input("Masukkan Pekerjaan Pasien : ")

    list_pasien.append({
        'id':list_pasien[len(list_pasien)-1]['id'] + 1 , 
        'nama':tambah_nama,
        'usia':tambah_usia,
        'jenis_kelamin':tambah_kelamin.capitalize(),
        'alamat':tambah_alamat,
        'pekerjaan':tambah_pekerjaan,
        'tanggal_registrasi' : datetime.now().strftime("%Y-%m-%d"),
        'kunjungan':[] })
    
    print("Data Pasien Berhasil Ditambahkan")
    display()

main_menu()