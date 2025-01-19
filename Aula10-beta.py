#1.
lateral = float(input("Insira a lateral: "))
largura = float(input("Insira a largura: "))
area = lateral * largura
print(f"A area do campo é: {area}m².")

#alternativa:
lateral = float(input("Insira a lateral: "))
largura = float(input("Insira a largura: "))

def area(lateral, largura):
	return lateral * largura

print(f"A area do campo é: {area(lateral, largura)}m².")

#2.
l1 = float(input("L1:"))
l2 = float(input("L2:"))
l3 = float(input("L3:"))
triangulo = True

if (l1 > (l2+l3)):
	triangulo = False
elif (l2 > (l1+l3)):
	triangulo = False
elif (l3 > (l1+l2)):
	triangulo = False

if (triangulo == False):
	print("Não pode formar triangulo.")
else:
	print("Pode formar triangulo.")			

#alternativa:
l1 = float(input("L1:"))
l2 = float(input("L2:"))
l3 = float(input("L3:"))

def formaTriangulo(l1, l2, l3):
 if (l1 > (l2+l3)):
 	return False
 else:
 	return True	

if triangulo(l1, l2, l3) and triangulo(l2, l1, l3) and triangulo(l3, l1, l2):
	print("Pode formar triangulo.")
else:
	print("Não pode formar triangulo.")		

#alternativa2:
l1 = float(input("L1:"))
l2 = float(input("L2:"))
l3 = float(input("L3:"))

maior = max(l1, l2, l3)
2menores = l1+l2+l3-maior

if 2menores>maior:
	print("Forma triangulo")
else:
	print("Não forma.")	

#3.
n = int(input("Insira um inteiro: "))
contador = 0

if (n%2 == 0):
	contador += 1
if (n%3 == 0):
	contador += 1
if (n%5 == 0):
	contador += 1
if (n%7 == 0):
	contador += 1
print(f"O número {n} é divisivel por {contador} dos primos menores que 10.")

#alternativa:
#nem vale a pena


#4.
P1 = str(input("Nome 1: "))
P2 = str(input("Nome 2: "))
P3 = str(input("Nome 3: "))

acertou = True

if (P1 == "Huguinho" or P2 == "Huguinho" or P3 == "Huguinho"):
	if (P1 == "Zezinho" or P2 == "Zeziho" or P3 == "Zezinho"):
		if (P1 == "Luisinho" or P2 == "Luisinho" or P3 == "Luisinho"):
			acertou = True	

if ( (P1 == P2) or (P2 == P3) or (P1 == P3) ):
	acertou = False

if acertou == True:
	print("Acertou!")
else:
	print("Errou.")	

#alternativa
P1 = str(input("Nome 1: "))
P2 = str(input("Nome 2: "))
P3 = str(input("Nome 3: "))

nome = "Huguinho"
if P1 == nome or P2 == nome or P3 == nome:
	contador += 1
nome = "Zezinho"
if P1 == nome or P2 == nome or P3 == nome:
	contador += 1
nome = "Luisinho"
if P1 == nome or P2 == nome or P3 == nome:
	contador += 1

if contador==3:
	print("Acertou!")
else:
	print("Errou.")	

#5.
n1 = int(input("N1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))	

def Intervalo1(n):
	if n>=1 and n<=12:
		return True	
def Intervalo2(n):
	if n>=13 and n<=24:
		return True	
def Intervalo3(n):
	if n>=25 and n<=36:
		return True

def qtdIntervalo1(n1, n2, n3):
	contador1 = 0
	if Intervalo1(n1):
		contador1 += 1
	if Intervalo1(n2):
		contador1 += 1
	if Intervalo1(n3):
		contador1 += 1
	return contador1

def qtdIntervalo2(n1, n2, n3):
	contador2 = 0
	if Intervalo2(n1):
		contador2 += 1
	if Intervalo2(n2):
		contador2 += 1
	if Intervalo2(n3):
		contador2 += 1
	return contador2

def qtdIntervalo3(n1, n2, n3):
	contador3 = 0
	if Intervalo3(n1):
		contador3 += 1
	if Intervalo3(n2):
		contador3 += 1
	if Intervalo3(n3):
		contador3 += 1
	return contador3	

a = qtdIntervalo1(n1, n2, n3)
b = qtdIntervalo2(n1, n2, n3)
c = qtdIntervalo3(n1, n2, n3)

print(f"Dos números fornecidos ({n1}, {n2}, {n3}), {a} estão no primeiro intervalo, {b} estão no segundo intervalo e {c} estão no terceiro intervalo.")	
					