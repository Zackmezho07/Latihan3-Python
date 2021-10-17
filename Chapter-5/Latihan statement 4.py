kode = input('Masukkan kode karyawan        : ')
nama = input('Masukkan nama karaywan        : ')
gol  = input('Masukkan golongan             : ')

r = '\r'

if (gol == 'A') or (gol == 'B') or (gol == 'C') or (gol == 'D'):
    print(f'===================================={r}')
    print(f'STRUK RINCIAN GAJI KARYAWAN{r}')
    print(f'------------------------------------{r}')
    print(f'Nama karyawan       : {nama} (Kode:{kode}){r}')
    print(f'Golongan            : {gol}{r}')
    print(f'------------------------------------{r}')
    if (gol == 'A'):
        x = 10000000
        y = 2.5
        z = y/100*x
        v = x - z
    elif (gol == 'B'):
        x = 8500000
        y = 2.0
        z = y/100*x
        v = x - z
    elif (gol == 'B'):
        x = 7000000
        y = 1.5
        z = y/100*x
        v = x - z
    elif (gol == 'B'):
        x = 5500000
        y = 1.0
        z = y/100*x
        v = x - z
    
    print(f'Gaji Pokok          : Rp{x}{r}')
    print(f'Potongan ({y}%)     : Rp{z}{r}')
    print(f'------------------------------------  -{r}')
    print(f'Gaji Bersih         : Rp{v}{r}')
else:
    print('Masukkan golongan yang valid (A atau B atau C atau D)')