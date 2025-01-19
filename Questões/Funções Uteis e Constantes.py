def Fatorial(n):
	fatorial = 1
	i = 1
	while i<=n:
		fatorial = fatorial*i
		i += 1
	return fatorial

def fibonnaci(n):
	if   n==1:
		return 0
	elif n==2:
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




def ehPrimo(n): #Existe Mais otimizada, mas o prof ainda n ensinou
	if n<2:
		return False

	if n==2: 
		return True 
	if n%2==0: 
		return False

	i = 3
	while i*i<n:
		if n%i==0:
			return False
		i += 2
	return True
		