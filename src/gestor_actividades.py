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

while True:
    os.system("cls")
    print("Bienvenido al menu de opciones del gestor de actividades")
    print("Opcion 1: Registro de Actividad por fecha y prioridad")
    print("Opcion 2: Buscar por palabra clave")
    print("Opcion 3: Mostrar todas las actividades por orden")
    print("Opcion 4: eliminar actividad")
    print("Opcion 5: salir del programa")
    opc = input("Elija una opcion valida del menu: ")
    
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