#Alternativa 1:
n1 = int(input())
n2 = int(input())
n3 = int(input())
maior = 0
meio = 0
menor = 0

def maior(n1,n2,n3):
	if ( (n1>=n2) and (n1>=n3) ):
		return n1
	elif ( (n2>=n1) and (n2>=n3) ):
		return n2
	else:
		return n3	
		
def menor(n1,n2,n3):
	if ( (n1<=n2) and (n1<=n3) ):
		return n1
	elif ( (n2<=n1) and (n2<=n3) ):
		return n2
	else:
		return n3		

meio = (n1+n2+n3) - ( menor(n1,n2,n3) + maior(n1,n2,n3) )
print(menor(n1,n2,n3))
print(meio)
print(maior(n1,n2,n3))
print(f"{menor(n1,n2,n3)}, {meio}, {maior(n1,n2,n3)}")

#Alternativa 2:
n1 = int(input())
n2 = int(input())
n3 = int(input())
n = [n1,n2,n3]
print(sorted(n))

'''
#Alternativa 3 -  Incompleta(melhor do que fazer 24 if´s):
n1 = float(input("N1: "))
n2 = float(input("N2: "))
n3 = float(input("N3: "))
n4 = float(input("N4: "))

maior = max(n1,n2,n3,n4)
menor = min(n1,n2,n3,n4)
total = n1+n2+n3+n4
somaMeio = total - (maior+menor)

if n1!=maior and n1!=menor:
'''	
	