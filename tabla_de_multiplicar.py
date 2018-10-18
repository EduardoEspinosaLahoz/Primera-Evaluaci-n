def tabla_de_multiplicar():
    n_tabla=input("Que numero quieres multiplicar?")
    for i in range (0,11):
        print str(n_tabla)+ " x "+ str(i) +" = "+ str(n_tabla*i)
   
#i es la VARIABLE CONTADORA
tabla_de_multiplicar()
