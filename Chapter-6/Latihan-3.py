e = '\n'

def faktorial(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a

print(f'Hasil dari C(5, 3) adalah : {faktorial(5) / (faktorial(3) * faktorial(5-3))}')
print(f'Hasil dari P(10, 7) adalah : {faktorial(10) / faktorial(10-7)}')