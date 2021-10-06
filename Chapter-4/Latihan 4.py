jaraka = int(input('Jarak perjalanan yang ditempuh dari kota A ke B : '))
jarakb = int(input('Jarak perjalanan yang ditempuh dari kota B ke C : '))

kecepatana = int(input('Kecepatan berkendara dari kota A ke B : '))
kecepatanb = int(input('Kecepatan berkendara dari kota B ke C : '))

istirahat = int(input('Lama beristirahat dalam menit : '))
print('Pukul berapa anda berangkat?')
jam = int(input('Jam : '))
menit = int(input('menit : '))

a = jaraka/kecepatana*60
b = jarakb/kecepatanb*60

c = a + b + istirahat
cc = c % 60
ccc = round(cc, 1)
cccc = c//60
ccccc = ccc * 60

jamsampai = jam + cccc
y = int(jamsampai)
menitsampai = menit + ccc
z = int(round(menitsampai, 0))

if(z < 60) :
    print(f'Anda diperkirakan akan sampai di kota C pada pukul {y}:{z} ')
elif(z >= 60):
    x = z // 60
    xx = z % 60
    xxx = y + x
    print(f'Anda diperkirakan akan sampai di kota C pada pukul {xxx}:{xx}')