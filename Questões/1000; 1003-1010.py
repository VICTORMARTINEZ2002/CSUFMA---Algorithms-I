#PROBLEMA 1000 - Hello World!:
print("Hello World!")

#PROBLEMA 1003 - SOMA:
A = int(input())
B = int(input())
SOMA = A + B
print(f"SOMA = {SOMA}")

#PROBLEMA 1004 - PRODUTO:
A = int(input())
B = int(input())
PROD = A * B
print(f"PROD = {PROD}")

#PROBLEMA 1005 - MÉDIA:
A = float(input())
B = float(input())
MEDIA = ( (3.5 * A) + (7.5 * B) )/11
print(f"MEDIA = {MEDIA:.5f}")

#PROBLEMA 1006 - MÉDIA 2:
A = float(input())
B = float(input())
C = float(input())
MEDIA = ( (2 * A) + (3 * B) + (5 * C) )/10
print(f"MEDIA = {MEDIA:.1f}")

#PROBLEMA 1007 - DIFERENÇA:
A = int(input())
B = int(input())
C = int(input())
D = int(input())
DIFERENCA = ( (A * B) - (C * D) )
print(f"DIFERENCA = {DIFERENCA}")

#PROBLEMA 1008 - SALARIO:
NUMBER         =   int(input())
WORKED_HOURS   =   int(input())
ONE_HOUR_PRICE = float(input())
SALARY = WORKED_HOURS * ONE_HOUR_PRICE
print(f"NUMBER = {NUMBER}")
print(f"SALARY = U$ {SALARY:.2f}")

#PROBLEMA 1009 - SALARIO COM BONUS:
NOME         = str(input())
SALARIO_FIXO = float(input())
TOTAL_VENDAS = float(input())
TOTAL        = ( SALARIO_FIXO + (0.15 * TOTAL_VENDAS) )
print(f"TOTAL = R$ {TOTAL:.2f}")

#PROBLEMA 1010 - CALCULO SIMPLES:
CODIGO1, NUMERO1, VALOR1 = input().split(" ")
CODIGO1 = int(CODIGO1)
NUMERO1 = int(NUMERO1)
VALOR1  = float(VALOR1)

CODIGO2, NUMERO2, VALOR2 = input().split(" ")
CODIGO2 = int(CODIGO2)
NUMERO2 = int(NUMERO2)
VALOR2 = float(VALOR2)

VALOR_A_PAGAR = ( (NUMERO1 * VALOR1) + (NUMERO2 * VALOR2) )
print(f"VALOR A PAGAR: R$ {VALOR_A_PAGAR:.2f}")























































