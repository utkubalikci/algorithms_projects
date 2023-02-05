# -*- coding: utf-8 -*-
#sıra fonksiyonları için kütüphane
import queue as q


# tek cember varsa true donduren bir fonksiyon
def hasOddCycle(G, s, V): #G graf s source, başlanacak node hangisi oldugu fark etmez V Vertices köse sayısı
    # köşelerin rengini tutacak bir array oluşturdum
    colors = ['b'] * V #beyaz atadik hepsine
    colors[s] = 'g' #s.color <- gray

    Queue = q.Queue() #initialize an empty queue Q
    Queue.put(s) #Enqueue(Q,s)

    while (Queue.empty() == 0): #while Q is not empty

        u = Queue.get() #u = Dequeue(Q)

        # eger bir kenar kendisinden kendisine yola sahipse odd cycle vardır
        if (G[u][u] == 1):
            return "true"

        for v in range(V): #komsu köseleri bulacagiz
            if (G[u][v] and colors[v] == 'b'): #u'dan v'ye yol varsa ve v beyaz ise
                if colors[u] == 'g':
                    colors[v] = 's'
                else:
                    colors[v] = 'g'
                Queue.put(v) #Enqueue(Q,v)
            #eger u ile v aynı renkte ise ve aralarında yol varsa true
            elif (colors[v] == colors[u] and G[u][v]):
                return "true"

    return "false"

V = int(input())
G = []

for i in range(V):
    inp = input()
    inp = inp.split()
    for j in range(V):
        inp[j] = int(inp[j])
    G.append(inp)

print(hasOddCycle(G, 0, V),end="")