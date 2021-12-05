n = '\n'
myfile = open('fileProject2.txt', 'r')

dataTotal = []

myfile.seek(0)
eachLine = myfile.readlines()
for i in range(len(eachLine)):
    semuaData = {}
    data = eachLine[i].replace('\n', '')
    dataMhs = data.split('|')
    semuaData['nim']=dataMhs[0]
    semuaData['nama']=dataMhs[1]
    semuaData['alamat']=dataMhs[2]
    dataTotal.append(semuaData)

print(dataTotal)
myfile.close()