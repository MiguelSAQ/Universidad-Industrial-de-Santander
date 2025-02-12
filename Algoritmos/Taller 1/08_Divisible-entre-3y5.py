print("Números divisibles por 3 y/o 5")
n = int(input("Revisar desde el 1 hasta el: "))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}. Es divisible por 3 y 5.")
    elif i % 3 == 0:
        print(f"{i}. Es divisible por 3.")
    elif i % 5 == 0:
        print(f"{i}. Es divisible por 5.")
    else:
        print(f"{i}.")