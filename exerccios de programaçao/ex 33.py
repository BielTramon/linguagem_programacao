pessoas = 0
joao = 0
jose = 0
tiago = 0
jorge = 0
nulo = 0
branco = 0

while True:
    v = int(input(
        "Digite um numero correspodente ao canditado:"
        "\n1 joao \n2 josé \n3 tiago \n4 jorge\n5 voto nulo "
        "\n6 voto em branco \n7 sair\n digite aqui:  "))

    if v == 1:
        joao += 1
        pessoas += 1
    elif v == 2:
        jose = jose + 1
        pessoas += 1
    elif v == 3:
        tiago = tiago + 1
        pessoas += 1
    elif v == 4:
        jorge = jorge + 1
        pessoas += 1
    elif v == 5:
        nulo = nulo + 1
        pessoas += 1
    elif v == 6:
        branco = branco + 1
        pessoas += 1
    elif v == 7:
        break
    else:
        print("digite um valor valido")

print("\njoao",joao,"\njose",jose,"\ntiago",tiago,"\njorge",jorge,"\nnulo",nulo,"\nbranco",branco)
print(pessoas)

pn = pessoas/(nulo * 100)
print(pn* 100)