import os

class Actividades:
    def __init__(self, actividad, dia, mes, año, prioridad):
        self.actividad = actividad
        self.dia = dia
        self.mes = mes
        self.año = año
        self.prioridad = prioridad
        
    def __str__(self):
        return f"Nombre de la actividad: {self.actividad}, dia: {self.dia}, mes: {self.mes}, año: {self.año}, prioridad: {self.prioridad}"

actividades_universitarias = []

while True:
    os.system("cls")
    print("Bienvenido al menú de opciones del gestor de actividades")
    print("Opción 1: Registro de Actividad por fecha y prioridad")
    print("Opción 2: Buscar por palabra clave")
    print("Opción 3: Mostrar todas las actividades por orden")
    print("Opción 4: Eliminar actividad")
    print("Opción 5: Salir del programa")
    opc = input("Elija una opción válida del menú: ")

    if opc == "1":
        os.system('cls')
        print("Eligió la opción 1, registrar una actividad")
        actividad = input("Ingrese la actividad: ").lower()
        dia = input("Ingrese el día (ej. Martes): ").lower()
        mes = input("Ingrese el mes (ej. Diciembre): ").lower()
        año = input("Ingrese el año (ej. 2025): ")
        prioridad = input("Ingrese la prioridad de la actividad: ").lower()
        nueva_actividad = Actividades(actividad, dia, mes, año, prioridad)
        actividades_universitarias.append(nueva_actividad)

    elif opc == "2":
        os.system('cls')
        print("Eligió la opción 2, buscar actividades por palabra clave")
        palabra = input("Ingrese la palabra la clave: ").lower()

    elif opc == "3":
        os.system('cls')
        print("Opción 3, mostrar todas las actividades")
        mes_año = input("Ingrese el mes o año a buscar: ").lower()
        for actividad in actividades_universitarias:
            if mes_año in actividad.actividad or actividad.dia == mes_año or actividad.mes == mes_año or actividad.año == mes_año or actividad.prioridad == mes_año:
                print(actividad)

    elif opc == "4":
        os.system('cls')
        print("Eligió la opción 4, eliminar actividad")
        print("Estas son todas las actividades registradas:")
        for i in actividades_universitarias:
            print(i)

        eldia = input("Ingrese el día a buscar: ").lower()
        elmes = input("Ingrese el mes a buscar: ").lower()
        elaño = input("Ingrese el año a buscar: ").lower()

        actividades_a_eliminar = [act for act in actividades_universitarias if act.dia == eldia and act.mes == elmes and act.año == elaño]
        for act in actividades_a_eliminar:
            actividades_universitarias.remove(act)
            print(f"Se ha eliminado la actividad: {act}")

    elif opc == "5":
        print("Saliendo del programa…")
        break

    else:
        print("Opción no válida, intente de nuevo.")
        input("Presione Enter para continuar...")
