print('---------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('---------------------------')

def input_bilangan():
    bil = int(input('Masukkan bilangan bulat : '))
    return bil

jumlah = 0
banyak = 0

while True:
    try:
        jumlah += input_bilangan()
        banyak += 1
    except TypeError:
        print('Mohon masukkan bilangan bulat dengan benar')
    except ValueError:
        print('Mohon masukkan bilangan bulat dengan benar')
    tanya = str(input('Lagi? (y/n)'))
    if tanya == 'n':
        break
rerata = jumlah/banyak

print(f'Rata-ratanya adalah : {rerata}')