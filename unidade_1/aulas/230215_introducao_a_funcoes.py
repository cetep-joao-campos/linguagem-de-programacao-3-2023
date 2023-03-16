# A palavra reservada def inicia a definição de uma função. Ela deve ser 
# seguida do nome da função e da lista de parâmetros formais entre parênteses.
# Os comandos que formam o corpo da função começam na linha seguinte e devem
# ser indentados.
# https://docs.python.org/pt-br/3/tutorial/controlflow.html#defining-functions
#
# def nome_da_funcao(a: int):
#   print(a)
#
#
# nome da função  argumento
#           |        |   
# def nome_da_funcao(a: int):
#  |                     |
# inicialização    tipo de dado do argumento
#   print(a) -> conteúdo da função

def pega_nome():
    nome = input("Nome: ")
    print("Olá " + nome + ", seja bem vindo!")

def soma_lista(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    print(f"Os itens somados totalizou em {soma}")


numeros = [4, 3, 8, 7]

soma_lista(numeros)