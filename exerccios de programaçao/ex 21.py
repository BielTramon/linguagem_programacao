valor1 = float(input("Digite um valor X"))
valor2 = float(input("Digite um valor Y"))
a = input("1 somar, 2 multiplicar, 3 maior, 4 menor, 5 sair ")
for i in range(1):
    if a == 1:
        soma=valor1+valor2
        print(soma)
    if a == 2:
        mult=valor1*valor2
        print(mult)
    if a == 3:
        if valor1 > valor2:
            m=valor1
            print(m)
        if valor2 > valor1:
            m=valor2
            print(m)
    if a == 4:
        if valor1 < valor2:
            me=valor1
            print(me)
        if valor2 < valor1:
            me=valor2
            print(me)
    if a == 5:
        break
