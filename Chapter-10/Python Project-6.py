n = '\n'
asli = input('Masukkan Teks yang akan di sandi : ')
nosandi = int(input('Masukkan nomor sandi : '))

mylist = []

for i in range(len(asli)):
    a = ord(asli[i])
    if 65 <= a <= 90:
        a += nosandi
        if a >90:
            a -= 26
    elif 97 <= a <= 122:
        a += nosandi
        if a > 122:
            a -= 26
    elif a == 32:
        a = 32
    b = chr(a)
    mylist.append(b)

print('Teks Sandi : ', end ='')
for i in range(len(mylist)):
    print(mylist[i], end='')

