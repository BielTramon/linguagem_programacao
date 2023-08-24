nome = input("Digie seu nome")
horas = float(input("Digite quantas horas trabalhou"))
valor = float(input("Digite o valor ue vc ganhar a hora"))
salario = horas * valor
inss = salario * 0.02
salariof = salario - inss
print(nome,"ganha",salariof,"reais")