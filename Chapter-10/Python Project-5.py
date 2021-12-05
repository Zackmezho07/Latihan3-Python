n = '\n'
myfile = open('fileProject5.txt', 'r')

listData = []
eachLine = myfile.readlines()
for i in range(len(eachLine)):
    data = eachLine[i].replace('\n', '')
    nomor = data.split('|')
    a = int(nomor[0])
    b = int(nomor[1])
    hasil = a + b
    listData.append(hasil)

for i in range(len(listData)):
    print(listData[i])

myfile.close()