# Esercizio 5: Generatore di Numeri di Fibonacci

def fibonacci(n:int):
    """
    Genera i primi n numeri della sequenza di Fibonacci.
    
    Args:
    n (int): Il numero di elementi da generare.
    
    Returns:
    list: Una lista contenente i numeri di Fibonacci.
    """
    fib_sequence = []
    
    a, b = 0, 1  # I primi due numeri di Fibonacci
    for _ in range(n):
        fib_sequence.append(a)  # Aggiungi il numero corrente alla sequenza
        a, b = b, a + b  # Aggiorna i valori
    
    return fib_sequence

# Test della funzione
n = 15
print(fibonacci(n))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
