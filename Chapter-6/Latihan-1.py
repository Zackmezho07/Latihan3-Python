def isPythagoras(a, b, c):
    hasil = a**2 + b**2 - c**2
    if(hasil == 0):
        return 'True'
    else:
        return 'False'

a = 3
b = 4
c = 5
print(isPythagoras(a, b, c))