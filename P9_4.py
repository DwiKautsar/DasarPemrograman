# Nama : Dwi Raysah Anandifa Kautsar
# NIM : 2401300
# Kelas : RPL 1C

jam_mulai = int(input("Masukkan jam mulai: "))
menit_mulai = int(input("Masukkan menit mulai: "))
detik_mulai = int(input("Masukkan detik mulai: "))

jam_selesai = int(input("Masukkan jam selesai: "))
menit_selesai = int(input("Masukkan menit selesai: "))
detik_selesai = int(input("Masukkan detik selesai: "))

total_detik_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
total_detik_selesai = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai

selisih_detik = total_detik_selesai - total_detik_mulai

jam_selisih = selisih_detik // 3600
menit_selisih = (selisih_detik % 3600) // 60
detik_selisih = selisih_detik % 60

print(f"Selisih waktu: {jam_selisih} jam - {menit_selisih} menit - {detik_selisih} detik")