altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo f ou m")
if sexo == "f":
    pf = (62.1 * altura)-44.7
    print(pf)
if sexo == "m":
    pf = (72.7 * altura)-58
    print(pf)
