1172
i = 0
x = []
while i<=9:
	a = int(input())
	x.append(0)
	if a<=0:
		x[i] = 1
	else:
		x[i] = a
	print(f"X[{i}] = {x[i]}")		
	i += 1
	
1173
n = int(input())
x = []
i = 0
while i<=9:
	x.append(0)
	x[i] = n * (2**i)
	print(f"N[{i}] = {x[i]}")
	i += 1

1174
A = []
i = 0
while i<=99:
	A.append(0)
	A[i] = float(input())
	if A[i] <= 10:
		print(f"A[{i}] = {A[i]:.1f}")
	i += 1		

1175
n = []
i = 0
tv = 20
#Obtendo o vetor original
while i<= (tv-1):
	n.append(0)
	n[i] = int(input())
	i += 1

#Obtendo o vetor inverso
i = 0
m = n.copy()
while i < (len(m)//2):
	m[i], m[(len(m)-1)-i] = m[(len(m)-1)-i], m[i]
	i += 1

#Saída
i = 0
while i<=(tv-1):
	print(f"N[{i}] = {m[i]}")
	i += 1

1176
def fibonnaci(n):
	if   n==0:
		return 0
	elif n==1:
		return 1
	else:
		a = 0
		b = 1
		c = -1
		i = 1
		while i<n:
			c = a+b
			a = b
			b = c
			i += 1
		return c

t = int(input())
while t>=1:
	n = int(input())
	print(f"Fib({n}) = {fibonnaci(n)}")
	t -= 1

1177
t = int(input())
x = []
i = 0
j = 0

while i <= 999/t:
	while j <= (t-1):
		x.append(0)
		x[j+(t*i)] = j
		print(f"N[{j+(t*i)}] = {x[j+(t*i)]}")
		if len(x)>=1000:
			i = 1001
			break
		j += 1	
	j = 0	
	i += 1	


1178
n = float(input())
x = [n]
print(f"N[0] = {n:.4f}")
i = 1
while i<=99:
	x.append(0)
	x[i] = x[i-1]/2
	print(f"N[{i}] = {x[i]:.4f}")
	i += 1

1179
i=0
j=0
par = []
impar = []
while i<15:
	n = int(input())
	if n%2==0:
		par.append(n)
		if len(par)>=5:
			while j<=4:
				print(f"par[{j}] = {par[j]}")
				j += 1
			j = 0
			par.clear()		

	if n%2==1:		
		impar.append(n)
		if len(impar)>=5:
			while j<=4:
				print(f"impar[{j}] = {impar[j]}")
				j += 1
			j = 0
			impar.clear()		
	i += 1
if len(impar)>0:
	j = 0
	while j<=(len(impar)-1):
		print(f"impar[{j}] = {impar[j]}")
		j += 1
if len(par)>0:
	j = 0
	while j<=(len(par)-1):
		print(f"par[{j}] = {par[j]}")
		j += 1		
























