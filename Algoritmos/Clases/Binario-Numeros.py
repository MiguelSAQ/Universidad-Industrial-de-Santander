n = int(input(""))
c = 0
R = 1
Num = 0
i = 0

while n != 0:
    R = n % 2
    n //= 2
    Num += R*10**i 
    i += 1

print(Num)
print(i)