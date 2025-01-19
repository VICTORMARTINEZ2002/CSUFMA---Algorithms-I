#KAHOOT

#Questões Feitas pelo Professor:
#1132:
x = int(input())
y = int(input())

#menor = min(x,y)
#maior = max(x,y)

if x>y:
	x, y = y, x

soma = 0
for i in range(x,y+1):
	if i%13!=0:
		soma += i

print(soma)		

#1073(1):
n = int(input())
i = 1
while i<=n:
	if i%2==0:
		print(f"{i}^2 = {i*i}")	
	i += 1	

#1073(2):
n = int(input())
for i in range(2, n+1, 2):
	print(f"{i}^2 = {i*i}")

#1073(3):
n = int(input())
for i in range(1, n+1):
	if i%2==0:
		print(f"{i}^2 = {i*i}")

#1080(1):
i = 1
maior = 0
posMaior = 1
while i<=100:
	n = int(input())
	if i == 1:
		maior = n
	if n > maior:
		maior = n
		posMaior = i
	i += 1		
print(maior)
print(posMaior)
 
#1080(2):
maior = 0
posicao = 0

for i in range(100):
	n = int(input())

	if n>maior:
		maior = n
		posição = i+1
	
print(maior)
print(posicao)		

#OBS: aonde está o menor?
menor = int(input())
posicao = 1

for i in range(99):
	n = int(input())

	if n<menor:
		menor = n
		posição = i+2
	
print(menor)
print(posicao)	

#1078(1):
n = int(input())
i = 1
while i<=10:
	print(f"{i} x {n} = {i*n}")
	i += 1

###############################################################################################
#BEECROWD [UFMA_TREINO3]:
#1070:
x = int(input())
xi = x
while x<=xi+((6*2)-1):
	if x%2==1:
		print(x)
	x += 1	

#1070(prof):
x = int(input())

if x%2==0:
	x+=1

for i in range(6):
	print(x+2*i)		
#-------------------------------------------------------------------------
#1075:
n = int(input())
i = 1
while i<=10000:
	if i%n==2:
		print(n)
	i += 1

#1075(prof):
n = int(input())

for i in range(2, 10001, n):
	print(i)	
#----------------------------------------------------------------------------
#1113:
a = True
while a==True:
	x, y = map( int, input().split(" ") )
	if x == y:
		a = False
	if x>y:
		print("Decrescente")
	if y>x:
		print("Crescente")	

#1113(prof):
while True:
	x, y = map(int, input().split())
	if x > y:
		print("Decrescente")
	elif x < y:
		print("Crescente")
	else:
		break	
#---------------------------------------------------------------------------------		
#1116:
n = int(input())
i = 1
while i<=n:
	x1, y1 = map( int, input().split(" ") )
	if y1 == 0:
		print("divisao impossivel")
	else:
		div = x1/y1
		print(f"{div:.1f}")	
	i += 1
#-----------------------------------------------------------------------------
#1146:
a = True
while a:
	n = int(input())
	if n==0:
		a = False
	else:
		i = 1
		while i<=n:
			if i<n:
				print(f"{i}", end = " ")
				i += 1
			if i==n:
				print(f"{n}", end = "")
				i = n + 1
				print()
#--------------------------------------------------------------------------------

'''
#1151(1-Certo, mas fora do padrão beecrowd):
n = int(input())
a = 0 #recebe inicialmente fibonacci(1°)
b = 1 #recebe inicialmente fibonacci(2°)
c = 0 #será a nossa varialvel para o caso geral
pFib = 1
while pFib<=n:
		print(f"{pFib}° = {c}")
		a = b
		b = c
		c = a + b
		pFib += 1	
'''


#1151(for):
possiçãoFinal = int(input())
f1 = 0
f2 = 1
possiçãoAtual = 1

for possiçãoAtual in range(1, possiçãoFinal+1):
	if possiçãoAtual<possiçãoFinal:
		print(f1, end = " ")
		f1, f2 = f2, (f1+f2)	
	if possiçãoAtual==possiçãoFinal:
		print(f1) #Eu tinha feito print(f1, end = "") e dava presentation erro, eu errei essa questão 17 vezes pq euy sou burro;
		f1, f2 = f2, (f1+f2)

#1151(minha)
possiçãoFinal = int(input())
f1 = 0
f2 = 1
possiçãoAtual = 1

for possiçãoAtual in range(1, possiçãoFinal+1):
	if possiçãoAtual<possiçãoFinal:
		print(f1, end = " ")
		f1, f2 = f2, (f1+f2)	
	if possiçãoAtual==possiçãoFinal:
		print(f1) #Eu tinha feito print(f1, end = "") e dava presentation erro, eu errei essa questão 17 vezes pq euy sou burro;
		f1, f2 = f2, (f1+f2)

#1151(andrei que me deu essa moral e me mandou o dele.)
n = int(input())
numero = 0
ultimo = 1
variavel = "0"
while n>1:
	n -= 1
	numero += ultimo
	ultimo=numero-ultimo
	variavel += f" {numero}"
print(variavel)

#1151(prof):
n = int(input())
proximo, anterior = 0, 1
for i in range(1,n):
	print(proximo, end=" ")
	proximo, anterior = proximo+anterior, proximo
print(proximo)	
#-------------------------------------------------------------------------------------------------------------------------------------
#1153:
n = int(input())

def Fatorial(n):
	fatorial = 1
	i = 1
	while i<=n:
		fatorial = fatorial*i
		i += 1
	return fatorial
		
print(Fatorial(n))




#1165:
n = int(input())

def ehPrimo(n):
	i = 2
	while i<n:
		if n%i==0:
			return False
		i += 1
	return True

j = 1
while j<=n:
		a = int(input())
		if ehPrimo(a)==True:
			print(f"{a} eh primo")
		else:
			print(f"{a} nao eh primo")
		j += 1		
	
















