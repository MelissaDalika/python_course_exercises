import math

class CalcArea:
    """
    Classe per calcolare l'area di figure geometriche: quadrato, rettangolo e cerchio.
    Gestisce errori di input non validi.
    """
    
    def __init__(self, fig: str, *dim) -> float:
        self.fig = fig.lower()
        self.dim = dim
        
    def calc_area_fig(self) -> str:
        """
        Calcola l'area in base alla figura scelta e alle dimensioni.
        """
        if self.fig == "quadrato":
            return self.area_quadrato()
        elif self.fig== "rettangolo":
            return self.area_rettangolo()
        elif self.fig == "cerchio":
            return self.area_cerchio()
        else:
            raise ValueError("Figura non valida! Scegli tra: quadrato, rettangolo, cerchio.")
    
    #def area_quadrato(self, lato):
        #return self.lato ** 2
    def area_quadrato(self) -> float:
        area = self.dim[0] ** 2
        return f"L'area del quadrato è {area:.2f} unità quadrate." #due decimali dopo il punto
    
    #def area_rettangolo(self, base, altezza):
        #return self.base * self.altezza
    def area_rettangolo(self) -> float:
        return self.dim[0] * self.dim[1]
    
    #def area_cerchio(self, raggio):
        #return math.pi * self.raggio ** 2
    def area_cerchio(self) -> float:
        return math.pi * self.dim[0] ** 2
    
class AreaRettangolo:
    """
    Classe per calcolare l'area di un rettangolo
    """
    
    def __init__(self, base: float, altezza: float):
        self.base = base
        self.altezza = altezza
        
    def calc_area(self) -> float:
        return self.base * self.altezza
    
    def __str__(self) -> str:
        return f"L'area del rettangolo è {self.calc_area()} unità quadrate."


quadrato = CalcArea("quadrato", 5)
print(quadrato.calc_area_fig())
rettangolo = CalcArea("rettangolo", 4, 6)
print(rettangolo.calc_area_fig())
cerchio = CalcArea("cerchio", 3)
print(cerchio.calc_area_fig())

rettangolo = AreaRettangolo(5,6)
print(rettangolo)  

# Other stamp solution - List

figure = [
    CalcArea("quadrato", 5),
    CalcArea("rettangolo", 4, 6),
    CalcArea("cerchio", 3)
]

for figura in figure:
    print(figura.calc_area_fig())
    
    
# Other solution - Reduce code

import math

class CalcArea:
    """
    Classe per calcolare l'area di figure geometriche: quadrato, rettangolo e cerchio.
    Gestisce errori di input non validi.
    """
    
    def __init__(self, fig: str, *dim) -> None:
        self.fig = fig.lower()
        self.dim = dim

    def calcola_area(self) -> str:
        """
        Calcola l'area in base alla figura scelta e restituisce una stringa formattata.
        """
        area = None
        
        if self.fig == "quadrato" and len(self.dim) == 1:
            area = self.dim[0] ** 2
            figura = "quadrato"
        elif self.fig == "rettangolo" and len(self.dim) == 2:
            area = self.dim[0] * self.dim[1]
            figura = "rettangolo"
        elif self.fig == "cerchio" and len(self.dim) == 1:
            area = math.pi * (self.dim[0] ** 2)
            figura = "cerchio"
        else:
            raise ValueError("Figura non valida o numero di dimensioni errato! Scegli tra: quadrato, rettangolo, cerchio.")

        return f"L'area del {figura} è {area:.2f} unità quadrate."  # Due decimali dopo il punto


# Creazione delle istanze delle figure e stampa delle aree
shapes = [
    CalcArea("quadrato", 5),
    CalcArea("rettangolo", 4, 6),
    CalcArea("cerchio", 3)
]

for shape in shapes:
    print(shape.calcola_area())
