#AULA 5
#REVISÃO: 
#FUNÇÕES:
  # print
  # input
  # type
  # int, float, srt, bool

X = 12
print(x)

x = input("Informe um inteiro: ")
x = int(x)
print(x)

#AULAS DO BEECROWD
  # split
  # map
  # formatação de string  


#COMANDO CONDICIONAL: SE, IF
 # Até agora, nossos codigos sempre operam de uma mesma forma;
 # O maximo que podemos fazer é imprimir True ou False com base no que foi digitado;
  print(x>=89)
 # Com o if, podemos ter comportamentos diferentes dependendo do que o usuario digital, do valor de uma variavel:

#--------------------------------------------------------------------------------------------------------------------------------#
#EXERCICIO 1: O usuario pode dirigir?
idade = int(input("Qual a sua idade? "))

#IDENTAÇÃO (SEM IDENTAÇÃO O IF RESULTA EM ERRO)
if idade>=18 :
	print("Pode dirigir.") #CONDICIONAL
	print("Outra linha aqui!")	
else: #SENÃO        
	print("Não pode dirigir.")
	print("Outra linh aqui!")
#if idade<18:
#	print("Não pode dirigir.")
#if not idade>=18:
#	print("Não pode dirigir.")

#Podemos também escrever assim, embora seja extremamente preferencial evitar tal forma:
if idade>=18: print("Pode dirigir.")
else: print("Não pode dirigir.")	
	
#INCONDICIONALMENTE
print("Tchau! Programa Terminado.")

#--------------------------------------------------------------------------------------------------------------------------------#
#EXERCICIO 2:
# COMPARAR A IDADE DE DUAS PESSOAS E RETORNAR O MAIS VELHO

idadeJoao = int(input("Qual sua idade, Joaõ? "))
idadeBela = int(input("Qual sua idade, bela? "))

#MODO ERRADO 01:
if idadeJoao > idadeBela :
	print("João é mais velho que Bela.")
else:
	print("Bela é mais velha que João")
#Vai dar errado quando idadeJoao = idadeBela

#MODO ERRADO 02:
if idadeJoao > idadeBela :
	print("João é mais velho que Bela.")	
if idadeBela > idadeJoao :
	print("Bela é mais velha que João.")
else idadeJoao == idadeBela:
	print("Eles possuem a mesma idade.")
#Vai dar errado pq esse else pertence ao segundo if:
#De forma que podemos ter simultaneamente como resposta:
#	João é mais velho que Bela.
#	Eles possuem a mesma idade.
#Caso a idadeJoao > idadeBela.

#ALTERNATIVA 01 - 3 if´s:
if idadeJoao > idadeBela :
	print("João é mais velho que Bela.")	
if idadeBela > idadeJoao :
	print("Bela é mais velha que João.")
if idadeJoao == idadeBela:
	print("Eles possuem a mesma idade.")
#Em casos mais complexos, é dificil garantir que não vamos ter como verdadeiro mais de um if.		

#ALTERNATIVA 02 - ANINHAMENTO OU CASCATA:
if idadeJoao > idadeBela :
	print("João é mais velho que Bela.")
else:
 if idadeBela > idadeJoao :
	print("Bela é mais velha que João.")
 else:
 	print("Eles possuem a mesma idade.")				

#ALTERNATIVA 03 - ELIF (SWICH CASEC, EM C++ usamos o comando SWICH):
if idadeJoao > idadeBela :
	print("João é mais velho que Bela.")
elif idadeBela > idadeJoao :
	print("Bela é mais velha que João.")
 else:
 	print("Eles possuem a mesma idade.")

#--------------------------------------------------------------------------------------------------------------------------------#
#EXERCICIO 03:
'''
Judô feminino
- Ligeiro:   até 48 quilos
- Meio-leve: até 52 quilos
- Leve: até 57 quilos
- Meio-médio: até 63 quilos
- Médio: até 70 quilos
- Meio-pesado: até 78 quilos
- Pesado: mais de 78 quilos
'''

peso = float(input("Qual sua massa? "))
#Alternativa 01 - "full if´s":
if (massa <= 48.0):
	print("Ligeiro")
if (massa > 48 and massa <= 52):
	print("Meio-leve")	
if (massa > 52 and massa <= 57):
	print("Leve")
if (massa > 57 and massa <= 63):
	print("Meio-médio")	
if (massa > 63 and massa <= 70):
	print("Médio")
if (massa > 70 and massa <= 78):
	print("Meio-pesado")
else:
	print("Pesado")


#Alternativa 02 - elif´s:
 #Python  até aceita duas comparações na mesma condição: 
  #Mas varias outras linguagen não aceitam
  #Portanto é preferencial usar o "and";
if massa <= 48:
	print("Ligeiro")
elif 48 < massa <= 52:
	print("Meio-leve")	
elif 52 < massa <= 57:
	print("Leve")
elif 57 < massa <= 63:
	print("Meio-médio")	
elif 63 < massa <= 70:
	print("Médio")
elif 70 < massa <= 78:
	print("Meio-pesado")
else:
	print("Pesado")

#ALTERNATIVA 03 - Usando o "and":
if (massa <= 48):
	print("Ligeiro")
elif (massa > 48 and massa <= 52):
	print("Meio-leve")	
elif (massa > 52 and massa <= 57):
	print("Leve")
elif (massa > 57 and massa <= 63):
	print("Meio-médio")	
elif (massa > 63 and massa <= 70):
	print("Médio")
elif (massa > 70 and massa <= 78):
	print("Meio-pesado")
else:
	print("Pesado")	

#ALTERNATIVA 04 - Preferencial:
if massa <= 48:
	categoria = "Ligeiro"
elif massa <= 52:
	categoria = "Meio-leve"	
elif massa <= 57:
	categoria = "Leve"
elif massa <= 63:
	categoria = "Meio-médio"
elif massa <= 70:
	categoria = "Médio"
elif massa <= 78:
	categoria = "Meio-pesado"
else:
	categoria = "Pesado"

print(f"Sua categoria no judô femino é: Peso {categoria}.")	

#--------------------------------------------------------------------------------------------------------------------------------#
#EXERCICIO 03 - DADA UMA COORDENADA CARTESIANA, INFORME EM QUAL QUADRANTE ELA SE ENCONTRA:
#O tempo acabou, então ficou como dever de casa.
#Minha resposta:

#Entrada de dados:
x = float(input("Coordenada X: "))
y = float(input("Coordenada Y: "))
quadrante = "A"
eixo = "A"
sinal = "A"
origem = False

#Processamento:
if x == 0:
	if y == 0:
		origem = True
	elif y > 0:
		eixo = "ordenadas"
		sinal = "positivo"
	elif y < 0:
		eixo = "ordenadas"
		sinal = "negativo"
if x > 0:
	if y == 0:
		sinal = "positivo"
		eixo = "abscissas"
	elif y > 0:
		quadrante = 1
	elif y < 0:
		quadrante = 4
if x < 0:
	if y == 0:
		sinal = "negativo"
		eixo = "abscissas"
	elif y > 0:
		quadrante = 2
	elif y < 0:
		quadrante = 3

#Saida de dados:
if origem==True:
	print(f"O ponto fornecido, cuja cordenada é ({x};{y}), se encontra na origem do plano cartesiano.")
elif (not quadrante == "A"):
	print(f"O ponto fornecido, cuja cordenada é ({x};{y}), se encontra no {quadrante}° quadrante.")
else:
	print(f"O ponto fornecido, cuja cordenada é ({x};{y}), se encontra no eixo {sinal} das {eixo}.")	

