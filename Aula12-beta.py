#OBS: COMPUTAÇÃO: COMPUTACIONALMENTE INTRATAVEL.
#	  MATÉMATICA: INSOLUVEL.	
#print("aaa", end="" & sep(sep ele n ensinou, mas os alunas comentaram sobre))
#IMPRIMIR ALGO E NÃO PULAR A LINHA: 
print("calos", end="")
print("calos", end="\n")
#Revisão pós-prova
x = 234
x = 'carlos'

n= input()
print(n)

if n=="senha":
	print("abre-te sesamo")

#Revisão WHILE (Laços de repetição)
i = 1
while <=100:
	print(i)
	i = i+1	

#Laços dentro de Laços de repetição

#Imprimir 1, 1-2, 1-3, 1-4, ..., 1-10;
i = 1
while i<=10:
	j = 1
	while j<=i:
		print(j)
		j = j + 1
	
	i = i+1	

#Imprimindo 1, 22, 333, 4444, ..., 10(10 vezes)
i = 1
while i<=10:

	j = 1
	while j<=i:
		print(i)
		j += 1

	print()
	i += 1	

#IMPRIMIR ALGO E NÃO PULAR A LINHA:
 print("calos", end="")

#Imprimir de 1 a 10 e colocar todos os divisores do número quando for impresso
'''
1: 1 (1 divisor(es))
2: 1 2 (2 divisor(es))
3: 1 3 (2 divisor(es))
4: 1 2 4 (3 divisor(es))
.
.
.
100: 1 2 4 5 10 20 25 50 100 (9 divisor(es))
'''	

i = 1
while i <= 10:
	print(f"{i}: ", end=" ")

	j = 1
	divisores = 0
	while j<=i:
		if i%j == 0:
			print(j, end="; ")
			divisores += 1
		j += 1	
	print(f"divisor(es) = {divisores}")
	print()	

	i += 1

#COMANDO NOVO: for
 #problemas com o while: te deixa muito exposto a loops infinitos
 i = 100
 while i>=1:
 	print(i)
 	i += 1

i = 100
while i>=1:
	if i%2==1:
		print(i)
		i -= 1 	

#for variavel in range(inicialização, comparador, incrento)
#for variavel in range(inicialização, limite superior(parada), incremento)
#Imprime
for i in range(99, 0, -2):
	print(i)

#Vantagens do while sobre o for:
#O usuario digita números, e só para quando digitar 2 números seguidos
#ALT1
anterior = None
while True:
	n = int(input())

	if n==anterior:
		print("Igual ao anterior!")
		break #Quebra o Loop e segue em frente

	anterior = n	

#ALT2
anterior = None
n = int(input("Informe um inteiro: "))

while n!=anterior:
	anterior = n
	n = int(input("Informe um inteiro: "))
print("Igual ao anterior!")
	

	anterior = n

#Imprimir os números de 1a100
for i in range(1, 101, 1):
	print(i)

for i in range(1, 101): #Assume que o valor do incremento é 1.

for i in range(100):    #Assume que o valor parametro inicial é 0
	print(i)   #Vai de 0 a 99
	print(i+1) #Vai de 1 a 100

for i in range(20):
	print("UFMA") #Imprime UFMA 20x	

#Imprimir os Pares:
for i in range(2, 101, 2):
	print(i)

#Imprimir os Impas:
for i in tange(1, 101, 2):
	print(i)	

#Imprimir 1, 1-2, 1-3, ..., 1-100
for i in range(1, 101):
	for j in range(1, i+1):
		print(j)
	print()	

#Imprimir:
#
##
###
####
...
###### 10 vezes

#ALT1
for i in range (1, 11, 1):
	print(i*"#")

#ALT2
for i in range (1, 11, 1):
	print(f"{i}: ", end="")
	for j in range (1, i+1, 1):
		print("#", end="")
	print()

#ALT3
for i in range(1, 11):
	for j in range(1, i+1):
		print("#", end="")
	print()		

#BEECROWN 1065	
pares = 0
for i in range(5):
	n = int(input())
	if n%2==0:
		pares += 1
print(f"{pares} valores pares")		

#BEECROWN 1071
x = int(input())
y = int(input())
menor = min(x,y)
maior = max(x,y)
soma = 0

for i in range(menor+1, maior):
	if i%2==1:
		soma += i
print(soma)		




