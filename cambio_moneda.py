# -*- coding: cp1252 -*-
def cambio_moneda():
    moneda=input("¿Cuanto quieres cambiar?")
    respuesta_2=raw_input("¿Lo quieres en libras o en dolares(l/d/z/c)?")
    if(respuesta_2=="l"):
       print("Son "+str(moneda*0.88)+ "Libras")
    if (respuesta_2=="d"):
        print("Son "+str(moneda*1.15)+ "Dolares")
    if (respuesta_2=="z"):
        print("Son "+str(moneda*0.23)+ "Zlotys")
     if (respuesta_2=="c"):
         print("Son "+str(moneda*0.005)+ "Camellos")
  

cambio_moneda()
