# Baseado na função que soma dois números, crie as seguintes funções:
# - Subtração;
# - Divisão;
# - Multiplicação;

def soma_numeros(a: int, b: int):
    print(a + b)

def subtrai_numeros(a: int, b: int):
    print(a - b)

def multiplica_numeros(a: int, b: int):
    print(a * b)

def divide_numeros(a: int, b: int):
    print(a / b)


# Criação de um menu para o aplicativo utilizando o laço de repetição while.

opcao = None

while opcao != 'sair':
    print("MENU de apps")
    print("1 - Somar números;")
    print("2 - Subtrair números;")
    print("3 - Multiplicar números;")
    print("4 - Divide números.")
    print("Digite sair para finalizar o programa.")
    opcao = input("--> ")