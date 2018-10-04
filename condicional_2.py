def condicional_2 ():
    respuesta=input("Que hora es? (1-24)")
    if(respuesta>24):
        print "introduce una hora valida(1-24)"
    elif(respuesta >=12):
        print "Buenos tardes"
    elif(respuesta>=20):
        print "Buenas noches"
    elif(respuesta>=0):
        print "Buenos dias"

            

condicional_2() 
