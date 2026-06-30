# O loop principal continua rodando até que o número seja 1 ou menor
while True:
    # Pede o número ao usuário e converte para float
    numero = float(input("Digite um número par (ou <= 1 para sair): "))
    
    # Condição de saída do loop: se o número for 1 ou menos
    if numero <= 1:
        print("Número igual ou menor que 1. Saindo do loop...")
        break
        
    # Verifica se o número digitado é par
    # (Usamos o resto da divisão % 2 para saber se é par)
    if numero % 2 == 0:
        print(f"Número inicial: {numero}")
        
        # Loop interno para dividir o número por 2 até chegar a 1 ou menos
        while numero > 1:
            numero = numero / 2
            print(f"Dividido por 2 = {numero}")
            
        print("--- Divisões concluídas para este número! ---\n")
    else:
        print("Esse número não é par! Tente novamente.\n")