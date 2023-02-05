# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:32:12 2022

@author: utku
"""

array = input()

newArray = []

indexM = 0

B = ""
M = ""
W = ""

BMW = ""

for i in array:
    if i == 'B':
        newArray.insert(0,i) #B başta olacak
        indexM += 1
        B = B + 'B'
    elif i == 'M':
        newArray.insert(indexM, i) #M B'lerden sonra 
        M = M + 'M'
    elif i == 'W':
        newArray.append(i) #W en sona eklenecek
        W = W + 'W'
       
BMW = B + M + W
print(BMW,end=(""))
#print(newArray) #düzenlenmiş listemizi yazdırmak istersek

""" Bu kod ile birlikte hem sıralanmış string (BMW) elde ettik hem de sıralanmış array (newArray)"""