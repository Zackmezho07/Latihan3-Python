nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
        {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
        {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
        {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
        {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

nilaiAkhir = []
for i in range(len(nilai)):
    a = nilai[i]['mid']
    b = nilai[i]['uas']
    bb = b * 2
    rerata = (a + bb) / 3
    rerata = round(rerata, 2)
    if rerata >= 60:
        nilaiAkhir.append([rerata, 'LULUS'])
    elif rerata < 60:
        nilaiAkhir.append([rerata, 'TIDAK LULUS'])


print('======================================================================')
print('NIM      NAMA           N.MIDN        N.UAS     N.AKHIR         STATUS')
print('======================================================================')

for i in range(len(nilai)):
    print(nilai[i]['nim'].ljust(9), end='')
    print(nilai[i]['nama'].ljust(11), end='')
    print(str(nilai[i]['mid']).rjust(10), end='')
    print(str(nilai[i]['uas']).rjust(13), end='')
    print(str(nilaiAkhir[i][0]).rjust(12), end='')
    print(nilaiAkhir[i][1].rjust(15))

print('======================================================================')