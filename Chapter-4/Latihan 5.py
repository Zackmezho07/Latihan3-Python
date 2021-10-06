a = int(input(' Banyak mahasiswa laki-laki : '))
b = int(input(' Banyak mahasiswa perempuan : '))

aa = a // 10
bb = b // 10

print('--------------------Diagram batang data mahasiswa--------------------')
print('                                  .                                  ')
print('                                  .                                  ')
print('Mahasiswa Laki-laki    :' + '#'*aa + f' ({a})')
print('Mahasiswa Perempuan    :' + '#'*bb + f' ({b})')