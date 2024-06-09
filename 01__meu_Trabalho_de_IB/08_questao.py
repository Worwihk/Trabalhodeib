numero1=int(input("Digite um número: "))
numero2=int(input("Digite outro número:"))
soma=numero1+numero2
subtracao=numero1-numero2
multiplicacao=numero1*numero2
divisao=numero1/numero2
print("Qual a operação: Soma,subtração,multiplicação ou divisão")
operacao=input(": ")
if len(operacao)>1 and len(operacao)<5:print(soma)
if len(operacao)>7 and len(operacao)<10:print(subtracao)
if len(operacao)>10:print(multiplicacao)
if len(operacao)>6 and len(operacao)<9:print(divisao) 