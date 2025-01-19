vetorees - randomico - acesso aleatorio igual
listas- tabela hash- n tem um acesso igual, porém, muito parecido por causa da dinamica de hashinh

for num in v:
	print num

for i in range(0, len(v))
	print(v[i])	

qtd_linhas == len(cartela)
qtd_colunas== len(cartela[0])
elementos == qtd_colunas*qtd_linhas	

MATRIZES - Teoria e pr
#bingo
vetor de sting ["a", "b", "c"]
cartela = [ [ 7, 79,  9, 45,  4],
			[32, 19,  1, 21,  6],		
			[24, 13, 55, 73, 18],
			[29, 23,  5, 30, 57],
			[56, 33, 27, 36,  2]]

len(cartela)  #resulta em 5
cartela[0]    #resulta em [ 7, 79,  9, 45,  4]
cartela[2][2] #resulta em 55

qtd_linhas == len(cartela)
qtd_colunas== len(cartela[0])
elementos == qtd_colunas*qtd_linhas	

def printCartela(cartela):
	print("B\TI\TN\TG\TO")
	for linha in cartela:
		for num in linha:
			if num == -1:
				print("X", end = "\t")
			else:	
				print(f"{num}", end = "\t")
		print()
	print()

'''
def printCartela(cartela):
	print("B    I   N   G   O")
	for linha in cartela:
		for num in linha:
			espacos = " " * (3-len(str(num)))
			print(f"{espacos}{num}", end = "\t")
		print()
'''					 

def marcaNumero(cartela, n):
	flag = false
	for linha in cartela:
		for j in range(len(linha)):
			if linha[j]==n:
				linha[j] = -1 #sentinela
				return True
	return False	

def temLinha(cartela):
	for linha in cartela:
		todosSorteados = True
		for num in linha:
			if num!= -1
				todosSorteados = False
				break
		if todosSorteados:
			return True
	return False								

def temColuna(cartela):
	qtd_linhas == len(cartela)
	qtd_colunas== len(cartela[0])

	for j in range(qtd_colunas):
		todosSorteados = True
		for i in range(qtd_linhas):
			if cartela[i][j] != -1:
				todosSorteados = False
				break
		if todosSorteados:
			return True		

#def printCartela(cartela):
#	print("B\TI\TN\TG\TO")
#	for linha in cartela:
#		for num in linha:
#			tamanho_numero = len(num)
#			espacos = " "*len(num)
#			print(f"{espacos}{num}", end = "\t")
#		print()	 
'''
#codigo do andrei
caracteres="[],"
for i in range(5):
listastring=str(cartela[i])
for x in range(len(caracteres)):
listastring = listastring.replace(caracteres[x],"")
print(listastring)

caracteres="[],"
for i in range(5):
listastring=str(cartela[i])
for x in range(len(caracteres)):
listastring = listastring.replace(caracteres[x],"")
listastring = listastring.replace(" ", "\t")

print(listastring)
'''
'''
while True:
	printCartela(cartela)

	print()
	n = int(input("Qual número foi sorteado? "))

	#if n in cartela:               #os elementos de cartela são vetores, não vai funcionar;
	#	print("Acertou um número")


	flag = false
	for linha in cartela:
		for j in range(len(linha)):
			if linha[j]==n:
				print("Acertou um número!")
				print()
				linha[j] = -1
				flag = True
				break
		if flag==False:
			break

	if flag==False:
		print("Não acertou um número!")
		print()			
'''
números_faltando = elementos
while números_faltando > 0:
	printCartela(cartela)
	print()
	n = int(input("Qual número foi sorteado? "))

	if marcaNumero(cartela, n):
		print("acertou um número")
		print()
		números_faltando -= 1
	else:
		print("Não acertou um número!")
		print()		
	#algora o bingo termina quando temLinha ou temColuna está completo	
	if temLinha(cartela) or temColuna(cartela):
		break
	

	print(f"Faltam {números_faltando} em sua cartela.")
	print(20*"-")
print("BINGO!!!!")

printCartela(cartela)	
#------------------------------------------------------------------------------------------------#

final 27/julho
reposição 25/julho
3 prova 18-20/julho-(apresentação)
2 prova - 13/07 ou 18/07

cartela = [ [ 7, 79,  9, 45,  4],
			[32, 19,  1, 21,  6],
			[24, 13, 55, 73, 18],
			[29, 23,  5, 30, 57],
			[56, 33, 27, 36,  2]]

for i in cartela?
    for j in cartela[]



print(printCartela(cartela))
#------------------------------------------------------------------------------------------------#
Jogo Da Velha
velha = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

def printVelha(velha):
	print("")...
