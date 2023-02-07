#Mehmet Utku Balikci 19290293

licenses = []
n = 0

#Input
while True:
    try:
        license = input()
    except EOFError:
        break
    n += 1
    license = license.split()
    license[0] = int(license[0])
    license[1] = int(license[1])
    licenses.append(license)

#greedy approach we buy first the most expensive license

#bubble sorting alghoritm
#Time complexity O(n^2)
for i in range(0,n):
    for j in range(0,n-i-1):
        if licenses[j][1] < licenses[j+1][1]:
            licenses[j],licenses[j+1] = licenses[j+1],licenses[j]

isntFirst = True

#print
for i in licenses:
    if isntFirst:
        isntFirst = False
    else:
        print(" ",end="")
    print(i[0],end="")

#end of file \n
print("")



