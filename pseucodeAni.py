# Mulai program

# Definisikan variabel waktu batas (pukul 9) dan jumlah jeruk yang dibagikan
waktu_batas = 9
jumlah_jeruk = 5

# Meminta input jam kedatangan Ani sebagai integer
jam_kedatangan = int(input("Masukkan jam kedatangan Ani (dalam angka bulat): "))

# Cek apakah Ani datang sebelum pukul 9
if jam_kedatangan < waktu_batas:
    print("Ani membagikan jeruk sebanyak:", jumlah_jeruk)
else:
    print("Ani tidak membagikan jeruk.")

# Menampilkan pesan bahwa program telah selesai
print("Program selesai.")
