import math

#definindo variaveis
a = int (input("Insira o valor de a: "))
b = int (input("Insira o valor de b: "))
n = int(input("Insira o valor de n: "))
k = int(input("Insira um valor k: "))

k1 = n + 1
nkfato = math.factorial(n - k)

#formula fatorial
comb = math.factorial(n)/math.factorial(k)
final = comb / nkfato
Binomio = final * pow(a, n - k) * pow(b, k)

#definindo condições 
if n < 0:
    print("Insira um valor maior que zero! ")

if k < 1:
    print("Obedeça a realação k > 0 ")

if k > k1:
    print("Insira um valor menor que: ", k1)

#imprimindo valor
print( 'Valor da combinação é: ', final)
print( 'O valor do Teorema Binomial é: ', Binomio)
