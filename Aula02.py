Assuntos Novos Nessa Aula:
int()
float()
bool
True
False
str()
palavra/word
overflow
Casting
type()
div. inteira //




AULA 2 - TIPOS (PRIMITIVOS) DE DADOS
 INTEIRO
 REAL
 LOGICO
 STRING

 --> INT:  O INTEIRO usa menos memória do que um REAL, além de evitar erros de "arredondamento binario"*, portanto, É PREFERENCIAL USAR INT QUANDO FOR CABIVEL;
 --> REAL: Devido ao modo como funciona a definição de valores em binario, os números reais podem nem sempre resultar em resultados esperados;
  PONTO FLUTUANTE(float) é a forma usada para representar numeros reais na memoria do computador;



x = 0.2 + 0.2 + 0.2 # Isso aqui em binario é uma dizima periodica, o que da um erro de precisão;
					# Nem todo número real vai dar esse problema, 0.5 por exemplo não dá esse problema em binario;
y =  0.6

print( x == y ) #comparação que resulta em false


OBS: O professor comentou sobre NULL & FUNÇÃO também são tipos de dados primitivos, mas disse que não ia se aprofundar;
OBS: É possivel representar números complexos em python por meio de uma biblioteca numpy, mas não é um tipo primitivo;


DEFINIÇÃO INFORMAL(PALAVRA/WORD):
	É o tanto de bits(32 ou 64 bits) que o pc consegue enviarm em uma unica pulsação;
	A velocidade das pulsações num computador gira em torno de 1MHz-5MHz;

DEFINIÇÃO INFORMAL(OVERFLOW):
	É quando uma variavel passa do limite de barramento(32 ou 64bits);
	Em python, não ocorre overflow, pois python é uma linguagem de alto nivel e faz uso de BIGINT ou grande inteiro, embora isso possa significar erros de arredondamento nas variaveis do tipo real;
	Essa diferença faz o acesso a uma variavel inteira em python (linguagem de alto nivel) bem mais lento do que em C (linguagem de baixo nivel);
	OBS: DEFINIÇÃO INFORMAL(STACK OVERFLOW): É quando muitas funções são chamadas, mas isso é conteudo futuro;
	

	n = 18446744073709551616.384762924
	print("n")


DEFINIÇÃO INFORMAL(CASTING): 
	O python converte alguns tipos de dados automaticamente;
	Toda divisão é convertida em número REAL;


#NOVO COMANDO: TYPE()

'''


n = 43543
m = 43543.00

print( type(n))
print( type(m))

print( type(3)   ) # Resulta em INT
print( type(3/3) ) # Resulta em REAL(cashing)
print( 3/3       ) #toda vez q faz uma divisão, ele converte pra real


'''

#DIVISÃO INTEIRA: É fazer uma divisão e considerar somente a parte inteira, trunca-la, e, por consequencia, eliminar a parte decimal;
   REPRESENTAÇÃO: Pelo sinal //
         Exemplo: 5//3
#ARREDONDAMENTO: O professor não entrou em delatalhes, é um assunto futuro, mas se usa round();          

'''


print(3//3)       #divisão inteira, não é arredondamento, é truncar a parte inteiro e eliminar a parte decimal
			      #arredondamento é a função round()
print (8/3)
print (8//3)      #divisão inteira
print(type(8//3)) # vai dar inteiro, naturalmente
	

'''
OBSERVAÇÃO SOBRE BOOLEAN:
	Eu so preciso de 1 bit pra armazenar true ou false, mas não tem como mandar só um bit pelo barramento, é necessario mandar todos os 64 bits(ou32bits, enfim) por barramento;
	Para contornar esse problema, Pyton ultiliza do BIT MAP: quando vc tem varias variaveis do tipo logico, será ultilizado os mesmo 64 bits de uma palavra pra trnasportar as 64 variaveis logicas;
	Zero é arbritario pra ser falso, e 1 pra verdadeiro( 1 = TRUE; 0 = FALSE);
'''

mensagem = 'si4e0s()(HJ()U'
mensagem = "Carlos de Salles"
print(type(mensagem))   # vai me dizer que é uma string, em python string é STR;

TVligada = True
print(TVligada)
print( type(TVligada) ) # Vai retornar o tipo bool;
