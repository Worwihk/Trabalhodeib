print("A hora deve ser infirmada no formato de número inteiro de 0 a 23 ex:1") 
hora=int(input("Que horas são: "))
if hora>=0 and hora<12:print("Agora é manhã")
if hora>=12 and hora<18:print("Agora é tarde")
if hora>=18:print("Agora é noite")