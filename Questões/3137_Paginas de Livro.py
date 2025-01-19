#BEE_CROWD 3137
#------------------------------------------------------------------------------------
#DESAFIO, FAZER SEM O IF:
# ENTRADA DE DADOS
P = input()
P = int(P)

#PROCESSAMENTO
A = min(P, 9)

B = max(0, (P-9))
B1= min(B, (90))

C = max(0, (P-99))
C1= min(C, (900))

D = max(0, (P-999))
D1= min(D, (9000))

E = max(0, (P-9999))
E1= min(E, (90000))

F = max(0, (P-99999))
F1= min(F, (900000))

TOTAL = (A) + (B1*2) + (C1*3) + (D1*4) + (E1*5) + (F1*6)

# SAIDA DE DADOS:
print(TOTAL)
#------------------------------------------------------------------------------------
#Com o if(prof ainda n ensinou):
#QUANTIDADE DE ALGARISMOS DOS NUMEROS DE 1 ATÉ P USANDO O IF:
#ENTRADA DE DADOS:
P = int(input())

#PROCESSAMENTO:
if (P<10):
	TOTAL_DE_DIGITOS = P*1

if (P>10 and P<100):
	TOTAL_DE_DIGITOS = (9*1 + (P-9)*2)

if (P>100 and P<1000):
	TOTAL_DE_DIGITOS = (9*1 + 90*2 + (P-99)*3)

if (P>1000 and P<10000):
	TOTAL_DE_DIGITOS = (9*1 + 90*2 + 900*3 + (P-999)*4)

if (P>10000 and P<100000):
	TOTAL_DE_DIGITOS = (9*1 + 90*2 + 900*3 + 9000*4 + (P-9999)*5)

if (P>100000 and P<1000000):
	TOTAL_DE_DIGITOS = (9*1 + 90*2 + 900*3 + 9000*4 + 90000*5 + (P-99999)*6)

#SAIDA DE DADOS:
print(P)
print(TOTAL_DE_DIGITOS)	
#------------------------------------------------------------------------------
#Usando loops(se n deu nem o if, imagina loop):
P = int(input("DIGITE ALGUM NÚMERO: "))
resultado = 0

contador = 1
while (contador < numero+1)
	resultado = resultado + len(str(contador))
	contador = contador + 10

print(f"Resultado = {resultado}")	
#---------------------------------------------------------------------------------------
#Usando uma formula fechada que eu não sabia que tinha:
p = input()
numAlgarismos = len(p)
paginas = int(p)

subtraendo = int('1' * numAlgarismos)

digitos = (paginas + 1)*numAlgarismos - subtraendo

print(digitos)
#-------------------------------------------------------------------------------------------------------



#TENTATIVA 1:
'''
#BEE 3137
#ENTRADA DE DADOS:
P = int(input()) #1-1,000,000

#PROCESSAMENTO:
SUBTRAÇÃO_MAX = 1000000 - P

P1 = P % 10
P2 = P % 100
P3 = P % 1000
P4 = P % 10000
P5 = P % 100000
P5 = P % 1000000

999,999

TOTAL_DE_DIGITOS = (P1*1) + (P2*2) + (P3*3) + (P4*4) + (P5*5) + (P6*6)  + (P7*7)
				 = 1		99        999     9,999    99,999   999,999
'''
#TENTATIVA 2:
'''
#LIVRO DE 1 A 9 PAGINAS:
#ENTRADA DE DADOS
P= int(input())

#PROCESSAMENTO
P1 = P % 10
print(P1)
TOTAL_DE_DIGITOS = (P1*1)

#SAIDA DE DADOS:
print(TOTAL_DE_DIGITOS)


#LIVRO DE 1 A 99 PAGINAS:
#ENTRADA DE DADOS
P= int(input())

#PROCESSAMENTO
P1 = P % 10
P1 = P // 10  #4
D1 = 0      
P2 = P % 100 #34
D2 = P - 9  

#print(P1)
#print(P2)
TOTAL_DE_DIGITOS = (P1*1) + (D2*2)
TOTAL_DE_DIGITOS = (9 *1) + (25*2)
TOTAL_DE_DIGITOS = (9 *1) + ((P-9)*2)

#SAIDA DE DADOS:
print(P1)
print(P2)
print(D2)
print()

print(TOTAL_DE_DIGITOS)



#TENTATIVA 3:
#BEE  3137
#ENTRADA DE DADOS:
P = int(input()) #1-1,000,000

#PROCESSAMENTO:
P1 = P % 10
P2 = (P % 100)-(P1)
P3 = (P % 1000)-(P2+P1)
P4 = (P % 10000)-(P3+P2+P1)
P5 = (P % 100000)-(P4+P3+P2+P1)
P6 = (P % 1000000)-(P5+P4+P3+P2+P1)
print(P1, P2, P3, P4, P5, P6) #OKAY

999,999

TOTAL_DE_DIGITOS = (P1*1) + (P2*2) + (P3*3) + (P4*4) + (P5*5) + (P6*6)  + (P7*7)
				 = 1		99        999     9,999    99,999   999,999
'''



