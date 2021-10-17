kode = input('Masukkan kode karyawan                    : ')
nama = input('Masukkan nama karaywan                    : ')
gol  = input('Masukkan golongan                         : ')
stat = int(input('Masukkan status(1 : Menikah, 2: belum)    : '))
if (stat == 1) or (stat == 2):
    if (stat == 1):
        anak = int(input('Masukkan jumlah anak                  : '))
        status = 'Sudah menikah'
    elif (stat == 2):
        anak = 'Tidak memiliki anak'
        status = 'Belum Menikah'
else:
    print('Mohon masukkan stat dengan benar (1 atau 2)')
    exit()

r = '\r'

if (gol == 'A') or (gol == 'B') or (gol == 'C') or (gol == 'D'):
    print(f'===================================={r}')
    print(f'STRUK RINCIAN GAJI KARYAWAN{r}')
    print(f'------------------------------------{r}')
    print(f'Nama karyawan           : {nama} (Kode:{kode}){r}')
    print(f'Golongan                : {gol}{r}')
    print(f'Status Menikah          : {status}{r}')
    print(f'Jumlah anak             : {anak}{r}')
    print(f'------------------------------------{r}')
    if (gol == 'A'):
        x = 10000000
        y = 2.5
        z = y/100*x
    elif (gol == 'B'):
        x = 8500000
        y = 2.0
        z = y/100*x
    elif (gol == 'B'):
        x = 7000000
        y = 1.5
        z = y/100*x
    elif (gol == 'B'):
        x = 5500000
        y = 1.0
        z = y/100*x
    
    print(f'Gaji Pokok              : Rp{x}{r}')

    n = 10/100*x
    if(stat == 1):
        m = 5/100*anak*x
        o = x + n + m
    elif(stat == 2):
        m = 'Tidak memiliki anak'
        o = x + n
    p = o - z
    
    print(f'Tunjangan istri/suami   : Rp{n}{r}')
    print(f'Tunjangan anak          : Rp{m}{r}')
    print(f'------------------------------------  +{r}')
    print(f'Gaji kotor              : Rp{o}{r}')
    print(f'Potongan ({y}%)         : Rp{z}{r}')
    print(f'------------------------------------  -{r}')
    print(f'Gaji Bersih             : Rp{p}{r}')
else:
    print('Masukkan golongan yang valid (A atau B atau C atau D)')