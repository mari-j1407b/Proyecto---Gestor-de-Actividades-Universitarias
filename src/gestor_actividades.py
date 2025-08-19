import os

class actividades:
    def __init_(self, actividad, dia, mes, año, prioridad):
        self.actividad = actividad
        self.dia = dia
        self.mes = mes
        self.año = año
        self.prioridad = prioridad
        
    def __str__(self):
        return f"Nombre de la actividad {self.actividad} dia {self.dia} Mes {self.mes} año {self.año} con prioridad {self.prioridad}"

actividades_universitarias = []

pass

    if opc == 1:
        os.system('cls')
        print("Elijio la opcion 1, registrar una actividad")
        actividad = input("Ingrese la actividad: ").lower()
        dia = input("Ingrese el dia ejemplo (Martes): ").lower()
        mes = input("Ingrese el mes ejemplo (Diciembre): ").lower()
        año = input("Ingrese el año ejemplo (2025): ")
        prioridad = input("Ingrese la prioridad de la actividad: ").lower()
        nueva_actividad = actividades(actividad, dia, mes, año, prioridad)
        actividades_universitarias.append(nueva_actividad)

    elif opc == 3:
        os.system('cls')
    print("Se eligio la opcion 3, buscar actividades por mes, año, dia o categoria")
    criterio_busqueda = input("Ingrese el criterio de busqueda: ").lower()
    
    for actividad in actividades_universitarias:
        if (criterio_busqueda in actividad.actividad.lower() or 
            criterio_busqueda == actividad.dia.lower() or 
            criterio_busqueda == actividad.mes.lower() or
            criterio_busqueda == actividad.año.lower() or
            criterio_busqueda == actividad.prioridad.lower()):
            print(actividad)