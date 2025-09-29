from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre: str):
        self.nombre = nombre

    @abstractmethod
    def calcularSalarioMensual(self) -> float:
        pass

    def __str__(self) -> str:
        return f"Empleado: {self.nombre}"

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre: str, salarioAnual: float):
        super().__init__(nombre)
        self.salarioAnual = salarioAnual

    def calcularSalarioMensual(self) -> float:
        return self.salarioAnual / 12

    def __str__(self) -> str:
        return f"[Tiempo Completo] {self.nombre}, Salario Anual: {self.salarioAnual:.2f}"

class EmpleadoTiempoHorario(Empleado):
    def __init__(self, nombre: str, horasTrabajadas: float, tarifaHora: float):
        super().__init__(nombre)
        self.horasTrabajadas = horasTrabajadas
        self.tarifaHora = tarifaHora

    def calcularSalarioMensual(self) -> float:
        return self.horasTrabajadas * self.tarifaHora

    def __str__(self) -> str:
        return f"[Tiempo Horario] {self.nombre}, Horas: {self.horasTrabajadas}, Tarifa: {self.tarifaHora:.2f}"

def main():
    empleados = []

    
    for i in range(3):
        nombre = input(f"Ingrese el nombre del empleado tiempo completo {i+1}: ")
        salarioAnual = float(input("Ingrese el salario anual: "))
        empleados.append(EmpleadoTiempoCompleto(nombre, salarioAnual))

    
    for i in range(2):
        nombre = input(f"Ingrese el nombre del empleado por horas {i+1}: ")
        horas = float(input("Ingrese las horas trabajadas: "))
        tarifa = float(input("Ingrese la tarifa por hora: "))
        empleados.append(EmpleadoTiempoHorario(nombre, horas, tarifa))

    
    print("\n--- Nómina de Empleados ---")
    for emp in empleados:
        print(f"{emp.nombre}: Salario mensual = {emp.calcularSalarioMensual():.2f}")


if __name__ == "__main__":
    main()
