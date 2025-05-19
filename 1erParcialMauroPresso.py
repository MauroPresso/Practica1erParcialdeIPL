import os
os.system("cls")

# Programa principal

for i in range(10):
    
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
    elif codigoDeSector == "B":
        sueldo = 1225200
        sector = "DESARROLLO"
        capacitacion = "JOMMLA"
    else: # codigoDeSector == "C"
        sueldo = 1228800
        sector = "LOGÍSTICA"
        capacitacion = "ESTRATEGIAS"
    # Valide sueldo

    # Calcular el Plus en el sueldo por hacer capacitación
    if haceCapacitacion == "S":
        sueldo = sueldo*(1 + 0.10)
        cobraPlus = True
    else:
        sueldo = sueldo*(1 + 0)
        cobraPlus = False
    # Valide plus

    # Asigno localidad
    if codigoDeLocalidad == "C":
        localidad = "Cipolletti"
    elif codigoDeLocalidad == "N":
        localidad = "Neuquén"
    else: # codigoDeLocalidad == "P"
        localidad = "Plottier"
    
    
