#MINHA RESPOSTA:
Find_um = -1
find_dois = -1

while (Find_um == -1):
    m = str(input("Insira Um Número Do Tipo Float: "))
    Find_um = m.find(".")
    find_dois = m.find(".", Find_um + 1, len(m))

    if find_dois != -1:
        Find_um = -1
        find_dois = -1
        continue

    if (Find_um == 0):
        Pint = 0
        Pdcm = str(m[1:len(m)])
        if Pdcm.isnumeric():
            break
        else:
            Find_um = -1
            find_dois = -1
            continue

    if (Find_um > 0):
        Pint, Pdcm = map(str, m.split("."))
        if Pint.isnumeric() and Pdcm.isnumeric():
            break
        else:
            Find_um = -1
            find_dois = -1
            continue

if (Find_um == 0):
    Pint = 0
    Pdcm = str(m[1:len(m)])
else:            
    Pint, Pdcm = map(str, m.split("."))
    Pint = int(Pint)
    Pdcm = int(Pdcm)
n = Pint + ((int(Pdcm)) * (10 ** (-len(str(Pdcm)))))
print(n)   

#RESPOSTA DO MANO ANDREI:
num=input("Insira float\n")
numstring=str(num)
count=num.count(".")
caracteres="."
first=num[0].isnumeric()
last=num[-1].isnumeric()
for x in range(len(caracteres)):
    numstring = numstring.replace(caracteres[x],"")
numeric=numstring.isnumeric()
while count!=1 or numeric==False or first==False or last==False:
    num=input("Insira float\n")    
    count=num.count(".")
    numstring=str(num)
    first=num[0].isnumeric()
    last=num[-1].isnumeric()
    for x in range(len(caracteres)):
        numstring = numstring.replace(caracteres[x],"")
    numeric=numstring.isnumeric()


#Resposta do prof:
while True:
    try:
        n = float(input("Informe um real: "))
        break
    except:
        print("Digite no formato certo o número real.")    