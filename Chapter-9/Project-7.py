mhs =   ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
        'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
        'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

data = []
tanggal = []
for i in range(len(mhs)):
    a = mhs[i].split(':')
    data.append(a)
for i in range(len(data)):
    b = data[i][2].replace('-', '/')
    tanggal.append(b)

print('==============================================================')
print('NIM      NAMA MAHASISWA          TGL LAHIR     TEMPAT LAHIR   ')
print('==============================================================')

for i in range(len(data)):
    print(data[i][0].ljust(9), end='')
    print(data[i][1].ljust(24), end='')
    print(tanggal[i].ljust(14), end='')
    print(data[i][3].ljust(15))

print('==============================================================')
