# Definição da lista
Lista_exemplo = [50, 4, 10, 100, 30, 95, 1000]

# Calculando a soma total
soma_total = sum(Lista_exemplo)

# Exibindo o resultado
print(f"A soma total é: {soma_total}")







# Definição da lista
Lista_exemplo = [50, 4, 10, 100, 30, 95, 1000]

# Variável acumuladora
soma_total = 0

# Passando por cada item da lista e somando
for numero in Lista_exemplo:
    soma_total += numero  # O mesmo que: soma_total = soma_total + numero

# Exibindo o resultado
print(f"A soma total é: {soma_total}")