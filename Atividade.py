import math

a = 3
b = 1

n = int (input("Insira o valor de n: "))
p = int (input("Insira o valor de p: "))
npfato = math.factorial(n - p)


comb = math.factorial(n)/math.factorial(p)
final = comb / npfato
print( 'Valor da combinação é: ', final)

Binomio = final * pow(a, n - p) * pow(b, p)

print( 'O valor do Teorema Binomial é: ', Binomio)