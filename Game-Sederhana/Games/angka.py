import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import menu
import random

def game():
    print("selamat datang di tebak angka, disini anda harus menebak angka 0-100 dan kesempatan anda menebak 10x")
    again = "y"
    while again == "y":
        rand = random.randint(0,100)
        berhasil = False
        for i in range (9,-1,-1):
            angka = int(input("masukan angka 0-100 : "))
            if angka == rand:
                print(f"selamat anda berhahsil menebak angka, apakah anda ingin bermain lagi?")
                berhasil  = True    
                break
            elif angka > rand:
                print(f"terlalu atas kesempatan anda tersisa {i}x")
            elif angka < rand:
                print(f"terlalu bawah kesepatan anda terisa {i}x")  
        if not berhasil:
            print(f"maaf kesempatan anda habis jawabannya yaitu {rand} ingin bermain lagi?")
        again = input("apakah anda ingin bermain lagi \njawaban user (y/n) : ")
        if again == "n":
            menu.menu()
        while again != "y":
            again = input("jawabannya hanya ada y/n : ")
            if again == "n":
                    menu.menu()
        else:
            menu.menu