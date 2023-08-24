#20) Leia a idade e o tempo de servic¸o de um trabalhador e escreva se ele pode ou nao se aposentar.
#As condições para aposentadoria são:
#• Ter pelo menos 65 anos,
#• Ou ter trabalhado pelo menos 30 anos,
#• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input("Digite sua idade: "))
temp = int(input("digite seu tempo de serviço em anos: "))
if idade >= 65:
    print("pode se aposentar: ")
if temp >= 30:
    print("ja pode se aposentar")
if (idade >= 60) and (temp >= 25):
    print("ja pode se aposentar")
if (idade < 60) and (temp < 25):
    print("nao pode se aposentar")