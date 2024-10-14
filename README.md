# python_course_exercise

Esercizio 1: Fizz Buzz FizzBuzz

Scrivi un programma che stampi i numeri da 1 a 100. Tuttavia:
• Per i multipli di 3 stampa "Fizz" al posto del numero.
• Per i multipli di 5 stampa "Buzz".
• Per i numeri multipli sia di 3 che di 5 stampa "FizzBuzz".
ESEMPIO:
• Output: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, ...

-------------------------

Esercizio 2: Convertitore di Unità (Temperatura)

Scrivi un programma che permetta all'utente di convertire temperature tra Celsius, Fahrenheit
e Kelvin. L'utente deve specificare l'unità di partenza e l'unità di arrivo, oltre al valore della
temperatura.
Formule:
• Da Celsius a Fahrenheit F = C ×9/5 + 32
• Da Fahrenheit a Celsius: C = (F − 32) × 95
• Da Celsius a Kelvin: K = C + 273.15
• Da Kelvin a Celsius: C = K − 273.15

ESEMPIO:
• Input: 100, "Celsius", "Fahrenheit"
• Output: 212

-------------------------

Esercizio 3: Somma di Numeri in una Stringa

Scrivi una funzione che prenda in input una stringa contenente numeri e altri caratteri (come
lettere o simboli) e restituisca la somma di tutti i numeri presenti nella stringa. Ignora tutti i
caratteri non numerici.
ESEMPIO:
• Input: "abc123def45"
• Output: 168
(in questo caso123 + 45 = 168)
SUGGERIMENTO:
• Usa un ciclo per analizzare carattere per carattere e costruisci i numeri quando trovi
cifre consecutive.

-------------------------

Esercizio 4: Verifica di una Password Sicura

Scrivi una funzione che verifichi se una password è sicura. La password deve:
• Avere almeno 8 caratteri.
• Contenere almeno una lettera maiuscola.
• Contenere almeno una lettera minuscola.
• Contenere almeno un numero.
• Contenere almeno un carattere speciale (ad es. @, #, $, ecc.).
Se la password è sicura, la funzione dovrebbe restituire True, altrimenti False.
ESEMPIO:
• Input: "P@ssw0rd"
• Output: True

-------------------------

Esercizio 5: Generatore di Numeri di Fibonacci

Scrivi una funzione che generi i primi n numeri della sequenza di Fibonacci. La sequenza di
Fibonacci inizia con 0 e 1, e ogni numero successivo è la somma dei due numeri precedenti.
ESEMPIO:
• Input: 10
• Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
Suggerimento:
• Usa un ciclo for per generare i numeri, memorizzando i valori precedenti.

-------------------------

Esercizio 6: Analisi delle Parole in un Testo

Scrivi un programma che prenda in input un testo (una stringa lunga) e restituisca le seguenti
informazioni:
1. Numero di parole totali.
2. Parola più lunga e parola più breve.
3. Frequenza di ciascuna parola (quante volte appare nel testo).
ESEMPIO:
• Input: "Python è fantastico. Python è divertente!"
• Output:
o Numero di parole: 5
o Parola più lunga: "fantastico"

o Parola più breve: "è"
o Frequenza: {'Python': 2, 'è': 2, 'fantastico.': 1, 'divertente!': 1}

Suggerimento:
• Usa il metodo split() per dividere le parole e rimuovi la punteggiatura per calcolare
correttamente le frequenze.

-------------------------

Esercizio 7: Trova la Parola Palindroma più Lunga

Scrivi una funzione che prenda una stringa e restituisca la parola palindroma più lunga
presente nella stringa. Se non ci sono palindromi, restituisci un messaggio che lo indichi.
ESEMPIO:
• Input: "Anna ama il suo kayak"
• Output: "kayak"
Suggerimento:
• Un palindromo è una parola che si legge uguale sia da sinistra a destra che da destra a
sinistra.

-------------------------

Esercizio 8: Somma di Matrici

Scrivi una funzione che prenda in input due matrici (rappresentate come liste di liste) e
restituisca la loro somma. La somma di due matrici è una nuova matrice ottenuta sommando
gli elementi corrispondenti delle due matrici.
ESEMPIO:
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
Output: [[6, 8], [10, 12]]
Suggerimento:
• Le due matrici devono avere le stesse dimensioni.

-------------------------

Esercizio 9: Crittografia di Cesare

Implementa un cifrario di Cesare, un semplice sistema di cifratura in cui ogni lettera di un
messaggio è spostata di un certo numero di posizioni nell'alfabeto. Scrivi una funzione che
prenda una stringa e un numero di spostamenti (shift) e restituisca la stringa cifrata.
ESEMPIO:
• Input: "abc", shift = 3
• Output: "def"
Suggerimento:

• Gestisci anche lo spostamento di lettere maiuscole e mantieni gli altri caratteri
invariati.

-------------------------

Esercizio 10: Trova le Coppie con Somma

Scrivi una funzione che prenda una lista di numeri e un numero target, e restituisca tutte le
coppie di numeri nella lista che sommano al target.
ESEMPIO:
• Input: lista = [2, 4, 3, 5, 7, 8, -1], target = 6
• Output: [(2, 4), (3, 3), (-1, 7)]
Suggerimento:
• Usa un set per memorizzare i numeri già visti e ottimizzare il tempo di esecuzione.

