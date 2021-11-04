nama = input("Masukkan nama file : ")

try:
    file = open(nama, "r")
    print(f'isi file {nama} adalah : ')
    print(file.read())
except FileNotFoundError:
    print('File tidak ditemukan')