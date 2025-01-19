#AULA 6-beta
#1035
a, b, c, d = map(int, input().split(" "))
a = int(a)
b = int(b)
c = int(c)
d = int(d)
a_par = False

if((a%2) == 0):
	a_par = True	

if( (b>c) and (d>a) and ( (c+d)>(a+b) ) and (c>0) and (d>0) and (a_par == True) ):
	print("Valores aceitos")
else:
	print("Valores nao aceitos")	

#1037
n = float(input())
intervalo = "A"

if (n>=0 and n<=25):
	intervalo = "[0,25]"
elif (n>25 and n<=50):
	intervalo = "(25,50]"
elif (n>50 and n<=75):
	intervalo = "(50,75]"
elif (n>75 and n<=100):
	intervalo = "(75,100]"
else:
	print("Fora de intervalo")	

if(not intervalo == "A"):
	print(f"Intervalo {intervalo}")	

#1038
cdg, qtd = input().split(" ")
cdg = int(cdg)
qtd = int(qtd)
preço = 0
if (cdg == 1):
	preço = 4.0 * qtd
elif (cdg == 2):
	preço = 4.5 * qtd
elif (cdg == 3):
	preço = 5.0 * qtd
elif (cdg == 4):
	preço = 2.0 * qtd
elif (cdg == 5):
	preço = 1.5 * qtd
print(f"Total: R$ {preço:.2f}")		

#1042
a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
p1 = 0
p2 = 0
p3 = 0

if (a == max(a, b, c)):
	if(b == max(b,c)):
		p1 = a
		p2 = b
		p3 = c
	elif(c == max(b,c)):	
		p1 = a
		p2 = c
		p3 = b
elif (b == max(a, b, c)):
	if(a == max(a,c)):
		p1 = b
		p2 = a
		p3 = c
	elif(c == max(a,c)):
		p1 = b
		p2 = c
		p3 = a
elif (c == max(a, b, c)):
	if(a == max(a,b)):
		p1 = c
		p2 = a
		p3 = b
	elif(b == max(a,b)):
		p1 = c
		p2 = b
		p3 = a

print(p3)
print(p2)
print(p1)
print()	
print(a)
print(b)
print(c)	


#--------------------------------------------------------------------------------------------
#1042(professor resposta)
a, b, c = map(int, input().split())

if a<=b and a<=c:
	menor = a
elif b<=c:
	menor = b
else:
	menor = c

maior = a
if b>maior:
	maior = b
if c>maior:
	maior = c

meio = a + b + c -maior -menor

#ou

#if a>=menor and b<=maior:
#	meio = a
#elif b>=menor and b<=maior:
#	meio = b
#else:
#	meio = c

#ou

#meio = a
#if not(menor<=meio<=maior):
#	meio = b
#if not(menor<=meio<=maior):
#   meio = c

#insertsort
n1, n2, n3 = a, b, c
if n2<n1:
	n1, n2 = n2, n1
if n3<n1:
	n1, n3 = n3, n1	
if n3<n2:
	n2, n3 = n3, n2	

print(n1)
print(n2)	
print(n3)		

#alternativa 2(sem if)
p1 = min(a, b, c)
p2 = a+b+c-p1-p2
p3 = max(a, b, c)
#----------------------------------------------------------------------------------------

#1044
a, b = input().split(" ")
a = int(a)
b = int(b)
c = False

if (a>b):
	c = (a%b == 0)
elif (b>a):
	c = (b%a == 0)
else:
	c = True

if(c == True):
	print("Sao Multiplos")
else:
	print("Nao sao Multiplos")

#1044 - ALTERNATIVA:
if (a%b == 0) or (b%a == 0):
	print("Sao Multiplos")
else:	
	print("Não são multiplos")

#1052
if (n = 1):
  mes = "January"
elif (n = 2):
  mes = "February"
elif (n = 3):
  mes = "March"
elif (n = 4):
  mes = "April"
elif (n = 5):
  mes = "May"
elif (n = 6):
  mes = "June"
elif (n = 7):
  mes = "July"
elif (n = 8):
  mes = "August"
elif (n = 9):
  mes = "September"
elif (n = 10):
  mes = "October"
elif (n = 11):
  mes = "November"
else:
  mes = "December" 
print(mes)


#Os 2 ultimos exercicios são:
#Balança equilibrada(ja fiz quase sem o if)
#Paginas de um livro(ja fiz sem o if, foi chatinho...)
#Ambos estão na pasta do beecrowd