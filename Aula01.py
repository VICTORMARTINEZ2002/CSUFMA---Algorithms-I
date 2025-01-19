#Assuntos Novos Nessa Aula:
#print()
#print("\n")
#atribuição
#atribuições multiplas
#atribuição em cascata


#Exercício 2.1: Imprimir "Olá Mundo!"
print("Hello world!")
print("\n\n\n")
print()

#OBS: #isso vai ser ignorado, comentario

#Exercício 2.2: Imprimir seu nome
print("Victor josé")
print()
print("UFMA")
print("\n")

#Exercício 2.3: Imprimir o resultado de uma expressão aritmética
print("14+56")
print(14+56)
print(45-18)
print(5*6)
print(8/2)
print(10/3)
print("\n")

#Exercício 2.4: Imprimir a concatenação de cadeias de caracteres
print('Computação' + ' UFMA')
print(' DEINF' * 3)
print("\n")

#Explicação sobre existem duas aspas, a simples e a dupla
print('"Victor"')
print("'Victor'")
print(" \"VICTOR\" ")

#Observação: caracters de escape
print("\n") #NOVA LINHA
print("\t") #TABULAÇÃO
print("\"")
print("\'") 
print("\n")

#VARIAVEIS(caderno)

#atribuição a variaveis
idade = 20
print(idade)
print(idade + 3)
print("idade")

#alterar o valor de uma variavel já existemte
idade = 31
print(idade)

print("VICTOR", idade, 2*idade)


#Aplicação prática
Valorunidade = 35 #valor unidade de um produto
produtoscomprados = 3 #quantidade de produtos vendidos
total =  produtoscomprados * Valorunidade
print(total)

#demonstração de um erro:
Valorunidade = 39
print(total) #não vai atualizar o valor total pois ele total ja foi atribuido antes da nova atribuição de total
print("\n")
#como deveria ser feito para evitar o erro:
Valorunidade = 39
total =  produtoscomprados * Valorunidade
print(total)

#----------------------------------------------------------------------------------------------------------------------#

#Como inverter os valores de duas variaveis?
pesoMaria = 54 #inverter esses valores
pesoJoana = 67

#tentativa 1:
pesoMaria = 54 #inverter esses valores
pesoJoana = 67

pesoMaria = pesoJoana #aqui, peso de maria fica 67
pesoJoana = pesoMaria #aqui, peso de joana recebe 67
print(pesoMaria, pesoJoana)

#Solução uiltilizando uma sacada matemática, só funcionava pra variaveis númericas:
pesoMaria = 54 #inverter esses valores
pesoJoana = 67

pesoJoana = pesoJoana + pesoMaria
pesoMaria = pesoJoana - pesoMaria
pesoJoana = pesoJoana - pesoMaria
print("\n")


#Solução criando outra variavel auxiliar:
pesoMaria = 54 #inverter esses valores
pesoJoana = 67

troca=pesoMaria
pesoMaria = pesoJoana
pesoJoana = troca
print(pesoMaria, pesoJoana)

#solução usando 2 variaveis auxiliares:
pesoMaria = 54 #inverter esses valores
pesoJoana = 67

novopesomaria = pesoJoana
novopesojoana = pesoMaria
pesoMaria = novopesomaria
pesoJoana = novopesojoana

#solução mais prática, atribuições multiplas:
pesoMaria = 54 #inverter esses valores
pesoJoana = 67
pesoMaria, pesoJoana = pesoJoana, pesoMaria
print(pesoMaria, pesoJoana)

#Atribuição Multiplas:
a, b, c, d = 1, 2*3, 1-5, 1/7
#Que é o mesmo de fazer:
a = 1
b = 2*3
c = 1-5
d = 1/7

#Atribuição em cascata:
a = b = c = d = 1
print(a, b, c, d)
