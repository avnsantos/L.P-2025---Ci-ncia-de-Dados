# modulo.py

def fatorial(num: int) -> int:
    """
    Calcula o fatorial de um número inteiro de forma recursiva.

    A recursão é uma técnica onde uma função chama a si mesma. Funciona como uma
    pilha de chamadas (LIFO - Last-In, First-Out), onde cada chamada espera
    a próxima terminar.

    Parameters
    ----------
    num : int
        Um número inteiro não negativo.

    Returns
    -------
    int
        O valor do fatorial de `num`.

    Raises
    ------
    TypeError
        Se a entrada não for um número inteiro.
    ValueError
        Se a entrada for um número negativo.
    """
    if not isinstance(num, int):
        raise TypeError("O argumento deve ser um número inteiro.")
    
    if num < 0:
        # Fatorial não é definido para números negativos.
        raise ValueError("Fatorial não é definido para números negativos.")

    # Caso base: Fatorial de 0 e 1 é 1.
    if num <= 1:
        return 1
    
    # Passo recursivo: n * (n-1)!
    return num * fatorial(num - 1)
