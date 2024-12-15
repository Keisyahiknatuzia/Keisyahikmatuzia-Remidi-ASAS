def hitung_biaya_pengiriman(dimensi_paket, berat_paket, area_pengiriman):
    print("=== Sistem Perhitungan Biaya Pengiriman ===")
    
    # Input dimensi paket
    tinggi = float(input("Masukkan tinggi paket (cm): "))
    panjang = float(input("Masukkan panjang paket (cm): "))
    lebar = float(input("Masukkan lebar paket (cm): "))
    
    # Input berat paket
    berat = float(input("Masukkan berat paket (kg): "))
    
    # Input area pengiriman
    di_pasuruan = input("Apakah paket dikirim di area pasuruan (ya/tidak): ").lower()
    
    if di_pasuruan == "ya":
        # Jika berat lebih dari 1 kg
        if berat > 1:
            # Jika dimensi paket <= 50x50x50 cm
            if tinggi <= 50 and panjang <= 50 and lebar <= 50:
                biaya = 6000 * berat
            else:
                biaya = 5000 + (7000 * berat)
            print(f"Biaya pengiriman Anda adalah Rp{biaya:.2f}")
        else:
            print("Maaf, pengiriman hanya tersedia di area Pasuruan.")
    
    print("=== Selesai ===")
    
    kondisi = input("\napakah kamu ingin melanjutkan kalkulator lagi? (y/n)")
    if kondisi == 'n' :
        print('terimakasih telah menggunakan aplikasi ini')

