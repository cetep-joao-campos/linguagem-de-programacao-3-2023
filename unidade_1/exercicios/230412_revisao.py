"""
Faça um programa, com uma função que
necessite de um argumento. A função
retorna o valor de caractere ‘P’, 
se seu argumento for positivo, e ‘N’, 
se seu argumento for zero ou negativo. 
"""
def positivo_ou_negativo(n: int):
    if n > 0:
        print("P")
    else:
        print("N")

positivo_ou_negativo(int(input("Digite um número: ")))
