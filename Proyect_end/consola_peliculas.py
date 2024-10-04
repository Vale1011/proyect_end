import modulo_peliculas as mod

def mostrar_informacion_pelicula(pelicula: dict)-> None:
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]
    
    print("Nombre: " + nombre + " - Año: " + str(anio) + " - Duración: " + str(duracion) + " mins" )
    print("Género: " + genero + " - Clasificación: " + clasificacion)
    
    hora_formato = f"{hora//100:02d}:{hora%100:02d}"
    print("Día: " + dia + " Hora: " + hora_formato)

def ejecutar_encontrar_pelicula_mas_larga(*peliculas: dict)->None:
    pelicula_mas_larga = mod.encontrar_pelicula_mas_larga(*peliculas)
    print("La película más larga es:")
    mostrar_informacion_pelicula(pelicula_mas_larga)

def ejecutar_consultar_duracion_promedio_peliculas(*peliculas: dict)->None:
    duracion_promedio = mod.duracion_promedio(*peliculas)
    print("La duración promedio de las películas es:", duracion_promedio)

def ejecutar_encontrar_estrenos(*peliculas: dict)->None:
    anio = int(input("Ingrese el año para buscar estrenos: "))
    estrenos = mod.encontrar_estrenos(anio, *peliculas)
    if estrenos:
        print("Películas estrenadas en el año", anio, ":")
        for pelicula in estrenos:
            mostrar_informacion_pelicula(pelicula)
    else:
        print(f"No hay estrenos en el año {anio}")

def ejecutar_cuantas_peliculas_18_mas(*peliculas: dict)->None:
    cantidad = mod.cuantas_peliculas_18_mas(*peliculas)
    print("Hay", cantidad, "películas con clasificación 18+")

def ejecutar_reagendar_pelicula(*peliculas: dict)->None:
    nombre = input("Ingrese el nombre de la película que desea reagendar: ")
    pelicula = mod.encontrar_pelicula(nombre, *peliculas)
    
    if pelicula is None:
        print("No hay ninguna película con este nombre")
    else:
        nueva_hora = int(input("Ingrese la nueva hora (formato 24h, ej. 1930): "))
        nuevo_dia = input("Ingrese el nuevo día (ej. Lunes): ")
        control_horario = input("¿Desea controlar el horario de conflicto? (s/n): ").lower() == 's'
        exito = mod.reagendar_pelicula(pelicula, nueva_hora, nuevo_dia, control_horario, *peliculas)
        if exito:
            print("Película reagendada exitosamente.")
        else:
            print("No se pudo reagendar la película debido a un conflicto.")

def ejecutar_decidir_invitar(*peliculas: dict)->None:
    print("Decidir si se puede invitar a alguien a ver una película")
    nom_peli = input("Ingrese el nombre de la película: ")
    pelicula = mod.encontrar_pelicula(nom_peli, *peliculas)
    
    if pelicula is None:
        print("No hay ninguna película con este nombre")
    else:
        edad = int(input("Ingrese la edad de la persona: "))
        if edad >= 18 or pelicula['clasificacion'] != '18+':
            print(f"Puedes invitar a alguien a ver {pelicula['nombre']}.")
        else:
            print("No puedes invitar a esta persona debido a la clasificación.")

def iniciar_aplicacion():
    pelicula1 = mod.crear_pelicula("Shrek",  "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes")
    pelicula2 = mod.crear_pelicula("Get Out",  "Suspenso, Terror", 104, 2017, '18+', 2330, "Sábado")  
    pelicula3 = mod.crear_pelicula("Icarus",  "Documental, Suspenso", 122, 2017, '18+', 800, "Domingo")
    pelicula4 = mod.crear_pelicula("Inception",  "Acción, Drama", 148, 2010, '13+', 1300, "Lunes")
    pelicula5 = mod.crear_pelicula("The Empire Strikes Back",  "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miércoles")   
    pelicula6 = mod.crear_pelicula('Fractura','Suspenso, Misterio',120, 2018,'13+',1700, 'lunes')
    pelicula7 = mod.crear_pelicula('Sonic','familiar, comedia',122,  2020,'todos',800, 'Domingo')
    pelicula8 = mod.crear_pelicula('Guerra Mundial Z','accion,suspenso',156, 2013,'+13',1300,'lunes')
    pelicula9 = mod.crear_pelicula('Otro día para matar','accion',104, 2014,'+13',1700, 'Viernes')
    pelicula10 = mod.crear_pelicula("Pulp Fiction", "Drama, Crimen", 154, 1994, '18+', 1900, "Viernes")
    
    ejecutando = True
    while ejecutando:            
        print("\n\nMi agenda de películas para la semana de receso" + "\n" + ("-" * 50))
        
        for i, pelicula in enumerate([pelicula1, pelicula2, pelicula3, pelicula4, pelicula5, pelicula6, pelicula7, pelicula8, pelicula9, pelicula10], 1):
            print(f"Película {i}")
            mostrar_informacion_pelicula(pelicula)
            print("-" * 50)

        ejecutando = mostrar_menu_aplicacion(pelicula1, pelicula2, pelicula3, pelicula4, pelicula5, pelicula6, pelicula7, pelicula8, pelicula9, pelicula10)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

def mostrar_menu_aplicacion(*peliculas: dict) -> bool:
    print("Menú de opciones")
    print(" 1 - Consultar película más larga")
    print(" 2 - Consultar duración promedio de las películas")
    print(" 3 - Consultar películas de estreno")
    print(" 4 - Consultar cuántas películas tienen clasificación 18+")
    print(" 5 - Reagendar película")
    print(" 6 - Verificar si se puede invitar a alguien")    
    print(" 7 - Salir de la aplicación")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(*peliculas)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(*peliculas)
    elif opcion_elegida == "3":
        ejecutar_encontrar_estrenos(*peliculas)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(*peliculas)
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(*peliculas)
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(*peliculas)
    elif opcion_elegida == "7":
        continuar_ejecutando = False
    else:
        print("La opción " + opcion_elegida + " no es válida.")
    
    return continuar_ejecutando


iniciar_aplicacion()
