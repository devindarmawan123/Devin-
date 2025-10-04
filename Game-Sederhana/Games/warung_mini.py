import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import menu
import db

def add():
    kode_barang = input("kode barang : ")
    nama_barang = input("nama barang : ")
    harga_barang = int(input("harga barang : "))
    stok_barang = int(input("stok barang : "))
    
    db.insert_barang(kode_barang,nama_barang,harga_barang,stok_barang)
 
    
def check():
    items = db.fetch_item()
    for item in items:
        kode_barang = item[1]
        nama_barang = item[2]
        harga_barang = item[3]
        stok_barang = item[4]
        print(f"\nkode {kode_barang}\n{nama_barang} | Rp.{harga_barang}\nstok = {stok_barang}\n")
def game ():
    while True: 
        print("selamat datang di warung mini")
        menu1 = int(input("menu: \n 1. Tambah Barang \n 2. Cek Barang \n 3. Kembali \nsilahkan pilih : "))
        if menu1 == 1:
            add()
        elif menu1 == 2:
            check()
        elif menu1 == 3:
            menu.menu() 
        else:
            break
            
