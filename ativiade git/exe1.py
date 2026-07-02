# Lista original fornecida
lista = [1, 3, 5, 3, 7, 9, 3]

# Recebe o número do usuário e converte para inteiro
numero_digitado = int(input("Digite um número: "))

# Conta as ocorrências do número na lista
ocorrencias = lista.count(numero_digitado)

# Exibe o resultado formatado
print(f"Número de ocorrências do número {numero_digitado} na lista: {ocorrencias}")