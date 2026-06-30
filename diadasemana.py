print("menu da semana")
print("domingo")
print("segunda")
print("terca")
print("quarta")
print("quinta")
print("sexta")
print("sabado")






dia_semana=input("digite dia semana")



match dia_semana:
    case "1":
       print ("Domingo")
    case "2":
       print ("Segunda-feira")
    case "3":
       print ("Terça-feira")
    case "4":
       print ("Quarta-feira")
    case "5":
       print ("Quinta-feira")
    case "6":
       print ("Sexta-feira")
    case "7":
       print ("Sábado")
    case _:
       print ("Opção inválida! Digite um número de 1 a 7.")

