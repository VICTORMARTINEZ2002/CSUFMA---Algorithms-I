#AULA3-beta:
#tipos de dados

n = 3
print( type(n) )   #int 

n = 4/2
print(n)           #2.0
print( type(n) )   #float

flag = True
print(flag)        #True
print( type(flag)) #bool

nome = "ufma"
print( type(nome)) #str

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CASTING: conversão de um tipo de dado pra outro tipo de dado, podendo ou não ocorrer automaticamente;
n = 8/4
n = int(n)          #recebe um paramentro de outro tipo e converte pra inteiro
print(n)            #vai aparecer só 2
print ( type(n))

n = int("1024")
print(n+4)          #n se pode somar um inteiro com uma string, a string faz concatenação
print(type(n))

n = "1024"
print(n+"4")        #É uma string, não é um inteiro #Resulta em10244

n = int(n)
print(n*4) 	 	    #Resulta em 4096
print( type(n))

m = float("3.1456") #converte de string para ponto flutuante
print(m)
print(type(m))

w = 1200
print(2*w) 			#Resulta em 2400
w = str(w)
print(2*w)          #Resulta em 12001200

#Usa-se int   para converter para inteiro
#Usa-se float para converter para real
#Usa-se srt   para converter para string
#Usa-se bool  para converter para booleano

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# EXPRESSÕES aritmeticas
x = 2*4
print(x)

print(3**2)     	#Operação de exponenciação: no caso, 3 elevado a 2
print(3**(0.5)) 	#Uma alternativa para realizar uma operação de radiciação por meio do uso de expoentes: no caso, 3 elevado (0.5) = Raiz Quadrada de 3

x = 10/3 			#Vai resultar em um real / float, pode ter um erros de arredondamentos
y = 10//3 			#É uma divisão inteira, vai resultar em um inteiro

print(x, type(x))
print(y, type(y))

resto = 10%3        #RESTO DA DIVISÃO DE DOIS NÚMEROS
print(resto) #1

resto = 2%10
print(resto) #2

n = 1234
resto = n % 2
print(resto)        #Se resultar em zero, o número é par; se resultar em 1, é impar;

#SE UM NÚMERO QUALQUER FOR DIVIDIDO POR N, O RESTO VAI VARIAR ENTRE ZERO E (N-1)

m = 344354
resto = m % 7       #Se resultar em zero, 7 é divisor de m;
print(resto)

#EXERCICIO: QUERO OBTER O ULTIMO DIGITO DE UM NÚMERO INTEIRO QUALQUER
#PARA ISSO BASTA CALCULAR O RESTO DA DIVISÃO DO NÚMERO POR 10
#SE QUISSE-SE OS 2 ULTIMOS DIGITOS, DEVO CALCULAR O RESTO DA DIVISÃO POR 100 E ASSIM POR DIANTE...
o = 3829475 
resto = o % 10
print(o, resto)

#OBSERVAÇÃO: um numero perfeito é aquele em que a soma dos divisores é igual ao proprio número. Exemplo: 6;

#AS REGRAS DE MATEMÁTICA AINDA SÃO VALIDAS:
x = 1+2*3
y = (1+2)*3
print(x)
print(y)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#EXPRESSÕES RELACIONAIS:
#SÃO COMPARAÇÕES CUJO RESULTADO SEMPRE SERÁ BOOLEANO, ISTO É, VERDADEIRO OU FALSO

minhaVariavel = 7 > 5
print(minhaVariavel) 				#Resulta em true
minhaVariavel = 7*7 > 51
print(minhaVariavel) 				#Resulta em false
minhaVariavel = 7*7 > 51 - x
print(minhaVariavel) 				#Resulta em true
print(type(minhaVariavel))          #Resulta em bool

s = ( "UFMAUFMA" == 2*"UFMA" )
print(s) 							#Resulta em true
s = ( "UFMAUFMA" == 2*"ufma" )
print(s) 							#Resulta em false


#UM SÓ IGUAL É UMA ATRIBUIÇÃO =
#DOIS IGUAIS É UMA COMPARAÇÃO ==

idade = 17
podeDirigir = (idade >= 18)
print(podeDirigir)					#Resulta em false 

idade = 21
podeDirigir = (idade >= 18) 		#Resulta em true
print(podeDirigir)
idade = 15 							#Não vai alterar nada, não afeta mais a variavel podeDirigir, hajá vista que já foi atribuido um valor a ela, sendo necessario fazer nova atribuição;
podeDirigir = (idade >= 18) 		#Apos a nova atribuição, havera mudança de valor;
print(podeDirigir) 					#Resulta em false

#Operadores relacionais:
print(11 > 11)  #maior
print(11 < 11)  #menor
print(11 == 11) #igual
print(11 >= 11) #maior ou igual
print(11 <= 11) #menor ou igual
print(11 != 11) #diferente(negação do igual)

#print(11 <> 11) #diferente? Estava assim no slide, mas acho que é um erro;

#print(11 = 11), #vai dar erro, um unico simbolo de igual é atribuição

print( not 11 == 11)   				#Resulta em false
print( not False) 					#Resulta em true
print( not True)  					#Resulta em false

#Queremos que ambos tenham mais de 15 anos para ser autorizada a entrada
#Caso 1:
idadePessoa1 = 14
idadePessoa2 = 18
podemEntrar = (idadePessoa1 >= 15 and idadePessoa2 >= 15)
print(podemEntrar) 					#Resulta em false

#Caso 2:
idadePessoa1 = 19
idadePessoa2 = 18
podemEntrar = (idadePessoa1 >= 15 and idadePessoa2 >= 15)
print(podemEntrar) #true

#Queremos que pelo menos uma pessoa tenha 15 anos ou mais para ser autorizada a entrada
idadePessoa1 = 14
idadePessoa2 = 18
podemEntrar = (idadePessoa1 >= 15 or idadePessoa2 >= 15)
print(podemEntrar) #true

#CURTO CIRCUITO
#COMO MEDIDA DE EVITAR DESPERDICIO DE TEMPO PROCESSANDO UMA COISA PARA A QUAL JÁ TEMOS A RESPOSTA, PODE HAVER ERROS COM A SEMANTICA DA AFIRMAÇÃO:
#Caso OR: 
print( True or False) 	#Haja vista que o true já torna a afirmação verdadeira, o false é ignorado completamente. Problemas:		
print( True or 127863781269 + 17862178621 > 2687921789343) #O False está semanticamente incorreto

#Caso AND:
print( False and True)  #Haja vista que o false já torna a afirmação incorreta, o true  é ignorado completamente. Problemas:
print( False and 3917390187 * 17829718924 < 1789375558931) #O true está semanticamente incorreto

#DICA:
#SE NOS DEPARARMOS COM UMA SITUAÇÃO QUE EXIJA O USO DE MUITOS "AND" & "OR", USE (PARENTESES);
#EMBORA DESACOMSELHAVEL, É POSSIVEL FAZER USO DA ORDEM PADRÃO: 1-NÃO, 2-AND, 3-OR;

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ENTRADA DE DADOS
#COMANDO INPUT()

linha = input("Digite algo: ") 				#Será captado o que o usuario escreveu e será guardado pelo programa em forma de string;
print(linha)

linha = input("Digite um inteiro: ") 		#O resultado será uma string;
print(2*linha) 								#Ocorrerá uma concatenação, não uma multiplicação;

linha = input("Digite um inteiro: ") 		#O resultado será uma string;
linha = int(linha) 							#Agora o resultado é um inteiro;
print("O dobro desse inteiro é ", 2*linha) 

#Alternativa mais eficiente
linha = int( input("Digite um inteiro: ")) 	#O resultado é um inteiro;
print("O dobro desse inteiro é ", 2*linha) 


#dever de casa, imprimir o delta de uma equação
#a, b, c = float( input("Digite um a, b, c em ordem: ")) #ainda tenho q testar e vai ser proxima aula

#EXERCICIO: DADOS a, b, c Pertencentes ao conjunto dos REAIS tal que a.x² + b.x + c = 0, Calcule Delta:
#ALTERNATIVA 1:
a = float(input("Digite o termo A: "))
b = float(input("Digite o termo B: "))
c = float(input("Digite o termo C: "))

delta = b*b - 4*a*c
print("O valor de delta é: ", delta)

#ALTERNATIVA 2, FAZENDO USO DE STRING FORMATADA(CONTEUDO DAS PROXIMAS AULAS):
a=float(input('Digite o valor de A: '))
b=float(input('Digite o valor de B: '))
c=float(input('Digite o valor de C: '))

print('Lembre-se, delta(Δ) se dá pela fórmula: b²-4ac')
delta=(b**2 - 4*a*c)
print(f'Resultado do seu delta: {b}²-4*{a}*{c}={delta}')

#ALTERNATIVA 3, FAZENDO USO DO .FORMAT, QUE APARENTEMENTE É UMA STRING COM VARIAVEIS NO MEIO DELA(CONTEUDO DAS PROXIMAS AULAS):
print ('Digite a, b e c:')
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
delta = (b**2 - 4*a*c)
print ('O valor de delta é {}'.format(delta))






