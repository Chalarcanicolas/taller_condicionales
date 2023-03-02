# input
x = int(input("digite el valor de x: "))
y = int(input("digite el valor de y: "))

# processing
if x==0:
    if y==0:
        print("el punto esta en el origen")
    else:
        print("el punto esta en el eje y")
else:
    if y==0:
        print("el punto esta en el eje x")
    else:
        if x>0:
            if y>0:
                print("el punto esta en el cuadrante 1")
            else:
                print("el punto esta en el cuadrante 4")
        else:
            if x<0:
                if y<0:
                    print("El punto esta en el cuadrante 3")
                else:
                    print("El punto esta en el cuadrante 2")   