from datetime import datetime

# Data Pasien Awal
list_pasien = [{'id':10001,'nama': 'Agus Wijaya', 'usia': 28, 'jenis_kelamin': 'Pria', 'alamat': 'Jl. Sudirman No. 123, Jakarta, Indonesia', 'pekerjaan': 'Manajer Proyek', 'tanggal_registrasi': '2019-06-12','kunjungan':[]},
{'id':10002,'nama': 'Ratna Susilo', 'usia': 34, 'jenis_kelamin': 'Wanita', 'alamat': 'Jl. Gajah Mada No. 456, Surabaya, Indonesia', 'pekerjaan': 'Analisis Data', 'tanggal_registrasi': '2020-09-08','kunjungan':[]},
{'id':10003,'nama': 'Siti Rahayu', 'usia': 42, 'jenis_kelamin': 'Wanita', 'alamat': 'Jl. Imam Bonjol No. 789, Bandung, Indonesia', 'pekerjaan': 'Guru', 'tanggal_registrasi': '2021-03-21','kunjungan':[]},
{'id':10004,'nama': 'Budi Santoso', 'usia': 21, 'jenis_kelamin': 'Pria', 'alamat': 'Jl. Pemuda No. 987, Yogyakarta, Indonesia', 'pekerjaan': 'Desainer Grafis', 'tanggal_registrasi': '2022-01-05','kunjungan':[]},
{'id':10005,'nama': 'Dewi Utami', 'usia': 47, 'jenis_kelamin': 'Wanita', 'alamat': 'Jl. Diponegoro No. 321, Medan, Indonesia', 'pekerjaan': 'Akuntan', 'tanggal_registrasi': '2022-11-16','kunjungan':[]}]

# Data Dokter Awal
list_dokter = [{'nama': 'Dr. Ahmad Basuki', 'spesialis': 'Dokter Umum'}, {'nama': 'Dr. Budi Santoso', 'spesialis': 'Dokter Gigi'}, {'nama': 'Dr. Chandra Pratama', 'spesialis': 'Dokter THT'}, {'nama': 'Dr. Dewianto Joko', 'spesialis': 'Dokter Umum'}, {'nama': 'Dr. Eka Putra', 'spesialis': 'Dokter Mata'}, {'nama': 'Dr. Gita Purnama', 'spesialis': 'Dokter Mata'}, {'nama': 'Dr. Hadi Nugraha', 'spesialis': 'Dokter Gigi'}, {'nama': 'Dr. Indra Kusuma', 'spesialis': 'Dokter Kulit'}]

# Main Menu
def main_menu():
    menu = input('''
Selamat Datang di Database Rumah Sakit Alamanda
1. Menampilkan Data Pasien
2. Menambahkan Pasien Baru
3. Mengupdate Data Pasien
4. Menghapus Data Pasien
5. Sorting Data Pasien
6. Menu Kunjungan Pasien
7. Menu Dokter
8. Exit Program
Masukkan angka Menu yang ingin dijalankan :''')
    
    if menu == '1':
        menu1()
    elif menu == '2':
        menu2()
    elif menu == '3':
        menu3()    
    elif menu == '4':
        menu4()
    elif menu == '5':
        menu5()  
    elif menu == '6':
        menu6()
    elif menu == '7':
        menu7()
    elif menu == '8':
        print("Terimakasih Telah Berkunjung")
        exit() 
    else:
        print("Input Tidak Valid")
        main_menu()
         
# Menu Read
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
        try:
            id = int(input('Masukkan Nomor Pasien yang ingin dilihat : '))
            filter_id(id)
        except ValueError:
            print('Masukkan Angka yang Benar')
    elif menu == '3':
        main_menu()
    else:
        print('Menu Tidak Tersedia')
    menu1()

# Menu Create
def menu2():
    menu = input('''
Menambah Data Pasien
1. Menambah Data Pasien
2. Kembali Ke Menu Awal
Masukkan angka Menu yang ingin dijalankan :''')
    
    if menu == '1':
        print()
        try : 
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
        except ValueError:
            print('Masukkan Angka yang Benar')
    elif menu == '2':
        main_menu()
    else:
        print('Menu Tidak Tersedia')
    menu2()    

# Menu Update
def menu3():
    menu = input('''
Mengupdate Data Pasien
1. Mengupdate Data Pasien
2. Kembali Ke Menu Awal
Masukkan angka Menu yang ingin dijalankan :''')
    
    if menu == '1':
        try:
            display()
            id = int(input('Masukkan Nomor Pasien yang ingin diupdate : '))
            filter_id(id,'edit')
        except ValueError:
            print('Masukkan Angka yang Benar')
    elif menu == '2':
        main_menu()
    else:
        print('Menu Tidak Tersedia')
    menu3()  

# Menu Delete
def menu4():
    menu = input('''
Menghapus Data Pasien
1. Menghapus Data Pasien
2. Kembali Ke Menu Awal
Masukkan angka Menu yang ingin dijalankan :''')
    
    if menu == '1':
        try:
            display()
            id = int(input('Masukkan Nomor Pasien yang ingin dihapus : '))
            filter_id(id,'delete')
        except ValueError:
            print('Masukkan Angka yang Benar')
    elif menu == '2':
        main_menu()
    else:
        print('Menu Tidak Tersedia')
    menu4()

# Menu Sorting
def menu5():
    menu = input('''
Sorting Data Pasien Berdasarkan
1. Nama (A-Z)
2. Nama (Z-A)
3. Usia (Muda - Tua)
4. Usia (Tua - Muda)
5. Tanggal Registrasi (dari terbaru)
6. Kembali Ke Menu Awal
Masukkan angka Menu yang ingin dijalankan :''')
    
    if menu == '1':
        display(0,'nama')
    elif menu == '2':
        display(0,'nama',True)
    elif menu == '3':
        display(0,'usia')
    elif menu == '4':
        display(0,'usia',True)
    elif menu == '5':
        display(0,'tanggal_registrasi',True)           
    elif menu == '6':
        main_menu()
    else:
        print('Menu Tidak Tersedia')
    menu5()

# Menu Kunjungan Pasien
def menu6():
    menu = input('''
Menu Kunjungan Pasien
1. Melihat Kunjungan Per Pasien
2. Menambahkan Data Kunjungan Pasien
3. Kembali Ke Menu Awal
Masukkan angka Menu yang ingin dijalankan :''')
    
    if menu == '1':
        try:
            display()
            id = int(input('Masukkan Nomor Pasien yang ingin dilihat : '))
            filter_id(id,'kunjungan')
        except ValueError:
            print('Masukkan Angka yang Benar')
    elif menu == '2':
        try:
            display()
            id = int(input('Masukkan Nomor Pasien yang ingin ditambahkan kunjungan : '))
            data = list(filter(lambda i:i if i['id'] == id else '',list_pasien))
            if len(data) != 0:
                display_dokter()
                tambah_dokter = int(input("Masukkan Nomor Dokter : "))
                if 0<tambah_dokter<=len(list_dokter):
                    tambah_keluhan = input("Masukkan Keluhan Pasien : ")
                    index = list_pasien.index(data[0])
                    list_pasien[index]['kunjungan'].append({
                    'tanggal': datetime.now().strftime("%Y-%m-%d"),
                    'dokter':list_dokter[tambah_dokter-1]['nama'],
                    'keluhan':tambah_keluhan
                    })
                    print()
                    print("Data Kunjungan Berhasil Ditambahkan")
                else:
                    print("Dokter Tidak Ditemukan")
            else:
                print(f"Data Pasien dengan nomor {id} Tidak Ada")
        except ValueError:
                print('Masukkan Angka yang Benar') 
    elif menu == '3':
        main_menu()
    else:
        print('Menu Tidak Tersedia')
    menu6()

# Menu Dokter
def menu7():
    menu = input('''
Menu Dokter
1. Menambah Data Dokter
2. Menghapus Data Dokter
3. Kembali Ke Menu Awal
Masukkan angka Menu yang ingin dijalankan :''')
    
    if menu == '1':
        tambah_nama = input("Masukkan Nama Dokter : ")
        tambah_spesialis = input("Masukkan Spesialis Dokter : ")
        list_dokter.append({
            'nama':tambah_nama,
            'spesialis':tambah_spesialis
        })
        print()
        print("Data Dokter Berhasil Ditambahkan")
        display_dokter()
    elif menu == '2':
        try:
            display_dokter()
            id = int(input('Masukkan Nomor Dokter yang ingin dihapus : '))
            if 0<id<=len(list_dokter):
                konfirmasi_hapus = True
                while konfirmasi_hapus:
                    konfirmasi = input(f"Apakah yakin ingin menghapus data dengan nomor dokter {id}? (Ya/Tidak) : ")
                    if konfirmasi.lower() == 'ya':
                        konfirmasi_hapus = False
                        list_dokter.pop(id-1)
                        print()
                        print("Data Dokter Berhasil Dihapus")
                        display_dokter()
                    elif konfirmasi.lower() == 'tidak':
                        konfirmasi_hapus = False
                    else :
                        print("Input Tidak Valid")
            else:
                print(f"Data Dokter dengan nomor {id} Tidak Ada")
        except ValueError:
                print('Masukkan Angka yang Benar')
    elif menu == '3':
        main_menu()
    else:
        print('Menu Tidak Tersedia')
    menu7()

# Untuk print List Pasien
def display(id = 0,sort='',reverse=False):
    if len(list_pasien) != 0:
        print()
        print("Daftar Pasien")
        print()
        print(f"Nomor | {'Nama':<20} | {'Usia':<5} | {'Jenis Kelamin':<15} | {'Alamat':<50} | {'Pekerjaan':<15} | Tanggal Registrasi")
        if id == 0:
            if sort == '':
                for i in list_pasien:
                    print(f'{i["id"]:<5} | {i["nama"]:<20} | {i["usia"]:<5} | {i["jenis_kelamin"]:<15} | {i["alamat"]:<50} | {i["pekerjaan"]:<15} | {i["tanggal_registrasi"]}')
                print()
            else :
                newList = sorted(list_pasien, key=lambda d: d[sort],reverse=reverse)
                for i in newList:
                    print(f'{i["id"]:<5} | {i["nama"]:<20} | {i["usia"]:<5} | {i["jenis_kelamin"]:<15} | {i["alamat"]:<50} | {i["pekerjaan"]:<15} | {i["tanggal_registrasi"]}')
                print() 
        else :
            for i in list_pasien:
                if i["id"] == id:
                    print(f'{i["id"]:<5} | {i["nama"]:<20} | {i["usia"]:<5} | {i["jenis_kelamin"]:<15} | {i["alamat"]:<50} | {i["pekerjaan"]:<15} | {i["tanggal_registrasi"]}')
            print()
            
    else :
        print("Data Pasien Tidak Ada")

# Untuk filter nomor pasien apakah ada atau tidak dan juga fungsi selanjutnya seperti edit dan delete atau hanya read
def filter_id(id,step='read'):
    data = list(filter(lambda i:i if i['id'] == id else '',list_pasien))
    if len(data) > 0:
        if step == 'edit':
            display(id)
            handleEdit(data)
        elif step == 'delete':
            display(id)
            handleDelete(data)
        elif step == 'kunjungan':
            if len(data[0]['kunjungan']) > 0 :
                display_kunjungan(id)
            else :
                print("Pasien Belum Pernah Berkunjung, Hanya Mendaftar")
        elif step == 'read' :
            display(id)
    else:
        print(f"Data Pasien dengan nomor {id} Tidak Ada")


# untuk edit pasien
def handleEdit(data):
    index = list_pasien.index(data[0])
    konfirmasi_input = True
    while konfirmasi_input :
        edit = input(f"Apakah ingin mengupdate data dengan nomor pasien {data[0]['id']} (Ya/Tidak) : ")
        if edit.lower() == 'ya'    :
            konfirmasi_input = False
            form_edit = True
            while form_edit:
                menu_edit = input('''
Pilih kolom yang ingin diupdate
1. Nama
2. Usia
3. Alamat
4. Pekerjaan
5. Kembali Ke Menu Edit
Masukkan angka kolom yang ingin diupdate :''')

                if menu_edit == '1':
                    new_value = input("Masukkan Nama Baru Pasien :")
                    print(f"Data nama berubah dari {data[0]['nama']} menjadi {new_value}")
                    konfirmasi_edit = True
                    while konfirmasi_edit:
                        konfirmasi = input("Apakah tetap ingin mengupdate data? (Ya/Tidak) : ")
                        if konfirmasi.lower() == 'ya'   :
                           konfirmasi_edit = False
                           list_pasien[index]['nama'] = new_value
                           print("Data Berhasil Di Update")
                           display(list_pasien[index]['id'])
                           konfirmasi_more = True
                           while konfirmasi_more:
                                more = input("Apakah ingin mengupdate kolom lain? (Ya/Tidak) :")
                                if more.lower() == 'ya'   :
                                    konfirmasi_more = False
                                    form_edit = True
                                elif more.lower() == 'tidak'   :
                                    konfirmasi_more = False
                                    form_edit = False    
                                else :
                                    print("Input Tidak Sesuai")
                        elif konfirmasi.lower() == 'tidak' :
                            konfirmasi_edit = False
                        else :
                            print("Input Tidak Sesuai")
                elif menu_edit == '2':
                    try:
                        new_value = int(input("Masukkan Usia Baru Pasien :"))
                        print(f"Data usia berubah dari {data[0]['usia']} menjadi {new_value}")
                        konfirmasi_edit = True
                        while konfirmasi_edit:
                            konfirmasi = input("Apakah tetap ingin mengupdate data? (Ya/Tidak) : ")
                            if konfirmasi.lower() == 'ya'   :
                                konfirmasi_edit = False
                                list_pasien[index]['usia'] = new_value
                                print("Data Berhasil Di Update")
                                display(list_pasien[index]['id'])
                                konfirmasi_more = True
                                while konfirmasi_more:
                                    more = input("Apakah ingin mengupdate kolom lain? (Ya/Tidak) :")
                                    if more.lower() == 'ya'   :
                                        konfirmasi_more = False
                                        form_edit = True
                                    elif more.lower() == 'tidak'   :
                                        konfirmasi_more = False
                                        form_edit = False   
                                    else :
                                        print("Input Tidak Sesuai")
                            elif konfirmasi.lower() == 'tidak' :
                                konfirmasi_edit = False
                            else :
                                print("Input Tidak Sesuai")
                    except ValueError:
                        print('Masukkan Angka yang Benar')
                elif menu_edit == '3':
                    new_value = input("Masukkan Alamat Baru Pasien :")
                    print(f"Data alamat berubah dari {data[0]['alamat']} menjadi {new_value}")
                    konfirmasi_edit = True
                    while konfirmasi_edit:
                        konfirmasi = input("Apakah tetap ingin mengupdate data? (Ya/Tidak) : ")
                        if konfirmasi.lower() == 'ya'   :
                           konfirmasi_edit = False
                           list_pasien[index]['alamat'] = new_value
                           print("Data Berhasil Di Update")
                           display(list_pasien[index]['id'])
                           konfirmasi_more = True
                           while konfirmasi_more:
                                more = input("Apakah ingin mengupdate kolom lain? (Ya/Tidak) :")
                                if more.lower() == 'ya'   :
                                    konfirmasi_more = False
                                    form_edit = True
                                elif more.lower() == 'tidak'   :
                                    konfirmasi_more = False
                                    form_edit = False    
                                else :
                                    print("Input Tidak Sesuai")
                        elif konfirmasi.lower() == 'tidak' :
                            konfirmasi_edit = False
                        else :
                            print("Input Tidak Sesuai")
                elif menu_edit == '4':
                    new_value = input("Masukkan Pekerjaan Baru Pasien :")
                    print(f"Data pekerjaan berubah dari {data[0]['pekerjaan']} menjadi {new_value}")
                    konfirmasi_edit = True
                    while konfirmasi_edit:
                        konfirmasi = input("Apakah tetap ingin mengupdate data? (Ya/Tidak) : ")
                        if konfirmasi.lower() == 'ya'   :
                           konfirmasi_edit = False
                           list_pasien[index]['pekerjaan'] = new_value
                           print("Data Berhasil Di Update")
                           display(list_pasien[index]['id'])
                           konfirmasi_more = True
                           while konfirmasi_more:
                                more = input("Apakah ingin mengupdate kolom lain? (Ya/Tidak) :")
                                if more.lower() == 'ya'   :
                                    konfirmasi_more = False
                                    form_edit = True
                                elif more.lower() == 'tidak'   :
                                    konfirmasi_more = False
                                    form_edit = False    
                                else :
                                    print("Input Tidak Sesuai")
                        elif konfirmasi.lower() == 'tidak' :
                            konfirmasi_edit = False
                        else :
                            print("Input Tidak Sesuai")
                elif menu_edit == '5' :
                    form_edit = False
                else :
                    print("Input Tidak Valid")

        elif edit.lower() == 'tidak' :
            konfirmasi_input = False
        else :
            print("Input tidak valid") 

# untuk delete pasien
def handleDelete(data):
    konfirmasi_hapus = True
    while konfirmasi_hapus:
        konfirmasi = input(f"Apakah yakin ingin menghapus data dengan nomor pasien {data[0]['id']}? (Ya/Tidak) : ")
        if konfirmasi.lower() == 'ya':
            konfirmasi_hapus = False
            list_pasien.remove(data[0])
            print("Data Pasien Berhasil Di Hapus")
            display()
        elif konfirmasi.lower() == 'tidak':
            konfirmasi_hapus = False
        else :
            print("Input Tidak Valid")

# Untuk print kunjungan per pasien
def display_kunjungan(id):
        print()
        print(f"Daftar Kunjungan Pasien {id}")
        print()
        print(f"{'Tanggal':<30} | {'Dokter':<30} | Keluhan")
        data = list(filter(lambda i:i if i['id'] == id else '',list_pasien))
        for i in data[0]['kunjungan']:
            print(f'{i["tanggal"]:<30} | {i["dokter"]:<30} | {i["keluhan"]}')
        print()

# Untuk print list dokter
def display_dokter():
        print()
        print("Daftar Dokter")
        print()
        print(f"{'Nomor':<10} | {'Nama':<30} | Spesialis")
        for index,i in enumerate(list_dokter):
            print(f'{index+1:<10} | {i["nama"]:<30} | {i["spesialis"]}')
        print()

# Untuk menjalankan fungsi utama
main_menu()