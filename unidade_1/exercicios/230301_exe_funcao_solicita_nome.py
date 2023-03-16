# Crie uma função que peça o nome de uma pessoa e verifique se essa pessoa está
# proíbida de entrar no sistema. Michael é a única pessoa proíbida nesse momen-
# to.

def solicita_nome():
    nome = input("Digite seu nome: ")

    if nome.title() == "Michael":
        print("Você não tem autorização.")
    else:
        print("Bem vindo!")


solicita_nome()
