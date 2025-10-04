import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import menu
import random
import copy
def game():
    print ("Selamat datang di cuypy \nsilahkan pilih salah 1 dari 4 cuypy dibawah ni")
    while True:
        cuypy = ["|_|"]* 4
        cuyrand = random.randint(0,3)
        cuypy_len = copy.deepcopy(cuypy)
        cuypy_len[cuyrand] = "|0_0|" 
        print(" ".join(cuypy))
        jawab = int(input("masukan angka 1-4 : "))
        if jawab == cuyrand+1:
            print(" ".join(cuypy_len))
            print(f"selamat jawaban anda benar cuypy ada di {cuyrand+1}, apkaah ingin bermain lagi?")
            again = input("jawaban user (y/n) : ")
            while again != "y" and again != "n":
                    again = input("jawabannya hanya (y/n) jgn yang lain : ")
            if again == "y":
                continue
            elif again == "n":
                break
        else:
            print(" ".join(cuypy_len))
            print(f"maaf jawaban anda salah cuypy ada di {cuyrand+1} apakah anda ingin bermain lagi? ")
            again = input("jawaban user (y/n) : ")
            while again != "y" and again != "n":
                    again = input("jawabannya hanya (y/n) jgn yang lain : ")
            if again == "y":
                continue
            elif again == "n":
                break
    menu.menu()