def starFormation(n):
    for i in range(n):
        i += 1
        print('*' * i)
    return n

def starFormation2(n):
    for i in range(n):
        print('*' * n)
        n -= 1

def starFormation3(n):
    a = 1
    for i in range(n):
        print('*' * a)
        if i <= 2:
            a += 1
        elif i >= 3:
            a -= 1
n = 7
starFormation(n)
starFormation2(n)
starFormation3(n)
