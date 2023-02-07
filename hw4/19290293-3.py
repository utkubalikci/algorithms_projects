temp = input().split()
graphLen = len(temp)

graph = [[0 for _ in range(graphLen)] for _ in range(graphLen)]  # define graph[a][a]

temp = list(map(int, temp))
for j in range(graphLen):
    graph[0][j] = temp[j]

for i in range(1,graphLen):  # O(n^2)
    temp = input().split()
    temp = list(map(int, temp))
    for j in range(graphLen):
        graph[i][j] = temp[j]

tree = []

def move(node):
    global tree
    
    if node not in tree:
        tree.append(node)

    minW = 0
    minI = 0
    for i in range(graphLen):
        temp = graph[node][i]
        if  temp == 0:
            continue
        elif minW == 0 and i not in tree:
            minW = temp
            minI = i
        elif temp < minW and i not in tree:
            minW = temp
            minI = i
    if len(tree) == graphLen:
        return
    elif minI != 0:
        move(minI)
    else:
        move(tree[tree.index(node)-1])


move(0)

_isFirst = True
for i in tree:
    if _isFirst:
        _isFirst = False
    else:
        print(" ", end="")
    print(i, end="")
print("")

