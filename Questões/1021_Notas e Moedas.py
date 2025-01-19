#PROBLEMA 1021 - NOTAS E MOEDAS:
inteiros, decimais = input().split(".")
inteiros = int(inteiros)
decimais = int(decimais)

#NOTAS:
QT_NOTA_100 = (inteiros // 100)
RESTO_100   = (inteiros - (QT_NOTA_100 * 100))

QT_NOTA_050 = (RESTO_100 // 50)
RESTO_050   = (RESTO_100 - (QT_NOTA_050 * 50))

QT_NOTA_020 = (RESTO_050 // 20)
RESTO_020   = (RESTO_050 - (QT_NOTA_020 * 20))

QT_NOTA_010 = (RESTO_020 // 10)
RESTO_010   = (RESTO_020 - (QT_NOTA_010 * 10))
											  # COLOCAR O CODIGO DA SEGUINTE FORMA ESTÁ INCORRETO:
QT_NOTA_005 = (RESTO_010 // 5)                #  QT_NOTA_005 = (RESTO_010 // 05)                   
RESTO_005   = (RESTO_010 - (QT_NOTA_005 * 5)) #  RESTO_005   = (RESTO_010 - (QT_NOTA_005 * 05))
											  # "SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers"
QT_NOTA_002 = (RESTO_005 // 2)
RESTO_002   = (RESTO_005 - (QT_NOTA_002 * 2))

QT_MOEDA_1_00  = (RESTO_002  // 1)
RESTO_1_00     = (RESTO_002 - (QT_MOEDA_1_00 * 1)) #DESNECESSARIO

#MOEDAS:
QT_MOEDA_0_50  = int( (decimais) // (0.50 * 100))
RESTO_0_50     = int( (decimais) - (QT_MOEDA_0_50 * (0.50 * 100) ) )

QT_MOEDA_0_25  = int( (RESTO_0_50 ) // (0.25 * 100))
RESTO_0_25     = int( (RESTO_0_50 ) - (QT_MOEDA_0_25 * (0.25 * 100) ) )

QT_MOEDA_0_10  = int( (RESTO_0_25 ) // (0.10 * 100))
RESTO_0_10     = int( (RESTO_0_25 ) - (QT_MOEDA_0_10 * (0.10 * 100) ) )

QT_MOEDA_0_05  = int( (RESTO_0_10 ) // (0.05 * 100))
RESTO_0_05     = int( (RESTO_0_10 ) - (QT_MOEDA_0_05 * (0.05 * 100) ) )

QT_MOEDA_0_01  = int( (RESTO_0_05 ) // (0.01 * 100))
RESTO_0_01     = int( (RESTO_0_05 ) - (QT_MOEDA_0_01 * (0.01 * 100) ) ) #DESNECESSARIO

#Saida:
print("NOTAS:")
print(f"{QT_NOTA_100} nota(s) de R$ 100.00")
print(f"{QT_NOTA_050} nota(s) de R$ 50.00" )
print(f"{QT_NOTA_020} nota(s) de R$ 20.00" )
print(f"{QT_NOTA_010} nota(s) de R$ 10.00" )
print(f"{QT_NOTA_005} nota(s) de R$ 5.00"  )
print(f"{QT_NOTA_002} nota(s) de R$ 2.00"  )
print("MOEDAS:")
print(f"{QT_MOEDA_1_00} moeda(s) de R$ 1.00")
print(f"{QT_MOEDA_0_50} moeda(s) de R$ 0.50")
print(f"{QT_MOEDA_0_25} moeda(s) de R$ 0.25")
print(f"{QT_MOEDA_0_10} moeda(s) de R$ 0.10")
print(f"{QT_MOEDA_0_05} moeda(s) de R$ 0.05")
print(f"{QT_MOEDA_0_01} moeda(s) de R$ 0.01")

''' 
Tentativa 01:
	#OBS, TERIA QUE USAR O IF, QUE É UM CONTEUDO QUE AINDA N VI
 	 #LOGO ESSE METODO NÃO CONVÉM AGORA
	QT_MOEDA_1_00  = (RESTO_002  // 01)
	RESTO_1_00     = (RESTO_002 - (QT_MOEDA_1_00 * 01))

	TESTE_MOEDA_0_50  = (RESTO_1_00 / (0.5 ** -1) )
	#SE O TESTE FOR > 1, TEMOS 1 MOEDA DE 50Centavos
	#SE O TESTE FOR < 1, TEMOS 0 MOEDA DE 50Centavos

tentativa 02: Não fazer sPLIT, usar apenas n=float(input())
			  Provavelmente possivel, porém mais trabalhoso	
QT_MOEDA_0_50  = ( (RESTO_1_00 * 100) // (0.50 * 100))
RESTO_0_50     = ( (RESTO_1_00 * 100) - (QT_MOEDA_0_50 * (0.50 * 100) ) )

QT_MOEDA_0_20  = ( (RESTO_0_50 * 100) // (0.20 * 100))
RESTO_0_20     = ( (RESTO_0_50 * 100) - (QT_MOEDA_0_20 * (0.20 * 100) ) )

QT_MOEDA_0_10  = ( (RESTO_0_20 * 100) // (0.10 * 100))
RESTO_0_10     = ( (RESTO_0_20 * 100) - (QT_MOEDA_0_10 * (0.10 * 100) ) )

QT_MOEDA_0_05  = ( (RESTO_0_10 * 100) // (0.05 * 100))
RESTO_0_05     = ( (RESTO_0_10 * 100) - (QT_MOEDA_0_05 * (0.05 * 100) ) )

QT_MOEDA_0_01  = ( (RESTO_0_50 * 100) // (0.01 * 100))
RESTO_0_01     = ( (RESTO_0_50 * 100) - (QT_MOEDA_0_01 * (0.01 * 100) ) )

'''