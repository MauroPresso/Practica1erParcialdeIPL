import os
os.system("cls")

# programa principal

for i in range(3):
    id = i + 1
    edad = int(input("\nIngrese la edad de la persona (La edad debe estar entre 30 y 60 años): "))
    while edad < 30 or edad > 60:
        print("Dato erroneo, intente nuevamente")
        edad = int(input("\nIngrese la edad de la persona La edad debe estar entre 30 y 60 años: "))
    apellido = input("\nIngrese el apellido de la persona: ").upper()
    nombre = input("Ingrese el nombre de la persona: ").capitalize()
    
    areaDeFormacion = input("\nIngrese el area de formacion de la persona (ADM – NAT – TEC ): ").upper()
    while areaDeFormacion != "ADM" and areaDeFormacion != "NAT" and  areaDeFormacion != "TEC":
        print("Dato erroneo, intente nuevamente")
        areaDeFormacion = input("\nIngrese el area de formacion de la persona (ADM – NAT – TEC ): ").upper()
    
    codigoDeLocalidad = input("\nIngrese el codigo de localidad de la persona (C/N/R/P): ").upper()
    while codigoDeLocalidad != "C" and codigoDeLocalidad != "N" and codigoDeLocalidad != "R" and codigoDeLocalidad != "P":
        print("Dato erroneo, intente nuevamente")
        codigoDeLocalidad = input("\nIngrese el codigo de localidad de la persona (C/N/R/P): ").upper()
    
    codigoDeSeminario = input("\nIngrese el codigo de seminario de la persona (A/B/C/D/E): ").upper()
    while codigoDeSeminario != "A" and codigoDeSeminario != "B" and codigoDeSeminario != "C" and codigoDeSeminario != "D" and codigoDeSeminario != "E":
        print("Dato erroneo, intente nuevamente")
        codigoDeSeminario = input("\nIngrese el codigo de seminario de la persona (A/B/C/D/E): ").upper()
    
    tipoDeModalidad = input("\nIngrese el tipo de modalidad de la persona (M/V/P): ").upper()
    while tipoDeModalidad != "M" and tipoDeModalidad != "V" and tipoDeModalidad != "P":
        print("Dato erroneo, intente nuevamente") 
        tipoDeModalidad = input("\nIngrese el tipo de modalidad de la persona (M/V/P): ").upper()
    
    cantidadDeEncuentros = int(input("\nIngrese la cantidad de encuentros de la persona (de 1 a 5): "))
    while cantidadDeEncuentros < 1 or cantidadDeEncuentros > 5:
        print("Dato erroneo, intente nuevamente")
        cantidadDeEncuentros = int(input("\nIngrese la cantidad de encuentros de la persona (de 1 a 5): "))
    
    tipoDePago = input("\nIngrese el tipo de pago de la persona (E/T): ").upper()
    while tipoDePago != "E" and tipoDePago != "T":
        print("Dato erroneo, intente nuevamente")
        tipoDePago = input("\nIngrese el tipo de pago de la persona (E/T): ").upper()
    
    print("\n--------------------------------------------------------")
    print("ID:", id)
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Edad:", edad)
    print("Area de formacion:", areaDeFormacion)
    print("Codigo de localidad:", codigoDeLocalidad)
    print("Codigo de seminario:", codigoDeSeminario)
    print("Tipo de modalidad:", tipoDeModalidad)
    print("Cantidad de encuentros:", cantidadDeEncuentros)
    print("Tipo de pago:", tipoDePago)
    print("--------------------------------------------------------")
    input("\nIngrese cualquier tecla para continuar:\t")
    os.system("cls")