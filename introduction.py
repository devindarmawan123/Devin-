import getpass
def introduction ():
    judul = f"halo {getpass.getuser()} selamat datang di cuygame"
    judul_len = len(judul)
    bintang = "*"*(judul_len + 4)
    print(bintang)
    print(f"**{judul}**")
    print(bintang)