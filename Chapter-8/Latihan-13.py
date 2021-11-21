nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	        {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

def nilaiTertinggi(arr):
    dataMhs = {}
    for i in arr:
        uas = int(i['uas']) * 2
        jmlhNilai = int(i['mid']) + uas / 3
        name = i['nama']
        nim = i['nim']
        data = f'{name} ({nim})'
        dataMhs[data] = jmlhNilai
    a = (dataMhs.values())
    b = max(a)
    for x,y in dataMhs.items():
        if y == b:
            print(f'Nilai akhir tertinggi adalah {x}')
            
nilaiTertinggi(nilaiMhs)