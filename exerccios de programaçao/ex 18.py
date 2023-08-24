#18) Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem
#peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi
#aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos.
nota1 = float(input("Digite sua nota"))
nota2 = float(input("Digite sua nota"))
nota3 = float(input("Digite sua nota"))
if (nota1 + nota2 > 10) and (nota1 + nota2 < 0):
    print("valores incorretos nas provas 1 e 2")
if (nota3 > 10) and (nota3 < 0):
    print("valores incorretos nas provas 1 e 2")
media = (nota1 + nota2 + nota3)/2
if media < 6:
    print("reprovado", media)
if media >= 6 and media < 10:
    print("aprovado", media)