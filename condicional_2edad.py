def condicional_2edad():
    edad=input("�Cuantos a�os tienes?")
    if(edad >= 18):
        print "Sala alcoholica"
    else:
        if(edad>=15):
            print "Sala adolescentes"
        else:
            print "Sala infantil"


condicional_2edad()
