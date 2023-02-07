#Mehmet Utku Balikci 19290293
products = input()
products = products.split()
n = len(products)
for i in range(n):
    products[i] = int(products[i])

#buyukten kucuge siralayip en buyuk ciftleri almamiz lazim
#bubble sorting alghoritm
#Time complexity O(n^2)
for i in range(0,n):
    for j in range(0,n-i-1):
        if products[j] < products[j+1]:
            products[j],products[j+1] = products[j+1],products[j]

#print pairs
for i in range(0,len(products),2):
    print(str(products[i]) + " " + str(products[i+1]))