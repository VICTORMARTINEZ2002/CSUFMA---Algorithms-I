#BEECROWN
#1072
n = int(input())
m = " "
contadorIn = 0
i = 1
while i<n-1:
	m = input()
	m = int(m)
	if m>=10 and m<=20:
		contadorIn += 1

contadorOut = n-contadorIn
print(f"{contadorIn} in") 		
print(f"{contadorOut} out") 


n = int(input())
i=1
contadorIn = 0
while i<=n:
	m=int(input())






#1073
n = int(input())

i = 1
while i<=n:
	if i%2==0:
		print(f"{i}^2 = {i**2}")
	i += 1