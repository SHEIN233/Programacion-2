import math
class Vector:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)
        
    def __matmul__(self, other: "Vector") -> float:  
    
        return self.x * other.x + self.y * other.y

    def __xor__(self, other: "Vector") -> float:  
        return self.x * other.y - self.y * other.x

    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def is_perpendicular(self, other: "Vector") -> bool:
        return math.isclose(self @ other, 0.0)

    def is_parallel(self, other: "Vector") -> bool:
        return math.isclose(self ^ other, 0.0)

    def projection(self, other: "Vector") -> "Vector":
        factor = (self @ other) / (other.length()**2)
        return Vector(factor * other.x, factor * other.y)

    def component(self, other: "Vector") -> float:
        return (self @ other) / other.length()

    def __repr__(self) -> str:
        return f"Vector({self.x:.2f}, {self.y:.2f})"

a = Vector(3, 4)
b = Vector(-4, 3)

print("a =", a)
print("b =", b)

print("a · b =", a @ b)
print("a × b =", a ^ b)

print("¿Perpendiculares?", a.is_perpendicular(b))
print("¿Paralelos?", a.is_parallel(b))

print("Proyección de a sobre b:", a.projection(b))
print("Componente de a sobre b:", a.component(b))
