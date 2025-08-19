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

    elif opc == 3:
        os.system('cls')
        print("Se eligio la opcio 3, buscra actividades por mes, año, dia, o categotia")
        mes_año = input("Ingrese el mes o año a buscar: ").lower()
        for actividad in actividades_universitarias:
            if mes_año in actividad.actividad or actividad.dia == mes_año or actividad.mes == mes_año or actividad.año == mes_año or actividad.prioridad == mes_año:
                print(actividad)
        passgt