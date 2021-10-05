jamawal = int(input("masukkan jam peminjaman : "))
menitawal = int(input("masukkan menit peminjaman : "))

jamakhir = int(input("masukkan jam pengembalian : "))
menitakhir = int(input("masukkan menit pengembalian : "))

menit = menitawal/60
awal = jamawal + menit

menitpengembalian = menitakhir/60
akhir = menitpengembalian + jamakhir

total = akhir - awal
jam = round(total, 2)

if (jam == 12) :
    a = jam * 200000
    print(f'Tarif sewa mobil anda adalah {a}')
elif (jam < 12) :
    b = jam * 200000
    print(f'Tarif sewa mobil anda adalah {b}')
elif (jam > 12) :
    x = jam - 12
    y = x * 10000
    z = y + 200000
    print(f'Tarif sewa mobil anda adalah Rp.{z} rupiah')

