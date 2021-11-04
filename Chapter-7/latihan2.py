n = '\n'
nama_file = input('Masukkan nama file : ')

def tambah():
    try:
        file = open(nama_file, "a")
        data = input('Data yang mau ditambahkan : ')
        data_input = f"{data}{n}"
        file.write(data_input)
        file.close()
    except FileNotFoundError:
        print('Maaf nama file tidak diketahui')
    
while True:
    tambah()
    tanya = str(input('Mau lagi? (y/n)'))
    if tanya == 'n' :
        break
    
buka_file = open(nama_file, "r")
print('Data anda : ')
print(buka_file.read())
