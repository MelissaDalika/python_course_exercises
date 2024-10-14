# Esercizio 2: Convertitore di Unità (Temperatura)

def temperature_conversion_calc(value:float, unit_from:str, unit_to:str):
    """
    Converte la temperatura utilizzando un dizionario che associa le unità di partenza e di arrivo alle formule di conversione corrispondenti.
    
    Poi restituisce il risultato della conversione usando il metodo get del dizionario per cercare la funzione corrispondente alla coppia di unità (unit_from, unit_to).
    
    Se la coppia non esiste nel dizionario, restituisce una funzione lambda predefinita che ritorna una stringa.
    (value): Argomento risultato della conversione.

    """
    conversions = {
        ("celsius", "fahrenheit"): lambda c: c * 9/5 + 32,
        ("fahrenheit", "celsius"): lambda f: (f - 32) * 5/9,
        ("celsius", "kelvin"): lambda c: c + 273.15,
        ("kelvin", "celsius"): lambda k: k - 273.15
    }
    return conversions.get((unit_from, unit_to), lambda x: "Conversione non disponibile")(value)

if __name__ == "__main__":
    """
    L'espressione if __name__ == "__main__": è utilizzata per determinare se il modulo sta funzionando come programma principale. Se la condizione è vera (cioè il modulo è eseguito direttamente), il blocco di codice indentato sotto di essa verrà eseguito.
    """
    value = float(input("Inserisci il valore della temperatura: "))
    unit_from = input("Unità di partenza (Celsius, Fahrenheit, Kelvin): ").lower()
    unit_to = input("Unità di arrivo (Celsius, Fahrenheit, Kelvin): ").lower()
    
    print(f"Risultato: {temperature_conversion_calc(value, unit_from, unit_to)}")


