COSMOS: COMANDO CONDICIONAL SE:
MAÇA E BANANA:
soma = int( input() )
subt = int( input() )

#soma = apple + banan
#subt = banan - apple
banan = (soma + subt)//2
apple = soma - banan
print(apple)

PAR OU IMPAR:
n = int(input())
print(n%2)

AREA DE UM RETANGULO:
base = int(input())
altura = int(input())
area = base*altura
print(area)

BONUS SALARIAL:
salario = float(input())
aumento = 0

if salario<=800.00:
	aumento = 15
elif salario<=1500.00:
	aumento = 12
elif salario<=2000.00:
	aumento = 8
else:
	aumento = 6

bonus = (salario * aumento)//100

print("{:.2f}".format(bonus))
print(f"{bonus:.2f}")

MAIOR 3 INTEIROS:
n1 = int(input())
n2 = int(input())
n3 = int(input())
print(max(n1,n2,n3))

Informando a senha:
senha = input()
if senha == "ufma":
	print("Ok")
else:
	print("Senha Errada")	

IMPARES:
n1 = int(input())
n2 = int(input())
n3 = int(input())
contador = 0

if n1%2 == 1:
	contador = contador + 1
if n2%2 == 1:
	contador = contador + 1
if n3%2 == 1:
	contador = contador + 1
print(contador)	

2 INTEIROS EM ORDEM CRESCENTE:
n1 = int(input())
n2 = int(input())

print((n1+n2)-max(n1,n2))
print(max(n1,n2))

MAIOR INTEIRO:
n1 = int(input())
n2 = int(input())

print(max(n1,n2))

#########################################################################################################################################################
COSMOS: VARIAVEIS E ATRIBUIÇÕES:
DOBRO DE UM NUMERO:
n = int(input())
print(2*n)

FALANDO, FALANDO, FALANDO:
stringInformada = input()
print(3*stringInformada)

AREA DE UM TRIANGULO REAL:
b = float(input())
h = float(input())
a = b*h
print("{:.1f}".format(a))

OLA, MUNDO:
print("Hello World!")

MAÇAS, LARANJAS E BANANAS:
sml = int(input())
smb = int(input())
slb = int(input())



#sml = m + l
#smb = m + b
#slb = l + b
somaTotal = (sml+smb+slb)//2


l = (sml + slb - smb)//2
m = sml - l
b = smb - m

print(m)
print(l)
print(b)

MEIDA DE GOLS:
gf = int(input())
gs = int(input())

sg = gf-gs
msg = sg/38

print("{:.2f}".format(msg))

################################################################################################################################################
COSMOS: Laçõs de repetição: (Eu fiz mas o prf ainda n ensinou)
IMPARES SEQUENCIAIS:
n1 = int(input())
n2 = int(input())
menor = n1 + n2 - max(n1,n2)
maior = max(n1,n2)
somaImpares = 0

while (menor+1)<maior:
	if (menor+1)%2 == 1:
		somaImpares += (menor+1)
	menor += 1
print(somaImpares)	

IMPARES SEQUENCIAIS:
n1, n2 = int(input()), int(input())
soma = 0
for n in range(n2,n1):
	if n%2 == 1:
		soma += n
print(soma)	

QUANTIDADE DE PARES_1:
pares = 0
soma = 0
for i in range(0,10):
	n = float(input())
	if n%2==0:
		pares += 1
		soma += n
print(f"{pares} {int(soma)}")		


QUANTIDADE DE PARES_2:
n0 = int(input())
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
n6 = int(input())
n7 = int(input())
n8 = int(input())
n9 = int(input())
maior = max(n0,n1,n2,n3,n4,n5,n6,n7,n8,n9)
contador  = 0
somaPares = 0

if n0%2 == 0:
	contador  += 1
	somaPares += n0
if n1%2 == 0:
	contador  += 1
	somaPares += n1
if n2%2 == 0:
	contador  += 1
	somaPares += n2
if n3%2 == 0:
	contador  += 1
	somaPares += n3
if n4%2 == 0:
	contador  += 1
	somaPares += n4
if n5%2 == 0:
	contador  += 1
	somaPares += n5
if n6%2 == 0:
	contador  += 1
	somaPares += n6
if n7%2 == 0:
	contador  += 1
	somaPares += n7
if n8%2 == 0:
	contador  += 1
	somaPares += n8
if n9%2 == 0:
	contador  += 1
	somaPares += n9

print(contador, somaPares)

print("{} {}".format(contador, somaPares))																				

TRÊS INTEIROS EM ORDEM CRESCENTE:
n1 = int(input())
n2 = int(input())
n3 = int(input())
maior = max(n1,n2,n3)
menor = min(n1,n2,n3)
meio = (n1+n2+n3)-(maior+menor)

print(menor)
print(meio)
print(maior)	

TRÊS INTEIROS EM ORDEM CRESCENTE:
n1 = int(input())
n2 = int(input())
n3 = int(input())

def maior(n1,n2,n3):
	if ( (n1>=n2) and (n1>=n3) ):
		return n1
	elif ( (n2>=n1) and (n2>=n3) ):
		return n2
	else:
		return n3	
		
def menor(n1,n2,n3):
	if ( (n1<=n2) and (n1<=n3) ):
		return n1
	elif ( (n2<=n1) and (n2<=n3) ):
		return n2
	else:
		return n3		

meio = (n1+n2+n3) - ( menor(n1,n2,n3) + maior(n1,n2,n3) )
print(menor(n1,n2,n3))
print(meio)
print(maior(n1,n2,n3))

TRES INTEIROS EM ORDEM CRESCENTE:
n1 = int(input())
n2 = int(input())
n3 = int(input())

if ( (n1>=n2) and (n1>=n3) ):
	maior = n1
elif ( (n2>=n1) and (n2>=n3) ):
	maior = n2
else:
	maior = n3

if ( (n1<=n2) and (n1<=n3) ):
	menor = n1
elif ( (n2<=n1) and (n2<=n3) ):
	menor = n2
else:
	menor = n3

meio = (n1+n2+n3) - ( menor + maior )

print(menor)
print(meio)
print(maior)

QUANTOS MULTIPLOS DE 7?
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
contador = 0

if n1%7==0:
	contador += 1
if n2%7==0:
	contador += 1
if n3%7==0:
	contador += 1
if n4%7==0:
	contador += 1			
print(contador)

#################################################################################################################################
VETORES E LISTA:

SEQUENCIA ORDENADA AO QUADRADO:
n = int(input())
l = []
for i in range(0, n):
	num = int(input())
	num = num**2
	l.append(num)
l=sorted(l)
for i in range (0,len(l)):
	print(l[i])	

TRANSFORMAÇÃO NO VETOR:
n = int(input())
v=[]
for i in range (0,n):
	num = int(input())
	v.append(num)
for i in range(0,len(v)):
	if v[i]%2==0:
		v[i]=2*v[i]
	else:
		v[i]=3*v[i] -1
print(v)

SOMA DE VALORES REAIS:
n = int(input())
soma=0
v=[]
for i in range(0,n):
	v.append(int(input()))
for num in v:
	soma += num
print(soma)		