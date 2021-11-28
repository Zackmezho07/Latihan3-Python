def polaDiamond(a):
    b = (a - 1) / 2 + 1
    n = int(b)
    for i in range ((-n)+1,n):
        t = n-abs(i)
        print(" "*(n-t), end=" ")
        for j in range(1,t+1):
            print('*',end=" ")
        print("")
        
z = polaDiamond(7)
print(z)