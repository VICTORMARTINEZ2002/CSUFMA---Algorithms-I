#LAÇOS DE REPETIÇÃO:
#pega um trecho de codigo e faz ele ser executado uma certa qunatidade de vezes.
 x = 10
 if x>12:
 	print("Maior que 12")
 else:
 	print("Menor que 12")

#Laçoes de codigo tem 3 elementos principais:
#Inicialização;
#Comparação;
#Incremento;

#--------------------------------------------------------------------------------------#
ESCREVER OS NÚMEROS DE 1 A 100:
#ALT1:
print("1")
print("2")
...
print("100")

#ALT2:
 i = 1 		        #Inicialização

while i<=100:       #Comparação (Critério De Parada)
 	print(i)
 	i = i + 1       #Incremento
print("carlos", i)


IMPRIMIR SO OS PARES DE 1 A 100:
#ALT1-(Ruim):
i = 1
while i<=100: #while é repetido 100x
	if i%2==0:
		print(i)
	i = i+1	

#ALT2:
i = 2
while i<=100: #while é repetido 50x
	print(i)
	i = i + 2

	#OBS: Imprimir os impares de 1 a 100:
	i = 1
	while i<=100:
		print(i)
		i = i + 2	

	#OBS: ERRO!!!
	i = 1
	while i<=100 and i%2==0:
		print(i)
		i += 1

#Imprimir só os multiplos de 7 no intervalo [1;100]:
#ALT1:
i = 7
while i<=100:
	print(i)
	i = i + 7

#ALT2:
i = 1
while (i<=100):
	if (i%7==0):
		print(i)
	i = i + 1

#Imprimir de 100 até 1
i = 100
while i>=1:
	print(i)
	i = i - 1	

#Imprimir todos os pares de 100 até 1:
#ALT1:
i = 100
while i>=1:
	print(i)
	i = i - 2
#ALT2:
i = 100
while i>=1:
	if (i%2==0):
		print(i)
	i = i - 1

#OBS: Cuidado com a inversão do print com o contador:
i = 100
while i>=1:
	i = i - 2
	print(i)

# OBS: Cuidado para que não criar um LOOP INFINITO:
# A condição de parada nunca é atendida
i = 100
while j>=1:
	i = i - 2
	print(i)

i = 100
while i<=100:
	i = i - 1
	print(i)

# O contador foi esquecido
i = 100
while i>=1:
	print(i)


#Imprimir os primos de 1 a 100:
#raiz 100=10, os primos menos que 10 sao 2,3,5,7
#um primo até 100 n pode ser divisivel pelos primos menos que a raiz(100)=10

#ALT1:
i = 2
while i<=100:
	if i==2 or i==3 or i==5 or i==7:
		print(i)
	elif i%2!=0 or i%3!=0 or i%5!=0 or i%7!=0:
		print(i)
	i+=1

#CASO GERAL:
n = int(input())
def ehPrimo(n):
	i = 2
	while i<n:
		if n%i==0:
			return False
		i += 1
	return True

print(n, ehPrimo(n))	

#um aluno mencionou os numeros perfeitos.

#MELHORANDO
n = int(input())
def ehPrimo(n):
	if n<2:
		return False

	i = 2
	while i<n:
		if n%i==0:
			return False
		i += 1
	return True

print(n, ehPrimo(n))	

#melhorando aqui:
n = int(input())
def ehPrimo(n):
	if n<2:
		return False

	if n==2: 
		return True 
	if n%2==0: 
		return False

	i = 3
	while i<n:
		if n%i==0:
			return False
		i += 2
	return True

print(n, ehPrimo(n))

#MELHORANDO MAIS AINDA:
n = int(input())
def ehPrimo(n):
	if n<2:
		return False

	if n==2: 
		return True 
	if n%2==0: 
		return False

	i = 3
	while i*i<=n:
		if n%i==0:
			return False
		i += 2
	return True

print(n, ehPrimo(n))

while i<= 100000:
	if ehPrimo(i):
	print(i)
i += 1


#Explicação da divisão
#Para cada divisor i menor que a raiz quadrada, existe um recíproco num/i maior que a raiz quadrada.
12 = 1 * 12
12 = 2 * 6
12 = 3 * 4
12 = (12^0.5) * (12^0.5)
12 = 4 * 3
12 = 6 * 2
12 = 12* 1

2 numeoros > raiz(n) tq n1*n2=n (ABSURDO! Pois: raiz(n) * raiz(n) = n)

#crivo de erastotenes(é mais eficiente, mas só vamos ver isso quando o prof tiver falando de números primos)

primos = [2]

def ehPrimo(n): 
  if n%2==0:
    return n==2
  if n<2:
    return False
  for primo in primos:
    if n%primo==0:
      return False
    if primo*primo>n:
      return True
  return True

for i in range(2,100000):
  if ehPrimo(i):
    primos.append(i)
    print(i)

