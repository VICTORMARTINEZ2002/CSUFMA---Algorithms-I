def maiorElemento(v):
	maior = v[0]
	for elemento in meuVetor:
		if elemento>maior:
			maior = elemento
	return maior

def maiorElemento(v):
	return max(v)	

meuVetor = [1, 345, 56, 24, 324, 1243]
x = maiorElemento(meuVetor)


def somaPares(v): #Minha solução 1 (igual ao gabarito do prof)
	somaPar = 0
	for elemento in meuVetor:
		if elemento%2==0:
			somaPar += elemento
	return somaPar

def somaPares(v): #Minha solução 2
	somaPar = 0
	i = 0
	while i <= len(meuVetor):
		if elemento%2==0:
			somaPar += elemento
		i += 1	
	return somaPar
#------------------------------------------#
jogadas = [1, 4, 4, 5, 6, 3, 2]
def TodasJogadasDeDados(jogadas): #Retrona true se tem todos os númeors de 1-6
	tem1 = False
	tem2 = False
	tem3 = False
	tem4 = False
	tem5 = False
	tem6 = False
	for elemento in jogadas:
		if elemento==1:
			Tem1 = True
		if elemento==2:
			tem2 = True
		if elemento==3:
			tem3 = True
		if elemento==4:
			tem4 = True
		if elemento==5:
			tem5 = True
		if elemento==6:
			tem6 = True
	if tem1 and tem2 and tem3 and tem4 and tem5 and tem6:
		return True
	else:
		return False

print(todosDe1a6(dados))			

def TodasJogadasDeDados(v): #Gabarito do professor
	for i in range(1, 7):
		if i not in v: #Podemos também: if not i in v:
			return False
	return True

	if 1 in v and 2 in v and 3 in v and 4 in v and 5 in v and 6 in v:
		return True
	else:
		return False

#retorn True se n está no vetor v
def procura(n, v): #Meu gabarito
	if n in v:
		return True
	return False

def procura(n, v):
	for i in v:
		if i==n:
			return True
		return False



def procura(n, v): #Gabarito do prof
	return n in v

def procura(n, v):
	flag = False
	if n in v:
		flag = True
	return Flag		

def procura(n, v):
	if v.count(i)==0: #count: retorna as ocorrencias de i em v
		return False
	return True
#------------------------------------------------------------------------
#Retorna quantos números sorteados tem na minha cartela
#sorteados e cartela n tem números repetidos
sorteados = [1, 3, 4, 5, 76]
cartela = [1, 3, 45, 76, 112]
def bingo(sorteados, cartela): #Minha
	soma = 0
	for elemento in sorteados:
		if elemento in cartela:
			soma += 1
	return soma

def bingo(sorteados, cartela):
	soma = 0
	for i in cartela:
		for j in sorteados:
			if i==j:
				soma += 1
	return soma			

def bingo (sorteados, cartela): #Gbarito 
  numeros = cartela.count(sorteados)
  return numeros


#O professor falou um pouco sobre o problema P=NP
 #computação: computacionalmente intratavel
  #demora muito tempo pra ser feito, de forma que é inviavel
   #solução polinomial/tempo polinomial (tratavel)
   #complexidade de algoritmo
   #funções hash(invulneravei)-2^256		
 #matematica: insoluvel

#-----------------
def meio(n):        #Eu fiz pra me ajudar no def inverte(v), mas essa resposta minha é redundante, a do prof é melhor.
	return (n//2)+1
v = [1,2,3,4,5,6]

def inverte(v):
	i = 0
	if len(v)%2==0:
		while i <= (len(v)//2):
			v[i], v[(len(v)-1)-i] = v[(len(v)-1)-i], v[i]
			i += 1

	if len(v)%2==1:
		a = v[meio(len(v))]
		while i <= (len(v)//2):
			if i==meio(len(v)):
				v[meio(len(v))] = a
			else:
				v[i], v[(len(v)-1)-i] = v[(len(v)-1)-i], v[i]
			i += 1	
	return v			
print(inverte(v))				


def inverte(v):
  vreverse = []
  for i in range(len(v),0,-1):
    vreverse.append(i)
  return vreverse
print(inverte(vetor))


def inverte(v):
  a=v.copy()
  for i in range(0, len(v)//2):
    a[i], a[len(v)-1-i]= a[len(v)-1-i], a[i]
    return a
    
#COPIEI DO REPLY
def inverte(v):
  vreverse = []
  for i in range(len(v)-1,-1,-1):
    vreverse.append(v[i])
  return vreverse

def inverte(v): #Gabarito do Prifessor  
  vreverse = v.copy()
  for i in range(len(v)//2):
    vreverse[i], vreverse[len(v)-1-i] = vreverse[len(v)-1-i], vreverse[i]
'''
  return vreverse

vetor = [10,20,30,40,50,60]
print( inverte(vetor) )




















