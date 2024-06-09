aluno=input("Nome do aluno: ")
diciplina=input("Qual a diciplina: ")
nota1=int or float(input("Qual a nota parcial do aluno: "))
nota2=int or float(input("Qual a nota bimestral do aluno: "))
media=(nota1+nota2)/2
situacao1=aluno+" "+"Esta aprovado na diciplina de"+" "+diciplina
situacao2=aluno+" "+"Esta reprovado na diciplina de"+" "+diciplina
if media>=6 and media<11:print(situacao1)
if media>=0 and media<6:print(situacao2)
if media<0 or media>10:print("Essa nota não existe")