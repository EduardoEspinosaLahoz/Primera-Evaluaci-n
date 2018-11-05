def bucle_10():
    print"*******************"
    print"* PARES E IMPARES *"
    print"*******************"

    #Suma de numeros pares e impares
    nfinal=input("Hasta que numero quieres sumar?")
    
    #Definimos una variable para contar los pares
    
    n_pares=0 #Inicializamos la variable a cero
    
    #Definimos una variable para contar los pares

    n_impares=0 #INicializamos la variable a cero
    
    for numero in range(1,nfinal+1):
        #para cada numero me pregunto si es par o impar
        if(numero%2==0):
            print str(numero)," es PAR"
            n_pares=n_pares+1
        else:
            print str(numero)," es IMPAR"
            n_impares=n_impares+1
    print "He contado ",n_pares," numeros pares."
    print "He contado ",n_impares," numeros impares."

bucle_10()
