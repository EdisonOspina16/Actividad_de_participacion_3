# Cree una clase CuentaBancaria que contenga los siguientes atributos:
# numero_cuenta, propietarios y balance.
# Los tres atributos se deben inicializar en el constructor
# con valores recibidos como parámetros.

class CuentaBancaria:

    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

# Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
    def retirar(self, monto):
        pass

# Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo
# que aplique un porcentaje del 2% sobre el balance de la cuenta

    def aplicar_cuota_manejo(self):
        cuota_manejo = f"2% de {self.balance}"
        self.balance = self.balance - cuota_manejo

# Para la clase CuentaBancaria, ncree un método mostrar_detalles
# que imprima por consola los detalles de la cuenta bancaria.

    def mostrar_detalles(self):
        pass


