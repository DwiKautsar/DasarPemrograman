# Nama : Dwi Raysah Anandifa Kautsar
# NIM : 2401300
# Kelas : RPL 1C

password = "Latihan"

def login():
    kesalahan = 0
    while kesalahan < 3:
        input_username = input("Username: ")
        input_password = input("Password: ")

        if input_password == password:
            print("Selamat Datang di Laboratorium Komputer SMAN 2 Harapan")
            return True
        else:
            kesalahan += 1
            print(f"Login gagal. Kesalahan {kesalahan} dari 3.")

    print("Anda tidak diperkenankan mengakses aplikasi ini.")
    return False

login()
print("Hello World")

def logout():
    print("Anda telah keluar dari aplikasi ini.")
    return True

logout()
print("Bekasi")