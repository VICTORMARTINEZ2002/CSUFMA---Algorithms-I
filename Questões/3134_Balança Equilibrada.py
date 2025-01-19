#2 BEE 3134 - BALANÇA EQUILIBRADA:
#ENTRADA DE DADOS:
Ai = float(input())
Bi = float(input())
Ci = float(input())
Di = float(input())
A = 10*Ai
B = 10*Bi
C = 10*Ci
D = 10*Di
A=int(A)
B=int(B)
C=int(C)
D=int(D)


#PROCESSAMENTO:
V = ( (A == B + C + D) or (A + B == C + D) or (A + C == B + D) or (A + D == B + C) or (A + B + C == D) or (A + B + D == C) or (A + C + D == B) )

#SAIDA DE DADOS:
if (V == True):
	print("YES")
if (V == False):
	print("NO")

obs:
inteiro, decimal = input().split(".")	
A = inteiro*10 + decimal








 



