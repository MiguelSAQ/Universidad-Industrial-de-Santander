n = input()

# Con cadenas

m = ""

for i in range(0, len(n)-1) :
    m += n[i] + "0" 

m = m + n[len(n)-1]

print(m)

# Con numeros 

n = int(n)

num = []
c = 0

while n > 0:
    r = n % 10
    n //= 10
    num.append(r)

for i in range(len(num)-1, -1, -1) :
    c = c*100 + num[i]

print(c)