def hitung_total_belanja():
    try:
        # Meminta pengguna memasukkan jumlah barang
        jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))
        
        # Validasi jumlah barang
        if jumlah_barang <= 0:
            print("Jumlah barang harus lebih dari 0.")
            return

        total_belanja = 0.0

        # Meminta harga setiap barang
        for i in range(1, jumlah_barang + 1):
            while True:
                try:
                    harga = float(input(f"Masukkan harga barang ke-{i}: "))
                    
                    # Validasi harga
                    if harga < 0:
                        print("Harga tidak boleh negatif. Silakan masukkan harga yang benar.")
                    else:
                        total_belanja += harga
                        break  # Keluar dari loop jika harga valid
                except ValueError:
                    print("Input tidak valid. Harap masukkan angka untuk harga.")
        
        # Menampilkan total belanja
        print(f"Total belanjaan Anda adalah: Rp{total_belanja:.2f}")
    
    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk jumlah barang.")

# Memanggil fungsi
hitung_total_belanja()
