# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 17:09:38 2022

@author: utku
"""

Not = int(input()) #number of tasks(n)

tasks = [] #define tasks array
temp = [0,0,0]

for i in range(Not):
    rawInput = input() #our input like "1 2 3"
    Input = rawInput.split() #our input like ['1','2','3']
    tasks.append(Input.copy())

for i in tasks: #char to int
    i[0] = int(i[0])
    i[1] = int(i[1])
    i[2] = int(i[2])

maxDeadline = 0

for i in tasks: #find max deadline
    if i[1] > maxDeadline:
        maxDeadline = i[1]
    
deadline = 0
tempId = -1
tempProfit = -1
isSpace = False #diff space hatalari icin

while 1:
    deadline += 1
    
    for i in tasks:
        #deadline uyan task secilir, önceki profit (varsa) kıyaslanır
        if (i[1] == deadline) and (i[2] > tempProfit):
            tempId = i[0]
            tempProfit = i[2]
            
    
    if tempId != -1:
        if isSpace:
            print(' ',end='')
        print(tempId,end='')
        isSpace = True
        
    tempId = -1
    tempProfit = -1
    
    if deadline == maxDeadline:
        break
    