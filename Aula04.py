#Aula 4
#-------------------------------------------------------------------------------#
#Problema 01:
'''
Leia 2 valores inteiros e armazene-os nas variáveis A e B.
Efetue a soma de A e B atribuindo o seu resultado na variável X.
Imprima X conforme exemplo apresentado abaixo.
Não apresente mensagem alguma além daquilo que está sendo especificado 
e não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

Entrada
A entrada contém 2 valores inteiros.

Saída
Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha.
 Cuide para que tenha um espaço antes e depois do sinal de igualdade, conforme o exemplo abaixo.
'''

#Solução:
#LEIA A ENTRADA

    A = int( input() ) 	# Se eu colocar um "informe o valor de A", o bot/juiz do site vai acusar erro.
    B = int( input() )

#FAÇA O PROCESSAMENTO PARA CALCULAR A SAIDA
    X = A + B

#IMPRIMA A SAÍDA
    #forma 1: Concatenação
        print("X =", X)

    #forma 2- String Formatada:
        print(f"X = {X}")  	#so a partir do python 3.9, mas alguns codigos antigos ainda podem n usar isso

    #forma 3- Literais De Cadeia(Jeito C):
        print("X = %d" %X) 	#Não tem virgula!

    #LITERAIS DE CADEIA - 3 forma:
    # %d - inteiro
    # %f - float (real)
    # %s = string

    #forma 4- .Format:
        print("X = {}".format(X))

#Qual vocês preferem? Maioria: String Formatada
    #Problema string formatada:
        nome = input("Informe seu nome: ")
        idade = int( input("Informe sua idade: ") )

        print(f"O aluno {nome} tem {idade} anos de idade.") 			#Mas e se eu não quiser os espaços?
        print(f"O aluno{nome}tem{idade}anos de idade.")     			#Os espaços permanecem.

        print("O aluno {} tem {} anos de idade.".format(nome, idade))	#Usando o .format

#-------------------------------------------------------------------------------#
#Problema 02:
 '''
 A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:

 - Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

 Entrada
 A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.

 Saída
 Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo,
  com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double).
  Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado.
  Caso contrário, você receberá "Presentation Error".
'''

#SOLUÇÃO:
#LEIA A ENTRADA
    raio = float( input() )

#PROCESSAMENTO
    pi = 3.14159
    area = pi * (raio**2)

#OBS: #area = int(area) #exclui as casas decimais

#IMPRIMA A SAIDA
    #Usando Concatenação:
        print(area) #Só isso é insuficiente, o problema especificou 4 casas decimais;
        #Como imprimir casas decimais usando concatenação? Não sei, por hora, o professor nem mencionou.
        print("%d.2f",volume) 

    #Usando String Formatada:
        print(f"A={area:.4f}")    #Dessa forma, definimos 4 casas decimais;
        print(f"A={area:12.4f}")  #Dessa forma, definimos que o tamanho total da variavel é de 12 caracteres, sendo 4 deles casas decimais;
                                  #Os caracteres vazios, se existirem, serão preenchidos com espaços;
                                   #EXMPLO:
						            # A=     12.5665 (O que efetivamente vai resultar)
						            # A=123456789012 (Comparação para quantificar os caracteres, 12 ao todo)
        print(f"A={area:012.4f}") #Dessa forma, definimos que o tamanho total da variavel é de 12 caracteres, sendo 4 deles casas decimais;
                                  #Os caracteres vazios, se existirem, serão preenchidos com zeros ao invez de espaços;
                                  #EXMPLO:
                                    # A=0000012.5665 (O que efetivamente vai resultar)
                                    # A=123456789012 (Comparação para quantificar os caracteres, 12 ao todo)

    #Usando .format:
        print("A = {:.2f}".format(area))
        #Outro exemplo:
            idade = float( input("Digite sua idade: ") )
            print("Sua idade é {:.2f} anos.".format(idade))

    #Usando literais de cadeia
        print("A=%.4f"%area)    #Dessa forma, definimos 4 casas decimais;
        print("A=%10.4f"%area)  #Dessa forma, definimos que o tamanho total da variavel é de 10 caracteres, sendo 4 deles casas decimais;
                                #Os caracters vazios, se existirem, serão preenchidos com espaços
                                 #EXEMPLO:   
                                 # A=   12.5665 (O que efetivamente vai resultar);
                                 # A=1234567890 (Comparação para quantificar os caracteres, 10 ao todo);
#----------------------------------------------------------------------------------------------------------------------------------------------------------#
#PROBLEMA 3:
'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

MaiorAB= (a+b+abs(a-b))/2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros. NA MESMA LINHA

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''

#SOLUÇÃO:

#Antes de mais nada, vamos aprender a seguinte função:
#A FUNÇÃO SPLIT:
    #"Ela é muito util para fragmentar uma string";
    # Os fragmentos continuam sendo strings;
    # A função split funciona com base em algum criterio para decidir aonde deve separar um fragmento de outro;
    # Por padrão, a função split() ultiliza como criterio o espaço (" ");
     # EXEMPLO:
       a, b, c = input().split()      #Input: 2 4 56
       print(a)                       #Resulta em 2  (string)
       print(b)                       #Resulta em 4  (string)
       print(c)                       #Resulta em 56 (string)
      # A conversão de string para o tipo de dado desejado ainda deve ser feita!
       a, b, c = input().split() #Input: 2 4 56
       a = int(a)
       b = int(b)
       c = int(c)       
       print(a)                       #Resulta em 2  (int)
       print(b)                       #Resulta em 4  (int)
       print(c)                       #Resulta em 56 (int)
      # ALTERNATIVA? NÃO! " int() argument must be a string, a bytes-like object or a real number, not 'list' "
       a, b, c = int(input().split()) #Input: 2 4 56
       print(a)                       #Resulta em 2  (int)
       print(b)                       #Resulta em 4  (int)
       print(c)                       #Resulta em 56 (int)
     
    # Podemos ainda alterar o criterio de fragmentação para outro caracter de nossa escolha:
    # Para isso, basta ultilizar a função split("#"), o # foi escolhido arbritrariamente como exemplo
     # EXEMPLO:
       a, b, c = input().split()      #Input: 7#14#106
       print(a)                       #Resulta em 7   (string)
       print(b)                       #Resulta em 14  (string)
       print(c)                       #Resulta em 106 (string)
     # APLICAÇÃO PRÁTICA:
      #Suponha que queremos separar a parte inteira da parte decimal de um número dado.
      #Para isso podemos simplesmente tomar o criterio de separação como sendo um ponto.
       inteira, decimal = float(input().split("."))
       print(type(inteira)) #string
       print(type(decimal)) #string
       inteira=int(inteira)
       decimal=int(decimal)  

#ENTRADA DE DADOS:
#Alternativa 1 - entrada linha por linha:
a = int(input())
b = int(input())
c = int(input())
print(a)
print(b)
print(c)

#Alternativa 2 - entrada de dados tudo em uma linha:
a, b, c = input().split() # lendo tudo em uma linha
a = int(a)
b = int(b)
c = int(c)
print(a)
print(b)
print(c)


#alternativa 3 - entrada e conversão de tipo tudo em uma linha:
a, b, c = map(int, input().split()) # vai aplicar a função int pra cada um dos resultados do input().split()
                                    #o split devolve uma TUPLA FIXA, MAS O PROF N ENTROU EM DETALHES.
print(a)
print(b)
print(c)

#PROCESSAMENTO DA ENTRADA:
#Alternativa 1 - tal como o programa foi solicitado:
maiorab = (a + b + abs(a-b))//2             #Não há problema em realizar divisão inteira, pois o problema especificou entradas de dados do tipo inteiro somente
maior = (maiorab + c + abs(maiorab-c))//2
print(f"{maior} eh o maior")                #A expressão "eh" é intencional, isto ocorre pois o "é" pode de alguma maneira levar a confusaõ ao ser confundido com função/codigo ask(o prof não entrou em detalhes)
                                            #De qualquer forma, os programadores devem evitar o uso de acentos.                        

#Alternativa 2 - ultilizando a função max:

# A FUNÇÃO MAX 
 #PODE SER USADO PRA CALCULAR O MAIOR DE ALGUNS VALORES
 #ACEITA MULTIPLOS PARAMETROS

#Alternativa 2.1: 
maiorab = max(a,b)   #Dois A Dois
maior   = max(maiorab, c)

#Alternativa 2.2:
maior = max(a, b, c) #Multiplos Parametros



