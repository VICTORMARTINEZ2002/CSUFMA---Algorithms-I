import random #importar biblioteca random,

#cria um vetor de len tamanho, com números, aleatorios no intervalo[menor, maior]
def criaVetor(tamanho, menor, maior):
	v = []
	for i in range(tamanho):
		v.append(random.randint(menor,maior))
	return v	

#criar uma matriz 40x50 c/ n° aleatorios de 1-1000;
def criaMatriz():
	mat = []
	for i in range(40):
		linha = []
		for j in range(50):
			linha.append(random.randint(1, 1000))
		mat.append(linha)
	return mat

def criaMatriz():
	mat = []
	for i in range(4):
		mat.append(criaVetor(5, 1, 1000))			

mat = criaMatriz()

#soma todos os numeros pares e retornar o resultado dessa soma
def somaPares(mat):
	for i in range(len(mat)):        #linhas = len(mat)
		for j in range(len(mat[0])): #colunas= len(mat[0])
			if mat[i][j]%2==0:
				soma += mat[i][j]
	return soma
	




def somaDiagonalPrincial(mat): #melhor
	soma = 0
	for i in range(len(mat)):
		soma += mat[i][i]
	return soma	
	
def somaDiagonalPrincial(mat):
soma = 0
for index_linha, linha in enumerate(mat):
	for index_coluna, elemento in enumerate(linha):
		if index_linha == index_coluna:
			soma += elemento
return soma

def somaDiagonalPrincial(mat):
	for i in range(len(mat)):
	    for j in range(len(mat[0])):
	        if i == j:
	            soma += mat[i][j]
	return soma





def somaAbaixoDiagonalPrincipal(mat):
	soma = 0
	for i in range(len(mat)-1):
		for j in range(len(mat)-i):
			soma += mat[j][j+i]

	return soma	

def somaAbaixoDiagonalPrincipal(mat):
  soma = 0
  for index_linha, linha in enumerate(mat):
    for index_coluna, elemento in enumerate(linha):
      if index_coluna < index_linha:
        soma += elemento
  return soma

def somaAbaixoDiagonalPrincipal(mat):
  	soma = 0
 	for i, linha in enumerate(mat):
    	for j, elemento in enumerate(linha
      		if i < j:
        		soma += elemento
    return soma 


#-------------------------------------------------------------------------#
T minutos sem interrupção
duração voo: D minutos
refeições q serão servidas: M
tempo da primeira refeição servido apos inicio do voo: yi

T, D, M = map(int, input().split(" "))

i=0
v = []
while i<=(M-1):
	v.append(0)
	v[i] = input(f"Minuto refeição número {i}: ")
	i += 1

def vooPerfeito(T, D, M, v):
	if v[0]>T:
		return True
	if D-v[M-1]>=T:
		return True
	i = 0
	while i<=(M-1):
		if v[i]-v[i-1]>=T:
			return True
		i += 1	
	return False

if vooPerfeito(T, D, M, v):
	print("S")
else:
	print("N")		

						












































