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
    import os

while True:
    os.system('cls')
    print("Bienvenido al menu de opciones del gestor de actividades")
    print("Opcion 1: Registro de Actividad por fecha y prioridad")
    print("Opcion 2: Buscar por palabra clave")
    print("Opcion 3: Mostrar todas las actividades por orden")
    print("Opcion 4: Eliminar actividad") 
    print("Opcion 5: Salir del programa")
    try: # <<< Probando manejo de errores usando try
        opc = int(input("Elija una opcion valida del menu: "))
    except:
        print("Debe ingresar un número válido")
        continue
    
    if opc == 5:
        print("Saliendo del programa...")
        break