# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 00:37:59 2022

@author: utku
"""

def isFamous (matris,notFamousPersons,size,index):
    
    for i in matris[index]:
        if i == 1: #kisi birisini taniyorsa unlu degildir
            notFamousPersons.append(index)
        elif i == 0:
            #bi kisinin tanimadigi kimse unlu olamaz
            notFamousPersons.append(i)
            
    return

matris = []

#kare bi matris olması gerektigini varsayiyiorum
rawInput = input() #our input like "1 2 3"
Input = rawInput.split() #our input like ['1','2','3']
size = len(Input) #our matris size X size

matris.append(Input)

for i in range(size - 1):
    rawInput = input() #our input like "1 2 3"
    Input = rawInput.split() #our input like ['1','2','3']
    matris.append(Input)
    
for i in range(size): #matris char -> int
    for j in range(size):
        matris[i][j] = int(matris[i][j])

notFamousPersons = [] #birisi eger buradaysa unlu degildir

for i in range(size):
    if notFamousPersons.count(i) == 0:
        #eger bir kisinin unlu olmadigini anlamissak onu eksiltip oyle devam edıyoruz
        isFamous(matris, notFamousPersons, size, i)

isThereFamous = False

for i in range(size): #unlu olmayanlar listesinde olmayan kisi unludur
    if notFamousPersons.count(i) == 0:
        print(i)
        isThereFamous = True
        break

if not isThereFamous: #eger kimse unlu degilse -1 yazacagiz
    print(-1)
    
