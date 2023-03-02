# input
Ing = int(input("ingrese sus ganancias: "))

# processing
if Ing>945200:
    deuda = int(input("ingrese sus deudas: "))
    if deuda==0:
        print("prestamo aprobado")
    else:
        print("prestamo no aprobado")
else:
    print("prestamo no aprobado")