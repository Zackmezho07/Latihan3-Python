buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

def rerataBuah(arr):
    harga = arr.values()
    jml = 0
    for i in harga:
        jml += i
    rerata = jml / len(harga)
    return rerata

print(f' Rerata harga buah adalah {rerataBuah(buah)}')