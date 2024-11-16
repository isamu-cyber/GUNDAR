#ani pergi ke kampus lebih cepat sebelum pujul 9. dia berjanji kepada kawannya untuk membagi buah jeruk sebanyak 5. 
#tetapi jika dia pergi terlambat lewat dari pukul 9 maka dia tidak membagi buah jeruknya.

#Pseucode nya
#Mulai
    #Tampilkan "Masukkan jam kedatangan"
    #Baca jam_kedatangan
    #Jika jam_kedatangan < 9
    #Tampilkan "Ani membagikan jeruk"
    #Jika tidak
    #Tampilkan "Ani tidak membagikan jeruk"
#Akhir

# Program untuk menentukan jumlah jeruk yang akan dibagi Ani
# Variabel waktu batas (pukul 9) dan jumlah jeruk yang dibagikan
waktu_batas = 9
jumlah_jeruk = 5

# input kedatangan ani
jam_kedatangan = int(input("Masukkan jam kedatangan Ani: "))

# Cek apakah Ani datang sebelum pukul 9
if jam_kedatangan < waktu_batas:
    print("Ani membagikan jeruk sebanyak:", jumlah_jeruk)
else:
    print("Ani tidak membagikan jeruk.")

# program selesai
print("Program selesai.")

