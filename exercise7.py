# Esercizio 7: Trova la Parola Palindroma più Lunga

def longest_palindrome(sentence: str):
    """
    Trova la parola palindroma più lunga in una frase.
    Args: sentence (str): Frase.
    """
    words = sentence.split()
    longest_palindrome = ""

    for word in words:
        cleaned_word = ''.join(char.lower() for char in word if char.isalnum())  # Rimuove la punteggiatura
        if cleaned_word == cleaned_word[::-1] and len(cleaned_word) > len(longest_palindrome): #Questo è un modo per invertire la stringa. La notazione [::-1] crea una nuova stringa che è l'inverso della cleaned_word. Se la parola è uguale alla sua versione invertita, significa che è un palindromo.
            longest_palindrome = cleaned_word

    return longest_palindrome if longest_palindrome else "Nessun palindromo."


# Test della funzione
input_sentence = "Reconocer que somos seres humanos"
print(longest_palindrome(input_sentence))
