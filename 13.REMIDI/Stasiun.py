import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    clear_screen()

# jenis kendaraan yang kamu pakai
    kendaraan = int((input('''kendaraan yang kamu pakai 
                          ketik 1500/1000
                          1500. mobil
                          1000. motor

                          pilihan kamu:''')))
    durasi = float(input('Berapa lama kamu parkir?'))
    
    if durasi <= 0:
        print('Data tidak valid')
        break

# perhitungan biaya
    elif durasi <= 2:
        tarif = 3000
        print (tarif)

# tambahan biaya jika melebihi 24 jam
    elif durasi <= 24:

        print (3000 + (durasi - 2) * kendaraan)

    else:

        print (3000 +(durasi - 2) * kendaraan + 10000)

        kondisi = input("\napakah kamu ingin melanjutkan kalkulator lagi? (y/n)")
    if kondisi == 'n' :
        print('terimakasih telah menggunakan aplikasi ini')
        break
