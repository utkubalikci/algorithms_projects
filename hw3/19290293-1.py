# 19290293 Mehmet Utku Balikci

def maxFunc(a, b):
    if a > b:
        return a
    else:
        return b


inputs = input().split()
n = int(inputs[0])  # floor
m = int(inputs[1])  # ball

floors = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # define floors[m+1][n+1]

max = 999999

for i in range(1, m + 1):
    floors[i][0] = 0  # if 0 floor -> 0 try
    floors[i][1] = 1  # if 1 floor -> 1 try

for i in range(1, n + 1):
    floors[1][i] = i  # if 1 ball -> n try

if n == 1 or n == 0:
    print(n, end="")

elif m == 1:
    print(n, end="")

else:  # dynamic programming O(m * n^2)
    for i in range(2, m + 1):
        for j in range(2, n + 1):
            floors[i][j] = max
            for k in range(1, j + 1):
                result = maxFunc(floors[i - 1][k - 1], floors[i][j - k]) + 1
                if result < floors[i][j]:
                    floors[i][j] = result
    print(floors[m][n], end="")
