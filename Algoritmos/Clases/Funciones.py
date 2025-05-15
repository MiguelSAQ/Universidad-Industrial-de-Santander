def factorial(n) :
    i = 1
    fact = 1
    while i <= n : 
        fact *= i
        i += 1
    return fact

m = 3
k = 2

numero_comb = (factorial(m) / (factorial(k) * factorial(m-k)))
print(numero_comb)