#16) Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
#para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
#conversão
escolha = input("Escola qual a forma de pedir temperatura 1 F para C , 2 C para F ")
if escolha == "1":
    F1 = float(input("Digite uma temperatura em F"))
    C1 = (F1 - 32)/1.8
    print(C1)
if escolha == "2":
    C2 = float(input("Digite uma temperatura em C"))
    F2 = (C2 * 1.8 + 32)
    print(F2)