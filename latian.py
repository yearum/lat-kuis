import math

# menu soal
print("""
Pilih perhitungan:
1. Diameter Lingkaran dari Luas
2. Tinggi Segitiga dari Luas dan Alas
3. Sisi Segitiga Sama Sisi dari Luas
4. Sisi Persegi dari Luas
5. Panjang Persegi Panjang dari Luas dan Lebar
6. Harga Barang dari Total Bayar dan Banyak Barang
7. Persentase Mahasiswa Hadir
8. Persentase Diskon
9. Panjang Rusuk Kubus dari Volume
10. Panjang Rusuk Kubus dari Diagonal Ruang
11. Diagonal Ruang dari Volume Kubus
12. Nilai Akhir Mata Kuliah
13. Jarak Tempuh dari Kecepatan dan Waktu Tempuh
14. Kecepatan dari Jarak Tempuh dan Waktu Tempuh
""")

# Memilih soal
pilihan = int(input("Masukkan pilihan (1-14): "))

# 1. Diameter Lingkaran dari Luas
if pilihan == 1:
    luas = float(input("Masukkan luas lingkaran: "))
    r = math.sqrt(luas / math.pi)
    diameter = 2 * r
    print(f"Diameter lingkaran: {diameter}")

# 2. Tinggi Segitiga dari Luas dan Alas
elif pilihan == 2:
    luas = float(input("Masukkan luas segitiga: "))
    alas = float(input("Masukkan alas segitiga: "))
    tinggi = (2 * luas) / alas
    print(f"Tinggi segitiga: {tinggi}")

# 3. Sisi Segitiga Sama Sisi dari Luas
elif pilihan == 3:
    luas = float(input("Masukkan luas segitiga sama sisi: "))
    sisi = math.sqrt((4 * luas) / math.sqrt(3))
    print(f"Sisi segitiga sama sisi: {sisi}")

# 4. Sisi Persegi dari Luas
elif pilihan == 4:
    luas = float(input("Masukkan luas persegi: "))
    sisi = math.sqrt(luas)
    print(f"Sisi persegi: {sisi}")

# 5. Panjang Persegi Panjang dari Luas dan Lebar
elif pilihan == 5:
    luas = float(input("Masukkan luas persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    panjang = luas / lebar
    print(f"Panjang persegi panjang: {panjang}")

# 6. Harga Barang dari Total Bayar dan Banyak Barang
elif pilihan == 6:
    total_bayar = float(input("Masukkan total bayar: "))
    banyak_barang = int(input("Masukkan jumlah barang: "))
    harga = total_bayar / banyak_barang
    print(f"Harga per barang: {harga}")

# 7. Persentase Mahasiswa Hadir
elif pilihan == 7:
    hadir = int(input("Masukkan jumlah mahasiswa yang hadir: "))
    total = int(input("Masukkan jumlah seluruh mahasiswa: "))
    persentase = (hadir / total) * 100
    print(f"Persentase mahasiswa yang hadir: {persentase}%")

# 8. Persentase Diskon
elif pilihan == 8:
    total_bayar = float(input("Masukkan total bayar: "))
    total_belanja = float(input("Masukkan total belanja: "))
    diskon = ((total_belanja - total_bayar) / total_belanja) * 100
    print(f"Persentase diskon: {diskon}%")

# 9. Panjang Rusuk Kubus dari Volume
elif pilihan == 9:
    volume = float(input("Masukkan volume kubus: "))
    rusuk = volume ** (1/3)
    print(f"Panjang rusuk kubus: {rusuk}")

# 10. Panjang Rusuk Kubus dari Diagonal Ruang
elif pilihan == 10:
    diagonal = float(input("Masukkan diagonal ruang kubus: "))
    rusuk = diagonal / math.sqrt(3)
    print(f"Panjang rusuk kubus: {rusuk}")

# 11. Diagonal Ruang dari Volume Kubus
elif pilihan == 11:
    volume = float(input("Masukkan volume kubus: "))
    rusuk = volume ** (1/3)
    diagonal = rusuk * math.sqrt(3)
    print(f"Diagonal ruang kubus: {diagonal}")

# 12. Nilai Akhir Mata Kuliah
elif pilihan == 12:
    P = float(input("Masukkan nilai partisipasi: "))
    T = float(input("Masukkan nilai tugas: "))
    NT = float(input("Masukkan nilai UTS: "))
    NS = float(input("Masukkan nilai UAS: "))
    NA = (P + 2 * T + 3 * NT + 4 * NS) / 10
    print(f"Nilai akhir: {NA}")

# 13. Jarak Tempuh dari Kecepatan dan Waktu Tempuh
elif pilihan == 13:
    kecepatan = float(input("Masukkan kecepatan (km/jam): "))
    waktu = float(input("Masukkan waktu tempuh (menit): "))
    jarak = kecepatan * (waktu / 60)
    print(f"Jarak tempuh: {jarak} km")

# 14. Kecepatan dari Jarak Tempuh dan Waktu Tempuh
elif pilihan == 14:
    jarak = float(input("Masukkan jarak tempuh (meter): "))
    waktu = float(input("Masukkan waktu tempuh (menit): "))
    kecepatan = (jarak / 1000) / (waktu / 60)
    print(f"Kecepatan: {kecepatan} km/jam")

else:
    print("Pilihan tidak valid.")
