# durasi 
def hitung_biaya_parkir(lama_durasi_parkir):
    if lama_durasi_parkir <= 2:
        biaya_parkir = 3000
    else:
        biaya_parkir = 3000 + (lama_durasi_parkir - 2) * 1500
    if lama_durasi_parkir > 24:
            biaya_parkir += 10000
    return round(biaya_parkir)

# menghitung biaya parkir
def main():
    print("Program Perhitungan Biaya Parkir")
    lama_waktu_parkir = float(input("Masukkan lama waktu parkir (jam): "))
    biaya_parkir = hitung_biaya_parkir(lama_waktu_parkir)
    print(f"Biaya parkir: Rp {biaya_parkir:,.2f}")

if "_name_" == "_main_":
    main()
    
# perulangan
kondisi = input("\napakah kamu ingin melanjutkan kalkulator lagi? (y/n)")
if kondisi == 'n' :
   print('terimakasih telah menggunakan aplikasi ini')