#2006
n = input()
r1, r2, r3, r4, r5 = input().split(" ")

v = [r1, r2, r3, r4, r5]
contador = 0
for elemento in v:
	if elemento == n:
		contador += 1

print(contador)	