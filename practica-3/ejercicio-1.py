import random
class Juego:
    def __init__(self, numeroDeVidas: int):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        print(" Reiniciando partida...")
        self.numeroDeVidas = 3  

    def actualizaRecord(self):
        self.record += 1
        print(f" Nuevo récord: {self.record}")

    def quitaVida(self) -> bool:
        self.numeroDeVidas -= 1
        if self.numeroDeVidas > 0:
            print(f" Te equivocaste. Te quedan {self.numeroDeVidas} vidas.")
            return True
        else:
            print(" Te quedaste sin vidas...")
            return False

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas: int):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        print(" Bienvenido al Juego Adivina Número!")
        print("Debes adivinar un número entre 0 y 10.")

        while True:
            intento = int(input(" Ingresa tu número: "))

            if intento == self.numeroAAdivinar:
                print(" ¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                if not self.quitaVida():
                    break
                else:
                    if intento < self.numeroAAdivinar:
                        print(" El número a adivinar es MAYOR.")
                    else:
                        print(" El número a adivinar es MENOR.")

class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()

if __name__ == "__main__":
    Aplicacion.main()
