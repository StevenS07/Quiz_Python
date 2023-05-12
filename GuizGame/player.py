# -*- coding: ISO-8859-2 -*-
#Autro Steven Sowa
from pytania import Pytania
from plik import Plik

class Player:
    def __init__(gracz, imie):
        gracz.imie = imie
        gracz.punkty = 0
        
        
    def oceny(gracz):
        if gracz>=85:
            focena = 5
        elif gracz>=75:
            focena=4.5
        elif gracz>=70:
            focena=4
        elif gracz>=65:
            focena=3.5
        elif gracz>=50:
            focena=3
        else:
            focena=2
        return focena
      
    def ileprocent(punkty):
        procenty = punkty*100/Pytania.dl
        return procenty
    
    def wynik(gracz):
        procent = Player.ileprocent(gracz.punkty)
        ocena = Player.oceny(procent)
        print("Gracz:",gracz.imie," uzyskal: ",gracz.punkty," punktów i ukonczyl przedmiot uzyskujšc ",procent,"% procent otrzymujac ocene ",ocena)
        czy = int(input("czy chesz zapisać wynik 1-tak/2-nie"))
        if czy == 1:
            return Plik.zapiszwynik(gracz.imie, gracz.punkty, procent)
        return print("\n Koniec ")
         


        
   




