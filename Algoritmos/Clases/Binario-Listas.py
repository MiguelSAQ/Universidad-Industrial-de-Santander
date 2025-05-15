n = int(input(""))
c = 0
R = 1
Lista = []
Num = ""

while n != 0:
    R = n % 2
    n //= 2
    Num = str(R) + Num

print(Num)
print(len(Num))