airports = input().split()
airportCount = len(airports)

graph = [[0 for _ in range(airportCount)] for _ in range(airportCount)]  # define graph[a][a]

for i in range(airportCount):  # O(n^2)
    temp = input().split()
    temp = list(map(int, temp))
    for j in range(airportCount):
        graph[i][j] = temp[j]

minDistance = -1
shortestPath = []


def shortestWay(start, finish, path, distance):
    global minDistance
    global shortestPath
    global airports
    global airportCount
    global graph
    for i in range(airportCount):

        if graph[i][start] == 0:
            continue

        elif len(path) > 3:
            continue

        elif i in path:
            continue

        else:
            distance += graph[i][start]
            path.append(i)

            if i == finish:
                if minDistance == -1:
                    minDistance = distance
                    shortestPath.clear()
                    shortestPath = path.copy()

                elif distance < minDistance:
                    minDistance = distance
                    shortestPath.clear()
                    shortestPath = path.copy()
            else:
                shortestWay(i, finish, path, distance)

            distance -= graph[i][start]
            path.remove(i)


while True:
    try:
        cities = input().split()
    except EOFError:
        break

    shortestWay(airports.index(cities[0]), airports.index(cities[1]), [airports.index(cities[0])], 0)
    _isFirst = True
    for i in shortestPath:
        if _isFirst:
            _isFirst = False
        else:
            print(" ", end="")
        print(airports[i], end="")
    print("")

    minDistance = -1
    shortestPath = []
