import time
def penutup() :
    for i in range (3,0,-1):
        print(f"program akan dihentikan dalam {i}.....")
        time.sleep(1)
    print("program dihentikan")
    exit()