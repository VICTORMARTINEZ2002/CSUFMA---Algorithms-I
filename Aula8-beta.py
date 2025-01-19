FUNÇÕES - Parte 2:
#return encerra uma função
ARQUIVO 1:
def quadrante(x , y): # Escopo, as variavesi que eu crio dentro de uma função só existem dentro daquela função, ou seja, h´um encapsulamento,
				      # O efeito de uma função,. intencionalmente, não se estende pro resto do codigo
	if x>0 and y>0:   # variaveis globais, saem do encapsulamento, a dica do professor foi não fazer uso de variaveis globais, salvo excessoes
		return "Primeiro quadrante" #uma função pode ter como resultado qualquer um dos TIPOS ja aprendidos té agora, ou até mesmo outra função(lambda calculus)
	elif x<0 and y>0:
		return "Segundo quadrante"
	elif x<0 and y<0:
		return "Terceiro quadrante"
	elif x>0 and y<0:
		return "Quarto quadrante"
	elif x==0 and y==0:
		return "Origem"
	elif x==0 :
		return "eixo Y"    
	else y==0:
		return "eixo X"			
	
print( quadrante(12, 56) )      # Retorna "Primeiro quadrante"
print( type(quadrante))         # Retorna <class 'function'>
print( type(quadrante(0, -56))) # Retorna <class 'str'>

x = quadrante
printi( x(34, 78) )             # Retorna "Primeiro quadrante"


def delta(a, b, c):
	return b*b - 4*a*c
print( delta(1, 2, 5) )

'''
def raiz1(a, b, c):
	d = delta(a, b, c)          # Podemos também chamar uma função dentro de uma outra função;
	x1 = (-b - (d**0.5) ) / (2 * a)
	return x1

def raiz2(a, b, c):
	d = delta(a, b, c)
	x2 = (-b + (d**0.5) ) / (2 * a)
	return x2
#Tais funções, como foram feitas, nos deixam expostos a deltas negativos, vamo resolver isso agora:
'''

def raizes(a, b, c):
	d = delta(a, b, c)
	if d<0:
		return None, None #É o nulo de python

	x1 = (-b - (d**0.5) ) / (2 * a)
	x2 = (-b + (d**0.5) ) / (2 * a)
	return x1, x2	

primeiraRaiz, segundaRaiz = raizes(1, -4, 2)
print(primeiraRaiz, segundaRaiz) # Returna (x1, x2) ou (None, None), ou seja, retorna em uma t-upla;

a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))
print(raizes(a, b, c)) 

#PERGUNTA: Tem como criar funções sem return? Sim, mas o prof. não quis adentrar nisso agora.

#--------------------------------------------------------------------------------------------------------------------------#
#ARQUIVO 2:
n = 23

def	dobro(n): #ESCOPO, o que eu consigo ver naquele trecho de codigo
	print(n)       #Não imprime nada; A função ainda não foi chamada/execuitada; 
	return n*2 #Uma função só enxerga seu escopo, o resultado de uma função só depende dos parametros internos da função
               #NÃO CHAME UMA FUNÇÃO ENQUANTO VC ESTA A CRIANDO,laço infinito RECURSÃO, QUANDO UMA FUNÇÃO CHAMA A ELA MESMA
               def dobro(n):
               	print(dobro(n)) #vai dar merda
               	return 2*n
print(n)      #Imprime: 23	

dobro(45)     #Imprime: 23"\n"45

x = dobro(45) #Armazena na variavel x aquilo que a função retorna/ o "return";

print(x) 	  #Resulta em 90
print(n)      #Resulta em 23


def podeDirigir(idade):
	if idade>=18:
		return True
	else:
		return False
#ou
def podeDirigir(idade):
		return (idade>=18)


def podeVotar(idade:)
	if idade>=16:
		return True
	else:
		return False
#ou
def podeVotar(idade:)
	if idade>=16:
		return True #return encerra uma função
	return False				

w = podeVotar(17)
print( type(w)) # Retorna <class 'bool'>
print(w) # True


#BEECROWD - 1005 - já feito, mas agora usando funções:
def media(a, b):
	soma = 3.5*a + 7.5*b
	return soma/11

a = float( input() )
b = float( input() )

resultado = media(a, b)
print(f"MEDIA = {resultado:.5f}")	
ou
print(f"MEDIA = {media(a, b):.5f}")

#BEECROWD - 1013 - já feito, mas agora usando funções:
def maiorAB(a, b):
	return ( ( a + b + abs(a-b) ) / 2 )