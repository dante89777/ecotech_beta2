from datetime import date

class Empleado:

    def __init__(
        self,
        rut,
        nombre,
        fecha_ingreso,
        sueldo_base
    ):
        self.rut = rut
        self.nombre = nombre
        self.fecha_ingreso = fecha_ingreso
        self.sueldo_base = sueldo_base

    def __str__(self):
        return (
            f"Empleado({self.rut}, "
            f"{self.nombre}, "
            f"{self.fecha_ingreso}, "
            f"{self.sueldo_base})"
        )