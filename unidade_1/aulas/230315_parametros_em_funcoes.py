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
#
#   print(a) -> conteúdo da função
#     |
# Os comandos que formam o corpo da função começam na linha seguinte e devem 
# ser indentados.
#
# * Em qualquer arquivo onde existam funções, elas sempre devem ficar no início
#   arquivo. Qualquer código que não seja parte de uma função, deverá ficar a-
#   baixo das funções.

# Função sem o uso de argumentos.
def soma_numeros_sem_argumentos():
    a = 10
    b = 20
    print(a + b)

# Função com o uso de argumentos.
def soma_numeros_com_argumentos(a: int, b: int):
    print(a + b)
