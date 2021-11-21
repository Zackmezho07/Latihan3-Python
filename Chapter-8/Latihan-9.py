buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
for i in buah:
    print(i)

nama = input('Nama buah yang dibeli : ')
kg =   int(input('Berapa Kg?           : '))
a = buah[nama]
b = a*kg

print('----------------------')
print(f'Total harga         :{b}')