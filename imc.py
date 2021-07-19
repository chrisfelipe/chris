while True:
    altura = float(input('''\033[1;33m
    Digite sua altura em Metros, usando um ponto para separar ex: 1.86 :'''))


    if altura == 0:
        print('\033[1;31mvalor invalido, digite uma altura valida !!!')
    else:
        break
    
while True:
    peso = float(input("Digite seu peso em Kg: "))
    
    if peso == 0:
        print('digite um valor valido, acima de 0!!!')
    else:
        break
 
imc = peso / (altura**2)


print('\033[1;33mseu imc é {:.1f}'.format(imc))
 
if imc < 16:
	print("Magreza grave")
elif imc < 17:
	print("Magreza moderada")
elif imc < 18.5:
	print("Magreza leve")
elif imc < 25:
	print("Saudável")
elif imc < 30:
	print("Sobrepeso")
elif imc < 35:
	print("Obesidade Grau I")
elif imc < 40:
	print("Obesidade Grau II (severa)")
else:
	print("Obesidade Grau III (mórbida)")