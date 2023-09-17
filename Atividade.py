import math

# dar entrada nos valores de a, b e n. Pedido no comando da questão
a = int (input("Insira o valor de a: "))
b = int (input("Insira o valor de b: "))
n = int (input("Insira o valor de n: "))

# atribuindo o valor de k = 0 para utilização do teorema binomial
k = 0

# criando variavel n - k para utilização na formula de analise combinatoria
nkfato = math.factorial(n - k)

#fazendo primeira parte da formula com n fatorial dividido por k fatorial
comb = math.factorial(n)/math.factorial(k)
#segunda parte da formula de analise combinatoria com o resultado dividido por n - k fatorial
final = comb / nkfato

# Resultado abaixo da formula de analise combinatoria
#print( 'Valor da combinação é: ', final)

#fazendo formula dos binomios: resultado da formula de analise * 'a' elevado a 'k' e 'b' elevado a 'n - k'
Binomio = final * pow(a, k) * pow(b, n - k)

print( 'O valor do Teorema Binomial é: ', Binomio)

#Letra B
p2 = a + b
result = pow(p2, n)
# ^ == elevado
print('O resultado de a + b^n é: ', result)

#Comparando:
print('Os resultados foram: ', Binomio,'e', result)