class ecuacionlineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def solucion(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0

    def X(self):
        return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)

    def Y(self):
        return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)

valores = input("ingrese a, b, c, d, e, f separados: ").split()
a, b, c, d, e, f = map(float, valores)

eq = ecuacionlineal(a, b, c, d, e, f)

if eq.solucion():
    print("La solución del sistema es:")
    print("x =", eq.X())
    print("y =", eq.Y())
else:
    print("La ecuación no tiene solución")
