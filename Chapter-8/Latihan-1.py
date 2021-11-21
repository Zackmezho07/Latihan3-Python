jmlBil = int(input('Jumlah bilangan bulat yang ingin dimasukkan : '))
n = []
for i in range(jmlBil):
    a = int(input('Masukkan bilangan : '))
    n.append(a)

n.sort(reverse= True)

print('bilangan yang anda masukkan adalah : ')
print(n)