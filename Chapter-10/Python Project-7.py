n = '\n'
fileinput = input('Masukkan file yang akan di decrypt : ')
nosandi = int(input('Masukkan nomor sandi : '))
bukafile = open(fileinput, 'r')
asli = bukafile.read()

mylist = []

for i in range(len(asli)):
    a = ord(asli[i])
    if 65 <= a <= 90:
        a -= nosandi
        if a < 65:
            a += 26
    elif 97 <= a <= 122:
        a -= nosandi
        if a < 97:
            a += 26
    elif a == 32:
        a = 32
    b = chr(a)
    mylist.append(b)

bukafile.close()

print('Teks Asli : ', end ='')
for i in range(len(mylist)):
    print(mylist[i], end='')