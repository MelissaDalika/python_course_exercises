#Esercizio 4: Verifica di una Password Sicura

def is_secure_password(password:str):
    """
    Verifica se la password è sicura.
    Criteri:
    - Almeno 8 caratteri
    - Al massimo 20 caratteri 
    - Almeno una lettera maiuscola
    - Almeno una lettera minuscola
    - Almeno un numero
    - Almeno un carattere speciale
    
    Args: password (str): La password da verificare.
    
    Returns:
    boolean: True per password sicura, False per pericolosa.
    """
    if len(password) < 8 or len(password) > 20:
        return False  # Deve avere almeno 8 caratteri ma un massimo di 20 (* aggiunta per evitare input lungo)
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/"
    
    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif character in special_characters:
            has_special = True
    
    return has_upper and has_lower and has_digit and has_special

#  Prova a scrivere una password
test_password = "Lamiapas#sword989"
print(is_secure_password(test_password))  # Output


# Other solution

def is_secure_password(password: str) -> bool:
    """
    Verifica se una password è sicura. *Any way :) oggetto itterable che restituisce un booleano*

    """
    if len(password) < 8 or len(password) > 20:
        return False  # Lunghezza non valida

    has_upper = any(char.isupper() for char in password)  
    has_lower = any(char.islower() for char in password)  
    has_digit = any(char.isdigit() for char in password)  
    has_special = any(char in "!@#$%^&*()-_=+[]{};:'\",.<>?/" for char in password) 

    return has_upper and has_lower and has_digit and has_special


