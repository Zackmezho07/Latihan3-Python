a = int(input('Masukkan nilai Bhs Indonesia : '))
b = int(input('Masukkan nilai IPA           : '))
c = int(input('Masukkan nilai Matematika    : '))

if (0 <= a <= 100) and (0 <= b <= 100) and (0 <= c <= 100):
    if (a >= 60) and (b >= 60) and (c > 70):
        print('LULUS')
    else:
        print('Status kelulusan         :TIDAK LULUS')
else:
    print('Mohon masukkan nilai valid yaitu nilai diantara 0 - 100')