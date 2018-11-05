def tabla_de_multiplicar_while():
    numero=input("Que tabla quieres que escriba?")
    #for i in range(numero,0,-1):
    i=numero
    while(i>0):
        print str(numero)+ " x "+ str(i)+ " = " + str (numero*i)
        i=i-1
tabla_de_multiplicar_while()
