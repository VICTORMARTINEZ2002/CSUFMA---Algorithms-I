def contaAprovados(v):
	contador = 0
	for nota in v:
		if nota >= 70:
			contador += 1
	return contador

def contaAprovados(v):
contador = 0
	for i in range(len(v)):
		if v[i] >= 70:
			contador += 1
	return contador	

#v1 e v2 são iguais em numeros de elementos
def somaDoisVetores(v1, v2): #meu, igual o gab
	vf = []
	for i in range(len(v1)):
		vf.append(v1[i]+v2[i])
	return vf

def somaDoisVetores(v1, v2): #Alternativa Ruim
	vf = []
	for pos, valor in enumerate(v1):
		for pos2, valor2 in enumerate(v1):
			if pos == pos2:
				soma = valor+valor2
				vf.append(soma)
	return vf			

#Tem uma matriz com booleanos, quero a soma dos True´s na diagonal principal
def somaVerdadeiro(m):  #minha
	diagonal_principal = []
	cont = 0
	for i in range(len(m)):
		diagonal_principal.append(m[i][i])
	for elemento in diagonal_principal:
		if elemento:
			cont += 1
	return cont	

def somaVerdadeiro(m): #gab
	contador = 0
	for i in range(len(m)):
		if m[i][i]==True:
			contador += 1
	return contador		

def somaVerdadeiro(m): #gab merda
	contador = 0
	for i in range(len(m)):
		for j in range(len(m[0])):
			if i==j and m[i][i]==True:
			contador += 1
	return contador								

#Crie uma função contaLinhasUFMA(m), que recebe como parâmetro uma matriz 40X60 de cadeias de caracteres.
# A função deve retornar como resultado quantas dessas 40 linhas (um inteiro de 0 a 40, inclusive) 
#da matriz m possui pelo menos uma ocorrência da cadeia de caracteres "UFMA".
def contaLinhaUFMA(m): #minha e eu entendi errado o q a questão queria...enfim, ta aqui
	cont = 0
	for i in range(len(m)):
		for j in range(len(m[i])):
			if m[i][j] = "U" and m[i][j+1] = "F" and m[i][j+2] = "M" and m[i][j+3] = "A":
				cont += 1
				pass
	return cont		

def contaLinhaUFMA(m):
	contadorLinhas = 0
	for linha in m:
		for elemento in linha:
			if elemento == "UFMA"
				contadorLinha += 1
				break	
	return contadorLinhas

def contaLinhasUFMA(m):
    contador = 0
    for linha in m:
        if "UFMA" in linha:
            contador += 1
    return contador				

#m 30x40
#v 50 inteiros
def verificaVetorNaMatriz(m,v): #minha
	elementos_apareceram = []
	for i in range(len(m)):
		for j in range(lem(m[j])):
			for k in range(len(v)):
				if v[k] == m[i][j] and v[k] not in elementos_apareceram:
					elementos_apareceram.append(v[k])
	for k in range(len(v)):
		if v[k] not in elementos_apareceram:
			return False
	return True					
					
def verificaVetorNaMatriz(m,v):
	for chave in v:
		achou = False
		for linha in m:
			if chave in linha:
				achou = True
				break
		if acho==False:
			return False
		return True			
