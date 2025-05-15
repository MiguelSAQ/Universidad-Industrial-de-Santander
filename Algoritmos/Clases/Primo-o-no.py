n = int(input("Numero: "))

for i in range(2, n):
    if (n % i) == 0:
        print(f"{n} no es primo")
        break
else:
    print(f"{n} es primo")
