Descripsión del proyecto: Gestor de Actividades Universitarias 
Sistema para registrar, calificar y consultar actividades de estudiantes (clases, tareas, exámenes, eventos, reuniones)

Instrucciones de uso:
El programa cuenta con 5 opciones:
Opción 1 - Registro de actividades
Opción 2 - Buscar actividades por palabras clave
Opción 3 - Mostrar las actividades por orden
Opción 4 - Eliminar actividad
Opción 5 - Salir del programa

Al inicializar el programa, se pide que se coloque una opción válida del menú. Al escoger la opción 1 el programa procede a pedir información sobre la actividad al usuario: 
-Actividad a guardar
-Día de la actividad
-Mes de la actividad
-Año a realizar la actividad
-Prioridades en caso de que la actividad cuente con ello

Seguido de eso, continúa con la opción de presionar enter para continuar seleccionando opciones

-Al escoger la opción 2 se le pide al usuario la palabra clave de la actividad a buscar
Si se desea seguir seleccionando opciones, saldrá la opción de presionar enter para continuar con el programa 

-Al escoger la opción 3 se le pide al usuario que ingrese el mes o año a buscar
Se se desea continuar nuevamente, se mostrará la opción de seleccionar enter para continuar con el programa 

-Al escoger la opción 3 se le pide al usuario que ingrese el mes o año a buscar

Seleccionando la opción 4 se le muestra al usuario las actividades registradas, como el nombre, día, mes y priodidad de dicha actividad, dando la opción de elegir qué actividad se desea eliminar.

-Al seleccionar la opción 5 el programa se cerrará automáticamente 


Roles de los integrantes:
Líder técnico / Desarrollador técnico - Mario Matheu
Responsabale de pruebas y manejo de errores - Cindy Estrada
Encargado de interfaz de usuario y flujo - Maria Belén Mendoza
Gestor de documentación y repositorio - Luna Calderón 

Problemas encontrados:
## 1. [Problemas al realizar el push request]
- **Descripción**: Al intentar hacer `git push origin main` aparecía el error de no poderlo realizar correcamente'`.
- **Solución**: Se ejecutó `git pull origin main --rebase` para traer los cambios más recientes
  del repositorio remoto y después se volvió a hacer `git push origin main`.
- **Estado**: Resuelto ✅.