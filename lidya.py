nama = str (input('MASUKAN NAMA :'))
usia = int(input('MASUKAN USIA :'))
tinggi_badan = float(input('MASUKAN TINGGI BADAN :'))
berat_badan = float(input('MASUKAN BERAT BADAN ANDA :'))
jenis_kelamin = str (input('MASUKAN JENIS KELAMIN :'))
pendidikan_terakhir= str (input('MASUKAN PENDIDIKAN ANDA :'))

if usia >16 and tinggi_badan > 150 and berat_badan >40 :
  hasil = 'SELAMAT ANDA DITERIMA'

else :
  hasil = 'MAAF ANDA BELUM DITERIMA'

print(nama)
print(hasil)