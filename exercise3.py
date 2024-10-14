#Esercizio 3: Somma di Numeri in una Stringa

def sum_of_numbers_in_string(stringa: str):
    """
    Calcola la somma di tutti i numeri presenti in una stringa.
    Args: stringa (str): La stringa contenente numeri e caratteri.
    """
    total = 0  # Inizializza somma a zero
    current_number = ""  # Stringa per memorizzare i numeri che trova

    for character in stringa:  # Ciclo che itera su ogni carattere della stringa
        if character.isdigit():  # Verifica se il carattere è una cifra, metodo boolean True se numero*
            current_number += character  # Aggiunge la cifra alla stringa corrente
        else:
            if current_number:  # Se c'è un numero corrente
                total += int(current_number)  # Aggiunge il numero alla somma
                current_number = ""  # Reset al numero corrente 

    if current_number:  # Aggiunge l'ultimo numero se presente
        total += int(current_number)

    return int(total)

# Change input
input_string = "4faw556ggfd8gsf31v5c"
print(f"Somma dei numeri nella stringa: {sum_of_numbers_in_string(input_string)}")  # Output


def sum_of_numbers_in_string(stringa: str):
    """
    Calcola la somma di tutti i numeri presenti in una stringa.
    
    Args:
    stringa (str): La stringa contenente numeri e caratteri.
    
    Returns:
    int: La somma dei numeri trovati nella stringa.
    """
    total = 0  # Inizializza somma a zero
    current_number = ""  # Stringa per memorizzare i numeri trovati
    index = 0  # Indice per scorrere la stringa

    while index < len(stringa):  # Continua finché ci sono caratteri nella stringa
        character = stringa[index]  # Ottieni il carattere corrente
        
        if character.isdigit():  # Verifica se il carattere è una cifra
            current_number += character  # Aggiungi la cifra alla stringa corrente
        else:
            if current_number:  # Se c'è un numero corrente
                total += int(current_number)  # Aggiungi il numero alla somma
                current_number = ""  # Reset al numero corrente
        
        index += 1  # Incrementa l'indice per passare al carattere successivo

    if current_number:  # Aggiunge l'ultimo numero se presente
        total += int(current_number)

    return total  # Ritorna la somma finale

# Esempio di input
input_string = "4faw556ggfd8gsf31v5c"
print(f"Somma dei numeri nella stringa: {sum_of_numbers_in_string(input_string)}")  # Output: 604

