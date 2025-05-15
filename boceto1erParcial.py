import os
os.system("cls")

# programa principal

for i in range(3):
    id = i + 1
    
    nombre = input("Ingrese el nombre de la persona: ").capitalize()
    apellido = input("\nIngrese el apellido de la persona: ").upper()

    # Ingreso de la edad de la persona y su respectiva validación.
    edad = int(input("\nIngrese la edad de la persona (La edad debe estar entre 30 y 60 años): "))
    while edad < 30 or edad > 60:
        print("Dato erroneo, intente nuevamente")
        edad = int(input("\nIngrese la edad de la persona (La edad debe estar entre 30 y 60 años): "))
    
    # Ingreso del codigo de area de formacion y su respectiva validación.
    codigodeAreaDeFormacion = input("\nIngrese el area de formacion de la persona (ADM – NAT – TEC ): ").upper()
    while codigodeAreaDeFormacion != "ADM" and codigodeAreaDeFormacion != "NAT" and  codigodeAreaDeFormacion != "TEC":
        print("Dato erroneo, intente nuevamente")
        codigodeAreaDeFormacion = input("\nIngrese el area de formacion de la persona (ADM – NAT – TEC ): ").upper()
    # Area de formacion ya validada, ahora se asigna el area de formacion correspondiente.
    if codigodeAreaDeFormacion == "ADM":
        areaDeFormacion = "ADMINISTRATIVAS"
    elif codigodeAreaDeFormacion == "NAT":
        areaDeFormacion = "NATURALES Y RENOVABLES"
    else: # codigodeAreaDeFormacion == "TEC":
        areaDeFormacion = "TECNOLÓGICAS"

    # Ingreso del codigo de localidad y su respectiva validación.
    codigoDeLocalidad = input("\nIngrese el codigo de localidad de la persona\nC: Cipolletti\nN: Neuquén Capital\nR: General Roca\nP: Plottier\nIngrese aquí: ").upper()
    while codigoDeLocalidad != "C" and codigoDeLocalidad != "N" and codigoDeLocalidad != "R" and codigoDeLocalidad != "P":
        print("Dato erroneo, intente nuevamente")
        codigoDeLocalidad = input("\nIngrese el codigo de localidad de la persona\nC: Cipolletti\nN: Neuquén Capital\nR: General Roca\nP: Plottier\nIngrese aquí: ").upper()
    # Codigo de localidad ya validado, ahora se asigna el localidad correspondiente.
    if codigoDeLocalidad == "C":
        localidad = "Cipolletti"
    elif codigoDeLocalidad == "N":
        localidad = "Neuquén Capital"
    elif codigoDeLocalidad == "R":
        localidad = "General Roca"
    else: # codigoDeLocalidad == "P":
        localidad = "Plottier"

    # Ingreso del codigo de seminario y su respectiva validación.
    codigoDeSeminario = input("\nIngrese el codigo de seminario de la persona\nA: IA EN LAS ÁREAS NATURALES\nB: LIDERAZGO SIGLO XXI\nC: ADMINISTRACIÓN DE RRHH\nD: NUEVAS TECNOLOGÍAS DE SOFTWARE\nE: INFORMÁTICA EN LA NUBE\nIngrese aquí: ").upper()
    while codigoDeSeminario != "A" and codigoDeSeminario != "B" and codigoDeSeminario != "C" and codigoDeSeminario != "D" and codigoDeSeminario != "E":
        print("Dato erroneo, intente nuevamente")
        codigoDeSeminario = input("\nIngrese el codigo de seminario de la persona\nA: IA EN LAS ÁREAS NATURALES\nB: LIDERAZGO SIGLO XXI\nC: ADMINISTRACIÓN DE RRHH\nD: NUEVAS TECNOLOGÍAS DE SOFTWARE\nE: INFORMÁTICA EN LA NUBE\nIngrese aquí: ").upper()
    # Codigo de seminario ya validado, ahora se asigna el seminario correspondiente.
    if codigoDeSeminario == "A":
        seminario = "IA EN LAS ÁREAS NATURALES"
        importePorEncuentro = 12500
    elif codigoDeSeminario == "B":
        seminario = "LIDERAZGO SIGLO XXI"
        importePorEncuentro = 8900
    elif codigoDeSeminario == "C":
        seminario = "ADMINISTRACIÓN DE RRHH"
        importePorEncuentro = 10500
    elif codigoDeSeminario == "D":
        seminario = "NUEVAS TECNOLOGÍAS DE SOFTWARE"
        importePorEncuentro = 11000
    else: # codigoDeSeminario == "E"
        seminario = "INFORMÁTICA EN LA NUBE"
        importePorEncuentro = 14900

    # Ingreso del tipo de modalidad y su respectiva validación.
    tipoDeModalidad = input("\nIngrese el tipo de modalidad de la persona\nM: Mixta\nV: Virtual\nP: Presencial\nIngrese aquí: ").upper()
    while tipoDeModalidad != "M" and tipoDeModalidad != "V" and tipoDeModalidad != "P":
        print("Dato erroneo, intente nuevamente") 
        tipoDeModalidad = input("\nIngrese el tipo de modalidad de la persona\nM: Mixta\nV: Virtual\nP: Presencial\nIngrese aquí: ").upper()
    # Tipo de modalidad ya validado, ahora se asigna la modalidad correspondiente.
    if tipoDeModalidad == "M":
        modalidad = "MIXTA"
        lugarDeCursado = "Aula Magna y Zoom"
    elif tipoDeModalidad == "V":
        modalidad = "VIRTUAL"
        lugarDeCursado = "Zoom"
    else: # tipoDeModalidad == "P":
        modalidad = "PRESENCIAL"
        lugarDeCursado = "Aula Magna"

    # Ingreso de la cantidad de encuentros y su respectiva validación.
    cantidadDeEncuentros = int(input("\nIngrese la cantidad de encuentros de la persona (de 1 a 5): "))
    while cantidadDeEncuentros < 1 or cantidadDeEncuentros > 5:
        print("Dato erroneo, intente nuevamente")
        cantidadDeEncuentros = int(input("\nIngrese la cantidad de encuentros de la persona (de 1 a 5): "))
    
    # Calculo el importe total de la persona.
    importeTotal = cantidadDeEncuentros * importePorEncuentro
    
    # Ingreso del tipo de pago y su respectiva validación.
    tipoDePago = input("\nIngrese el tipo de pago de la persona\nE: Efectivo\nT: Tarjeta\nIngrese aquí: ").upper()
    while tipoDePago != "E" and tipoDePago != "T":
        print("Dato erroneo, intente nuevamente")
        tipoDePago = input("\nIngrese el tipo de pago de la persona\nE: Efectivo\nT: Tarjeta\nIngrese aquí: ").upper()
    # Tipo de pago ya validado, ahora se asigna el pago correspondiente.
    if tipoDePago == "E":
        modalidadDePago = "Efectivo"
        importeApagar = importeTotal*(1 - 0.05) # 5% de descuento
    else: # tipoDePago == "T":
        modalidadDePago = "Tarjeta"
        importeApagar = importeTotal*(1 + 0.10) # 10% de recargo

    print("\n--------------------------------------------------------")
    print("ID:", id)
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Edad:", edad)
    print("Area de formacion:", areaDeFormacion)
    print("Localidad:", localidad)
    print("Seminario:", seminario)
    print("Modalidad:", modalidad)
    print("Lugar de cursado:", lugarDeCursado)
    print(f"Importe por encuentro: {importePorEncuentro} pesos")
    print("Cantidad de encuentros:", cantidadDeEncuentros)
    print(f"Importe total: {importeTotal} pesos")
    print("Modalidad de pago:", modalidadDePago)
    if modalidadDePago == "Efectivo":
        print("Importe a pagar: ", importeApagar, "pesos")
    else: # modalidadDePago == "Tarjeta":
        print("Importe a pagar: ", importeApagar, "pesos")
    print("--------------------------------------------------------")
    input("\nIngrese cualquier tecla para continuar:\t")
    os.system("cls")