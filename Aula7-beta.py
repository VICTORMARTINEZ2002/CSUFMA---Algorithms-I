# AULA 7: FUNÇÕES 16/05/22

#Revendo os codigos dos alunos que foram feitos na aula passada.

#OBSERVAÇÃO:
# O COMANDO MAP: (já foi usado antes, mas só foi propriamente ensinado nessa aula.)
# O comando "map" aplica uma função a um interador;
  A, B, C, D = map(int, input().split())
               map(função, interador)
# Nesse caso, aplicamos a função inteiro a entrada de dados input().split()
#"Lamba calculus: uma função é um tipo, igual ao tipo inteiro, bolleano, float, etc..."

# Só se pode usar a função map pra mesmos tipos de dados(int/float/bool/...)
#OU
# nome, idade = input().split()
# idade = int(idade)


#FUNÇÕES:
#O assunto funções já foi estudado anteriormente, porém agora vamos saber que a estamos usando.
#Exemplos:
  n = int('123')
  print(n+2)
  a, b = map(int, input())
#Elementos que compoem uma função: 
 #1. O nome dela; 
 #2. Os parametros dela;
  #Pode-se ter mais de 1 parametros, inclusive pode-se ter quantos parametors nos quisermos;

#Além disso, podemos criar nossas proprias funções:
 #1. Primeiro definir;
 #2. Depois chamar por ela;
#Por padrão, declaramos todas as funções que vamos usar no começo do codigo.

#EXEMPLO 1:
def soma(n1, n2): #colçocar só 1 parametro reuslta em erro
  return n1 + n2  #encerra a função e retorna n1 + n2

print( soma(34, 50) ) #incapsulamento, é bem interresante.

#EXEMPLO 2:
def incrementa(n):
  return n+1

print( incrementa(67) )  

#EXEMPLO 3:
def podeDirigir(idade):
  return idade>=18 #função de linha unica

print( podeDirigir(17) ) #False
print( podeDirigir(19) ) # True   





