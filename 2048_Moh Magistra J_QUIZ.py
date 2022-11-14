# NAMA  = MOH.MAGISTRA JAHFAL 
# NIM   = 222410102048
# PRODI = TEKNOLOGI INFORMASI
# KELAS = D 

print (3*"=","QUIZ ALGO",3*"=")

import random #untuk merandom angka 
angka = random.randint(0,100) #berfungsi untuk mengatur angka dengan range 0-100
bebas = 0

while bebas < 7 : #menggunakan while karena menggunakan perulangan dan dibatasi sampai tujuh kali
    inputan1 = int(input('\nMasukkan angka :'))
    bebas += 1 #agar inputan selalu berulang dan selalu bertambah
    if inputan1 == angka : #untuk inputan angka benar
        print(f"Selamat tebakan anda tepat, anda menebak sebanyak {bebas} kali") #menggunakan f karena dalam inputan terdapat variabel
        break #agar berhenti ketika inputan benar
    if bebas == 7 and inputan1 != angka : #untuk inputan lebih dari 7x
        print("Anda kurang beruntung")
    elif inputan1 < angka :#untuk inputan angka kurang/lebih kecil
        print("Tidak tepat, angka terlalu kecil")
        continue
    elif inputan1 > angka : #untuk inputan angka lebih/lebih besar
        print("Tidak tepat, angka terlalu besar")
        continue

print (3*"=","PERMAINAN BERAKHIR TERIMAKASIH",3*"=")      