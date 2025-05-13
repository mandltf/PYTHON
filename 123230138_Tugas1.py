import os

buku = {
    "ID" : [],
    "Judul" : [],
    "Nama Penulis" : [],
    "Kategori" : [],
    "Penerbit" : []
}

def tambah_data():
    id = input("ID buku\t: ")
    if id in buku["ID"]:
        print("Buku sudah terdaftar")
    else:
        buku["ID"].append(id)
        judul = input("Judul Buku\t: ")
        buku["Judul"].append(judul)
        penulis = input("Nama Penulis\t: ")
        buku["Nama Penulis"].append(penulis)
        kategori = input("Kategori\t: ")
        buku["Kategori"].append(kategori)
        penerbit = input("Penerbit\t: ")
        buku["Penerbit"].append(penerbit)

def tampil_data():
    if len(buku["ID"]) == 0:
        print("Tidak ada data buku")
    else:
        i = 0
        while i < len(buku["ID"]):
            print(f"ID Buku\t: {buku['ID'][i]}")
            print(f"Judul Buku\t: {buku['Judul'][i]}")
            print(f"Nama Penulis\t: {buku['Nama Penulis'][i]}")
            print(f"Kategori\t: {buku['Kategori'][i]}")
            print(f"Penerbit\t: {buku['Penerbit'][i]}")
            i += 1
            print("\n")

def cari_data():
    ditemukan = False
    judul = input("Masukkan nama buku: ")
    for x in range(len(buku["Judul"])):
        if judul.lower() in buku["Judul"][x].lower():
            print(f"ID Buku\t: {buku['ID'][x]}")
            print(f"Judul Buku\t: {buku['Judul'][x]}")
            print(f"Nama Penulis\t: {buku['Nama Penulis'][x]}")
            print(f"Kategori\t: {buku['Kategori'][x]}")
            print(f"Penerbit\t: {buku['Penerbit'][x]}")
            print("\n")
            ditemukan = True

    if not ditemukan:
        print("Buku tidak ditemukan")

def hapus_data():
    id = input("Masukkan id buku yang ingin dihapus: ")
    if id in buku["ID"]:
        index = buku["ID"].index(id)
        buku["ID"].pop(index)
        buku["Judul"].pop(index)
        buku["Nama Penulis"].pop(index)
        buku["Kategori"].pop(index)
        buku["Penerbit"].pop(index)
        print("Buku dengan ID "+id+" berhasil dihapus")
    else:
        print("ID buku tidak ditemukan")

pilih = 0            
while pilih <= 5:
    print("Sistem Manajemen Perpustakaan")
    print("-------------------------------")
    print("1. Tambah Data Buku")
    print("2. Tampilkan Data Buku")
    print("3. Cari Data Buku")
    print("4. Hapus Data Buku")
    print("5. Keluar")
    pilih = int(input("masukkan pilihan : "))
    os.system("cls")

    if pilih == 1:
        tambah_data()
        input("Tekan Enter untuk membersihkan layar...")
        os.system("cls")
    elif pilih == 2:
        tampil_data()
        input("Tekan Enter untuk membersihkan layar...")
        os.system("cls")
    elif pilih == 3:
        cari_data()
        input("Tekan Enter untuk membersihkan layar...")
        os.system("cls")
    elif pilih == 4:
        hapus_data()
        input("Tekan Enter untuk membersihkan layar...")
        os.system("cls")
    elif pilih == 5:
        print("Terima kasih telah menggunakan sistem manajemen perpustakaan")
        break
