from random import randint

bil = randint(0, 100)
n = '\n'

print(f'Haii... Nama saya Mr.Misterio, saya telah memilih bilangan bulat acak dari 0 sampai 100.{n}Silahkan kamu tebak ya!!! Semoga beruntung')
while True:
    tebak = int(input('Angka tebakan kamu : '))
    if(tebak < bil):
        print('Maaf hehe.., bilangan tebakan kamu terlalu kecil o_o')
    elif(tebak > bil):
        print('Maaf hehe.., bilangan tebakan kamu terlalu besar :V')
    elif(tebak == bil):
        print('Yeii.., selamat tebakan kamu benar >_<')
        break