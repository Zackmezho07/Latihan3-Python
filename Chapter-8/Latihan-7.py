buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

def palingMahal(x):
    a = x.values()
    b = tuple(a)
    c = max(b)
    for key, value in x.items():
        if value == c:
            print('Buah paling mahal adalah ', key)
    
palingMahal(buah)