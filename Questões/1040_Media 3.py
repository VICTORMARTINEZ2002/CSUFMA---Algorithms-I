#PROBLEMA 1040 - MÉDIA 3:
N1, N2, N3, N4 = map( float, input().split() )
media1 = (N1*2 + N2*3 + N3*4 + N4*1)/(2 + 3 + 4 + 1)
print(f"Media: {media1:.1f}")

if (media1 >= 7):
	print("Aluno aprovado.")
if (media1 < 5):
	print("Aluno reprovado.")
if ( (media1 < 7) and (media1 >= 5) ):
	print("Aluno em exame.")
	NE = float(input())
	print(f"Nota do exame: {NE}")
	media2 = float((media1 + NE)/2)
	if (media2 >= 5):
		print("Aluno aprovado.")
	else:
		print("Aluno reprovado.")

	print(f"Media final: {media2:.1f}")	