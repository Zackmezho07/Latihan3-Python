def sum(*bil):
    jumlah = 0
    for i in bil:
        jumlah += i
    return jumlah

def average(*bil):
    banyak = len(bil)
    jumlah = 0
    for i in bil:
        jumlah += i
    rerata = float(jumlah) / float(banyak)
    return rerata

def maks(*bil):
    hasil = max(bil)
    return hasil

def mini(*bil):
    hasil = min(bil)
    return hasil

print(f'Nilai rata-rata dari data 5, 10, 4, 9, 30, 16, 2, 11 adalah : {average(5, 10, 4, 9, 30, 16, 2, 11)}')
print(f'Nilai maksimum dari data 5, 10, 4, 9, 30, 16, 2, 11 adalah  : {maks(5, 10, 4, 9, 30, 16, 2, 11)}')
print(f'Nilai minimum dari data 5, 10, 4, 9, 30, 16, 2, 11 adalah   : {mini(5, 10, 4, 9, 30, 16, 2, 11)}')
print('====================================================================')
print(f'Nilai rata-rata dari data 81, 98, 12, 83, 45, 77, 69, 30, 56 adalah :   {average(81, 98, 12, 83, 45, 77, 69, 30, 56)}')
print(f'Nilai maksimum dari data 81, 98, 12, 83, 45, 77, 69, 30, 56 adalah  :   {maks(81, 98, 12, 83, 45, 77, 69, 30, 56)}')
print(f'Nilai minimum dari data 81, 98, 12, 83, 45, 77, 69, 30, 56 adalah   :   {mini(81, 98, 12, 83, 45, 77, 69, 30, 56)}')