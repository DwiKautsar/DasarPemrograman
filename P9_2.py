# Nama : Dwi Raysah Anandifa Kautsar
# NIM : 2401300
# Kelas : RPL 1C

def fibonacci(n):
    x = [0, 1]
    while len(x) < n:
        x.append(x[-1] + x[-2])
    return x

n = int(input("Masukkan jumlah deret Fibonacci: "))
print(fibonacci(n))