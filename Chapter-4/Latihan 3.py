jarak = int(input('Masukkan jarak yang anda tempuh : '))

a = jarak/12
liter = round(a, 2)

print(f'Bensin yang anda perlukan untuk menempuh perjalanan anda adalah {liter} liter')

if(liter <= 50) :
    print('Anda minimal harus mengisi bensin 1 kali')
elif(liter > 50) :
    x = liter//50
    y = liter%50
    if(y > 0):
        z = x + 1
        print(f'Anda minimal harus mengisi bensin {z} kali diperjalanan')
    elif(y == 0):
        print(f'Anda minimal harus mengisi bensin {x} kali diperjalanan')