myList = []

while True:
    nama = input('Masukkan nama : ')
    jml = list(nama)
    jml = len(nama)
    
    a = f'{nama} ({jml} karakter)'
    myList.append(a)
    
    keluar = ['n', 'N']
    b = input('Masukkan lagi? (y/n)')
    if b in keluar:
        break

for i in myList:
    print(i)