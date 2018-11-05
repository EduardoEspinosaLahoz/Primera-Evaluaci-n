def bucle_11():
    print"************************"
    print"* SUMA PARES E IMPARES *"
    print"************************"

    #Suma de numeros pares e impares
    nfinal=input("Hasta que numero quieres sumar?")
    
    #Definimos una variable para sumar los pares
    
    suma_pares=0 #Inicializamos la variable a cero
    
    #Definimos una variable para sumar los pares

    suma_impares=0 #INicializamos la variable a cero
    
    for numero in range(1,nfinal+1):
        #para cada numero me pregunto si es par o impar
        if(numero%2==0):
            print str(numero)," es PAR"
            suma_pares=suma_pares+numero
        else:
            print str(numero)," es IMPAR"
            suma_impares=suma_impares+numero
    print "La suma de numeros pares es= ",suma_pares
    print "La suma de numeros impares es= ",suma_impares

bucle_11()
