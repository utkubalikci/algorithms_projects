# Mehmet Utku Balikci 19290293
frogA = input().split()
frogB = input().split()

for i in range(len(frogA)):
    frogA[i] = int(frogA[i])
for i in range(len(frogB)):
    frogB[i] = int(frogB[i])

lenA = len(frogA)
lenB = len(frogB)

distances = [[0 for _ in range(lenB)] for _ in range(lenA)]  # define distances[lenA][lenB]

for i in range(lenA): # Big-Oh O(mn)
    for j in range(lenB):
        distances[i][j] = abs(frogA[i] - frogB[j])


a = 0
b = 0

if distances[0][0] > 100:
    print("false",end="")
else:
    while 1: # Dynamic programming, we are studying with arrays
        isMooved = False

        if a == lenA-1 and b == lenB-1:
            print("true",end="")
            break
        if a < lenA-1:
            if distances[a+1][b] <= 100:
                a += 1 # jump A
                isMooved = True
        if b < lenB-1 and isMooved == False:
            if distances[a][b+1] <= 100:
                b += 1 # Jump B
                isMooved = True
        if isMooved == False: # if both frog cannot jump false
            print("false",end="")
            break