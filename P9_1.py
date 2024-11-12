# Nama : Dwi Raysah Anandifa Kautsar
# NIM : 2401300
# Kelas : RPL 1C

def total_rata_rata(nilai):
    total = sum(nilai)
    rata_rata = total / len(nilai)
    return total, rata_rata

input_nilai = input("Masukkan nilai yang dipisahkan dengan koma (contoh: 2,3,5,10): ")
nilai_list = [int(n) for n in input_nilai.split(",")] #fungsi split untuk memisahkan string menjadi bebrapa bagian
total, rata_rata = total_rata_rata(nilai_list)

print(f"Total : {total}")
print(f"Rata-rata : {rata_rata}")  
print("Hello World")