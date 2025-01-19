x = 12
a, b = 12, `carlos`

w=x==12
w = (x==12)
print(w) # True

a=b=12
prinit(a, b) #12 12
print(a=35)  #Erro

line = input()
input() #Recebe uma entrada e descarta ela;
#--------------------------------------------------------------
PODEMOS ESCREVER IF SEM COMPARAÇÕES, USANDO APENAS A VARIAVEL
#Só esses 3 valores resultam em falso:
False #Bool
None
0     #(zero inteiro)
0.00  #(zero em ponto flutuante)
""    #(str vazia)
#cada tipo tem o seu falso;
 
w = 2022 (int) #O if resulta em True, pois não é nem False nem None nem Zero; 
if w: 
	print("Carlos")
else:
	print("UFMA")	

w = 0
if w:   #mesma coisa que: if w!=0:
	print("não-nulo")
else:
	print("Zero ou nulo")

w = -10.50 #ponto flutuante
if w: #True
	print("não-nulo")
else:
	print("Zero ou nulo")

w = "" #String vazia
if w: #False
	print("não-nulo")
else:
	print("Zero ou nulo")	

#--------------------------------------------------
#TECNICA DE FLAG:
a = int(input())	
b = int(input())	
c = int(input())

def somentePares(a, b, c):
	flag = True	
#Começa com uma bandeira levantada ou abaixada;
#Se um if meu encontrar um impar:
#Eu mudo a bandeira pra falso permanentemente;
	if a%2==1:
		flag = False
	if b%2==1:
		flag = False
	if c%2==1:
		flag = False
	return flag			
#Alternativa:
def somentePares(a, b, c):
	return (a%2==0 and b%2==0 and c%2==0)	

#Exemplo 2 com flag:
def peloMenosUmDivisivelPor7(a, b, c):
	return (a%7==0 or b%7==0 or c%7==0)

def peloMenosUmDivisivelPor7(a, b, c):
	flag = False
	if a%7==0:
		falg = True
	if b%7==0:
		falg = True
	if c%7==0:
		falg = True
	return flag

def peloMenosUmDivisivelPor7(a, b, c):
	if a%7==0:
		return True
	if b%7==0:
		return True
	if c%7==0:
		return True
	return False	


#TECNICA DE CONTADORES:

def quantoPares(a, b, c):
	if 		a%2==0 and b%2==0 and c%2==0:
		return 3
	elif if a%2==0 and b%2==0 and c%2==1:
		return 2
	elif if a%2==0 and b%2==1 and c%2==0:
		return 2
	elif if a%2==1 and b%2==0 and c%2==0:
		return 1
	elif if a%2==0 and b%2==1 and c%2==1:
		return 1
	elif if a%2==1 and b%2==0 and c%2==1:
		return 1
	elif if a%2==1 and b%2==1 and c%2==0:
		return 1
	elif if a%2==1 and b%2==1 and c%2==1:
		return 0										

def quantosPares(a, b, c):
	contador = 0
	if a%2==0:
		contador = contador + 1 #incrementando
	if a%b==0:
		contador += 1
	if a%b==0:
		contador += 1			
	return contador	

def quantosPares(a, b, c):
	impares = a%2 + b%2 + c%2
	return 3 - impares

def quantosPares(a, b, c):
	return 3 - (a%2 + b%2 + c%2)


n1 = int(input())	
n2 = int(input())	
n3 = int(input())

#Caso mais geral
def quantosDivisiveisPorN(n, a, b, c):
	contador = 0
	if a%n==0:
		contador = contador + 1 #incrementando
	if a%n==0:
		contador += 1
	if a%n==0:
		contador += 1			
	return contador	

print( quantosDivisiveisPorN(2, n1, n2, n3))				

#BUG DO MILENIO:
AAMMDD
780810

991231 31 de dezembro de 1999

000101 01 de janeiro  de 2000 (voltar 99 anos no tempo?!)

atualizar o ano pra 4 digitos:
AAAAMMDD




