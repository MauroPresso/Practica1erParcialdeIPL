import os
os.system("cls")

# Programa principal

# Inicializo los contadores por sector
contadorSectorA = 0
contadorSectorB = 0
contadorSectorC = 0

# Acumulo sueldos por sector
acumuladorSueldosTOTALESsectorA = 0
acumuladorSueldosTOTALESsectorB = 0
acumuladorSueldosTOTALESsectorC = 0

# Inicializo los contadores de la capacitacion
contadorSIcapacitacion = 0
contadorNOcapacitacion = 0

# Inicializo el acumulador de Plus
acumuladorPlus = 0



for i in range(3):
    
    numeroDeInscripicion = i + 100 # i arranca en cero.

    apellido = input("Ingrese su apellido: ").upper()
    nombre = input("Ingrese su nombre: ").capitalize()
    
    # Ingreso y valido antiguedad
    antiguedad = int(input("Ingrese su antiguedad (entre 0 a 25 años): "))
    while antiguedad < 0 or antiguedad > 25:
        print("Antiguedad incorrecta. Intente de nuevo.")
        antiguedad = int(input("Ingrese su antiguedad (entre 0 a 25 años): "))
    # Valide antiguedad

    # Ingreso y valido código de sector
    codigoDeSector = input("Ingrese su código de sector (A/B/C): ").upper()
    while codigoDeSector != "A" and codigoDeSector != "B" and codigoDeSector != "C":
        print("Código de sector incorrecto. Intente de nuevo.")
        codigoDeSector = input("Ingrese su código de sector (A/B/C): ").upper()
    # Valide código de sector

    # ¿Hace la capacitación?
    haceCapacitacion = input("Ingrese si hace la capacitación (S/N): ").upper()
    while haceCapacitacion != "S" and haceCapacitacion != "N":
        print("Respuesta incorrecta. Intente de nuevo.")
        haceCapacitacion = input("Ingrese si hace la capacitación (S/N): ").upper()
    # Valide capacitación

    # Ingreso y valido código de localidad
    codigoDeLocalidad = input("Ingrese su código de localidad (C/N/P): ").upper()
    while codigoDeLocalidad != "C" and codigoDeLocalidad != "N" and codigoDeLocalidad != "P":
        print("Código de localidad incorrecto. Intente de nuevo.")
        codigoDeLocalidad = input("Ingrese su código de localidad (C/N/P): ").upper()
    # Valide código de localidad

    if codigoDeSector == "A":
        sueldo = 1224500
        sector = "ADMINISTRACIÓN"
        capacitacion = "TANGO GESTION"
        contadorSectorA = contadorSectorA + 1
    elif codigoDeSector == "B":
        sueldo = 1225200
        sector = "DESARROLLO"
        capacitacion = "JOMMLA"
        contadorSectorB = contadorSectorB + 1
    else: # codigoDeSector == "C"
        sueldo = 1228800
        sector = "LOGÍSTICA"
        capacitacion = "ESTRATEGIAS"
        contadorSectorC = contadorSectorC + 1

    # Calcular el Plus en el sueldo por hacer capacitación
    if haceCapacitacion == "S":
        plus = sueldo*(0.10)
        acumuladorPlus = acumuladorPlus + plus
        contadorSIcapacitacion = contadorSIcapacitacion + 1
    else: # haceCapacitacion == "N"
        plus = 0
        contadorNOcapacitacion = contadorNOcapacitacion + 1
  
    # Calculo el sueldo total
    sueldoTOTAL = sueldo + plus

    # Sumo los sueldos totales por sector
    if codigoDeSector == "A":
        acumuladorSueldosTOTALESsectorA = acumuladorSueldosTOTALESsectorA + sueldoTOTAL
    elif codigoDeSector == "B":
        acumuladorSueldosTOTALESsectorB = acumuladorSueldosTOTALESsectorB + sueldoTOTAL
    else: # codigoDeSector == "C"
        acumuladorSueldosTOTALESsectorC = acumuladorSueldosTOTALESsectorC + sueldoTOTAL

    # Asigno localidad
    if codigoDeLocalidad == "C":
        localidad = "Cipolletti"
    elif codigoDeLocalidad == "N":
        localidad = "Neuquén"
    else: # codigoDeLocalidad == "P"
        localidad = "Plottier"

    # Muestro los datos de la persona
    print("\n-----------------DATOS DE LA PERSONA-----------------")
    print("Numero de inscripción:", numeroDeInscripicion)
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Sector:", sector)
    if haceCapacitacion == "S":
        print("Capacitación:", capacitacion)
    else: # haceCapacitacion == "N"
        print("Capacitación:", "NO HIZO CAPACITACIÓN")
    print("Antiguedad:", antiguedad, "años")
    print("Localidad:", localidad)
    print("Sueldo:", sueldo)
    print("Plus:", plus)
    print("Sueldo total:", sueldoTOTAL)
    print("-----------------------------------------------------")
    input("\nIngrese cualquier tecla para continuar:\t")
    os.system("cls")
# Fin ciclo for
print("\n\n\n----------------RESULTADOS---------------------")
print("\nAcumulacion del Plus:", acumuladorPlus) # Ejercicio 4 inciso l.
print("\nCantidad de trabajadores que hicieron capacitación: ", contadorSIcapacitacion) # Ejercicio 4 inciso m.
print("Cantidad de trabajadores que no hicieron capacitación: ", contadorNOcapacitacion) # Ejercicio 4 inciso n.
# Ejercicio 4 inciso j.
print("\nCantidad de trabajadores en sector A: ", contadorSectorA)
print("Cantidad de trabajadores en sector B: ", contadorSectorB)
print("Cantidad de trabajadores en sector C: ", contadorSectorC)
# Ejercicio 4 inciso k.
print("\nPromedio de sueldo del sector A: ", acumuladorSueldosTOTALESsectorA/contadorSectorA)
print("Promedio de sueldo del sector B: ", acumuladorSueldosTOTALESsectorB/contadorSectorB)
print("Promedio de sueldo del sector C: ", acumuladorSueldosTOTALESsectorC/contadorSectorC)
print("-----------------------------------------------------")
input("\nPresione ENTER para continuar...")
os.system("cls")
print("\nFin del programa.")

