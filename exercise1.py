# Esercizio 1: Fizz Buzz FizzBuzz

def fizz_buzz():
    """
    Stampa i numeri da 1 a 100 con le seguenti condizioni:
    - Se il numero è multiplo di 3, stampa "Fizz".
    - Se il numero è multiplo di 5, stampa "Buzz".
    - Se il numero è multiplo sia di 3 che di 5, stampa "FizzBuzz".
    """
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz", end=", ")
        elif n % 3 == 0:
            print("Fizz", end=", ")
        elif n % 5 == 0:
            print("Buzz", end=", ")
        else:
            print(n, end=", ")

fizz_buzz()







