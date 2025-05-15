n = input()

L = []


for i in range(len(n)) :
    r = int(n[i])
    c = 0

    for k in range(2, r) : 

        if r % k == 0 :
            c += 1
    
    if c == 0 and r != 1 and r != 0 : 
        L.append(r)

L.sort()
print(L)