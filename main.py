class Asiento:
    def __init__(self, color: str, precio: int, registro: int):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevoColor: str):
        colores_permitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if nuevoColor.lower() in colores_permitidos:
            self.color = nuevoColor



class Motor:
    def __init__(self, numeroCilindros: int, tipo: str, registro: int):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevoRegistro: int):
        self.registro = nuevoRegistro
    def asignarTipo(self, nuevoTipo: str):
        if nuevoTipo in ["electrico", "gasolina"]:
            self.tipo = nuevoTipo

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo: str, precio: int, asientos: list, marca: str, motor: Motor, registro: int):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
            return sum(isinstance(asiento, Asiento) for asiento in self.asientos)
        
    def verificarIntegridad(self):
        registroComparar = self.registro

        if self.motor.registro != registroComparar:
            return "Las piezas no son originales"
        for asiento in self.asientos:
            if self.asiento.registro != registroComparar:
                return "Las piezas no son originales"
                
        return "Auto original" 



