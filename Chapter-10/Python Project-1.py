n = '\n'

myfile = open('fileProject1.txt', 'r')
eachLine = myfile.readlines()

genap = 0
ganjil = 0

for i in range(len(eachLine)):
    if i % 2 == 0:
        genap += 1
    else:
        ganjil += 1

print(f'Banyaknya bilangan ganjil : {ganjil}')
print(f'Banyaknya bilangan genap : {genap}')

myfile.close()