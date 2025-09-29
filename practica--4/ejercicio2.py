import math
import random
from abc import ABC, abstractmethod

class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self) -> str:
        pass

class Figura(ABC):
    def __init__(self, color: str = "sin color"):
        self.color = color

    def setColor(self, color: str):
        self.color = color

    def getColor(self) -> str:
        return self.color

    def __str__(self):
        return f"Figura de color {self.color}"

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado: float, color: str = "rojo"):
        super().__init__(color)
        self.lado = lado

    def area(self) -> float:
        return self.lado ** 2

    def perimetro(self) -> float:
        return 4 * self.lado

    def comoColorear(self) -> str:
        return "Colorear los cuatro lados"

    def __str__(self):
        return f"Cuadrado de lado {self.lado}, color {self.color}"

class Circulo(Figura):
    def __init__(self, radio: float, color: str = "azul"):
        super().__init__(color)
        self.radio = radio

    def area(self) -> float:
        return math.pi * self.radio ** 2

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Circulo de radio {self.radio}, color {self.color}"

def main():
    figuras = []

    for _ in range(5):
        tipo = random.choice([1, 2])  
        if tipo == 1:
            lado = random.randint(1, 10)
            figuras.append(Cuadrado(lado))
        else:
            radio = random.randint(1, 10)
            figuras.append(Circulo(radio))

    
    for fig in figuras:
        print(fig)
        print(f"Área: {fig.area():.2f}, Perímetro: {fig.perimetro():.2f}")
        if isinstance(fig, Coloreado):
            print("Coloreado:", fig.comoColorear())
        print("-" * 40)


if __name__ == "__main__":
    main()
