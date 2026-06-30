
status_pedido = "pendente"

# Estrutura match/case para traduzir o status
match status_pedido:
    case "novo" | "pendente":
        print("Seu pedido está aguardando pagamento.")
    case "pago":
        print("Pagamento confirmado! Preparando envio.")
    case "enviado":
        print("Seu pedido já está a caminho.")
    case "entregue":
        print("Pedido finalizado.")
    case _:
        print("Status desconhecido.")