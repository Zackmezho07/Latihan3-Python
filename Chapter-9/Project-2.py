def bintang(n):
    for i in range(n):
        a = i * 2 + 1
        aa = n * 2 - 1
        b = '*' * a
        print(b.center(aa, ' '))
        
z = bintang(5)
print(z)