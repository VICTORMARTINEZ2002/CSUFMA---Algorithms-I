#vetores - mesma complexidade de acesso
v = [1, 2, 3]
print(v) #[1, 2, 3]

for i in range(4, 101):
	v.append(i)
print(v) #[1, 2, 3, ...,100]

print(v[10:15]) #[11, 12, 13, 14, 15]


#matrizes - vetores de vetores
m = [[1, 2, 3], [4, 5, 6]]

# criando matriz 20x30
m = []
num = 1
for i in range(20):
	m.append( [] )
	for j in range(30):
		m[i].append(num)
		num += 1

# interando sobre uma matriz
	linhas = len(m)
	colunas = len(m[0])
	# interando pela linha  (mostra todos os elementos linha por linha)
	for i in range(linhas):
		for j in range(colunas):
			print(m[i][j])		

	# interando pela coluna (mostra todos os elementos coluna por coluna)		
	for j in range(colunas):
		for i in range(linhas):
			print(m[i][j])

def contaFinal7(mat):
	cont = 0
	for  i in range(len(mat)):
		for j in range(len(mat[0])):
			if mat[i][j]%10==7:
				print(mat[i][j])
				cont += 1
	return cont

print( contaFinal7(m))		

#-------------------------------------------------------------------------------------------#
from random import randint

v = [23, 45, 67, 98, 34]

m = []
for i in range(8):
	m.append([])
	for j in range(6):
		m[i].append(randint(1, 100))

def contaVetorNaMatriz(vetor, matriz): #minha versão
	cont = 0
	b = []
	for i in range(len(matriz)):
		for j in range(len(matriz[0])):
			for k in range(len(vetor)):
				if m[i][j] == v[k]:
					if v[k] in b:
						pass
					else:	
						b.append(v[k])
						cont += 1
						print(i, j, k)				
	return cont
print(contaVetorNaMatriz(v, m))		

def contaVetorNaMatriz(v, m): #prof
	contador = 0
	#for k in range(len(v)):					#itero sobre vetor v
	#	elemento = v[k]
	for elemento in v:
		achou = False
		for i in range( len(m) ):
			for j in range ( len(m[i]) ):
				if m[i][j]== elemento:
					achou = True
		if achou:
			contador += 1
	return contador					

#--------------------------------------------------------------------------------
#SERIE DE COLLATZ
#Proximo(n):
#	n/2, se n for par
#	3*n + 1, se n for ímpar
# A serie sempre converge pra 1
#7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
#5 16  8  2  1
#3 10  5 16  8 4 2 1	

# Imprime a sequencia de collatz
m = []
for i in range(50):
	m.append([])
	m[i].append(i+1)

	while m[i][-1] != 1:           #Se o ultimo elemento diferente 1:
		if m[i][-1]%2 ==0:
			prox = (m[i][-1])//2
		else:
			prox = 3*m[i][-1] + 1
		m[i].append(prox)

for indice, linha in enumerate(m):
	print(indice+1, linha)		
#---------------------------------------------------------------------------------#
			





