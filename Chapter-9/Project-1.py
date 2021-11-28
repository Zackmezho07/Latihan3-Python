def ubahHuruf(teks, a, b):
    mylist = []
    for i in range(len(teks)):
        alpha = teks[i]
        mylist.append(alpha)
    for i in range(len(mylist)):
        if mylist[i] == a:
            mylist[i] = b
    word = ''.join(mylist)
    return word

kata = ubahHuruf('saya suka python', 'a', 'i')
print(kata)