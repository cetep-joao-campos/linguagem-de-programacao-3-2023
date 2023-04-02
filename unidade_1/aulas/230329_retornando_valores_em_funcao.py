# Retornando valores em funções
# Ao retornar informações processadas em uma função,
# outras funções podem se beneficiar dessas informa-
# ções processadas para realizar algum procedimento.

def soma_numeros(a: int, b: int):
    soma = a + b

    return soma

def media():
    media = soma_numeros(5, 9) / 2

    return media


print(media())
