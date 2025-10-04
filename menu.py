from Games import cuypy
from Games import warung_mini
from Games import angka
import penutup
 
def menu ():
    print("Menu Program :\n 1. Games CuyPY \n 2. Game Warung Mini \n 3. Game Tebak Angka \n 4. Keluar dari Program")
    pilihan = int(input("silahkan pilih : "))
    if pilihan == 1:
        cuypy.game()
    elif pilihan == 2:
        warung_mini.game()
    elif pilihan == 3:
        angka.game()
    else:
        penutup.penutup()