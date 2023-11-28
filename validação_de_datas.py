dia = int(input("Insira o dia: "))
mês = int(input("Insira o mes: "))
ano = int(input("Insira o ano: "))

if mês == 4 and dia > 30:
    print("A data não é valida")
elif mês == 2 and dia > 28:
    print("A data não é valida")
elif mês == 6 and dia > 30:
    print("A data não é valida")
elif mês == 9 and dia > 30:
    print("A data não é valida")
elif mês == 11 and dia > 30:
    print("A data não é valida")
elif dia > 0 and dia <= 31 and mês > 0 and mês <=12 and ano > 0 :
    print("A data: ", dia,"/",mês,"/", ano, "é valida")
else:
  print("A data não é valida")

  