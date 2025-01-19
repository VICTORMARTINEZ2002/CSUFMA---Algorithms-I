#1:
senha = 2002
senhaInserida = int(input())
while senhaInserida!=senha:
	print("Senha Invalida")
	senhaInserida = int(input())
print("Acesso Permitido")	


#2:
a=True
while a:
	n1 = float(input())
	while n1<0 or n1>10:
		print("nota invalida")
		n1 = float(input())

	n2 = float(input())
	while n2<0 or n2>10:
		print("nota invalida")
		n2 = float(input())		

	media = (n1+n2)/2
	print(f"media = {media:.2f}")	

	print("novo calculo (1-sim 2-nao)") 
	nc = float(input())

	while (nc!=1 and nc!=2):
		print("novo calculo (1-sim 2-nao)") 
		nc = float(input())
	if nc==2:
		a = False


#3:
n = int(input())
N=[]

i = 0
while i<=9:
	N.append(n*(2**i))
	print(f"N[{i}] = {N[i]}")
	i += 1





