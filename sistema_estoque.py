produto=[]
sair=False

print("bem vindo ao sistema de estoque")
while sair==False:
    print("-"*20)
    print("1-lista de produto")
    print("2-cadastrar um novo produto")
    print("3-deletar um produto")
    print("0-sair do sistema")
    opcao= input("sua opçao")
    match opcao:
        case '0':
            sair=True
        case'1' :
            for p in produto:
                print("- ", p)
            print("#"*30)
            input("pressione enter para continuar...")
        case '2':
            print("cadastro novo produto")
            nome_produto = input("nome do produto: ")
            produto.append(nome_produto) 
        case '3':
            print("remova produto")
            nome_produto=input("qual deletado:  ")
            if nome_produto in produto:
        
            produto.remove(nome_produto)
            print("removido com sucesso")
else:
            print(nome_produto,"nao existe na lista")
            input("pressione enter para continuar...")


        

    

