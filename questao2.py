def fibonacci(numero: int) -> bool:
    """
    Verifica se um número pertence à sequência de Fibonacci.

    Args:
    numero (int): O número a ser verificado.

    Returns:
    bool: True se o número pertence à sequência de Fibonacci, False caso contrário.
    """
    primeiro, segundo = 0, 1
    while primeiro <= numero:
        if segundo == numero or primeiro == numero:
            return True
        soma = primeiro + segundo
        primeiro, segundo = segundo, soma
    return False

numero = int(input("Digite o número: "))

if fibonacci(numero):
    print("O número {0} pertence à sequência de Fibonacci.". format(numero))
else:
    print("O número {0} não pertence à sequência de Fibonacci.". format(numero))

