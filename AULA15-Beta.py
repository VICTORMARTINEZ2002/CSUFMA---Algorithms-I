#AULA 15-Beta.py
VETORES
Armazena em uma unica variavel + de 1 valor
espaço de momoria em que vc coloca os inteiros um do lado do outro, mesma complexidade de acesso pros mesmos elementos, mesmo desempenho computacional, isto é:armazena com acesso aleatorio;leva o mesmo tempo;
em p
v = [ ] 											#inicializar um vetor;
													#criour um vetor vazio;

primos = [2, 3, 5, 7, 11, 13, 19, 23, 29 ]
print(primos) #Imprime: [2, 3, 5, 7, 11, 13, 19, 23, 29 ]	


indexação:
print(primos[0]) #Imprime 2
print(primos[3]) #Imprime 7

primos[1]=8 #atribuição dentro de um vetor 

print(type(primos))    #list(estrutura de dados que python usa pra implementar vetores), em pytthon, um vetor é representado como listas  
print(type(primos[1])) #inteiro

x = primos[3] + primos[5]
print(x) #Imprime 20 (7 + 13)

#MANIPULAÇÃO DE STRINGS
STRING=cadeia de caracteres
universidade = "Federal do Maranhão"
print(universidade)     #Federal do Maranhão
print(universidade[0])  #F
print(universidade[18]) #o (ultimo)
print(universidade[-1]) #0 (ultimo)
print(universidade[-2]) #ã
len(universidade) #retorna o tamanho da string, quantos caracteres ela tem;
print(universidade[len(universidade)-1])#o(ultimo)    #len pega o tamanho da string universidade

#
print(universidade[0:7]) #Federal
print(universidade[:10]) #pega do 0 até o 10
print(universidade[3:])  #eral do Maranhão (pega do 3 até o final)

l = len(primos)
print(l)

s = universidade[:6] + universidade[10:]
print(s) #Federal Maranhão

#acessar as possições de um vetor


#------------------------------------------------
primos = [2, 3, 5, 7, 11, 13]
print(len(primos)) #Imprime quantos elementos o vetor tem

for i in range(len(primos)):
	print(primos[i], end=" ")
print()

for num in primos: #esse num é so um nome, pode ser outro
	print(num)

universidade = "Federal do Maranhão"
for c in universidade:
	print(c)


soma = 0
for num in primos:
	soma += num
print(soma)
ou
print(sum(v))


v = [12, 324, 5, 567, -10]
menor = v[0]
maior = v[0]

for num in v:
	if num<menor:
		menor = num
	if num>maior:
		maior = num
print(menor)
print(maior)
#ou
print(min(v))
print(max(v))

vOrdenado = sorted(v) #ordena de forma crescente
print(v)
print(sorted(v))




v = []
for i in range(1, 101):
	v.append(i) #adc no fim do vetor como um novo elemento
print(v)	

































