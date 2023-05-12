# -*- coding: ISO-8859-2 -*-
#Autro Steven Sowa
from player import Player
from pytania import Pytania

class Quizy(Player, Pytania ):

    

    
    def opdowiedz(nrpytania, gracz):
        

        pyt = Pytania.pytania[nrpytania]
        podp = Pytania.poprawne[nrpytania]
        print(pyt)
        odp = input("podaj odp")
        if odp.lower()==podp.lower():
            gracz.punkty=gracz.punkty+1
            return print("dobra odpowedz") 
        else:
            return print("zla odpowiedz")
            

        
    def levels(gracz):
        print("Witam na tescie z pythona zeby zdac musisz uzyskac 50%\n")
        for i in range(0, Pytania.dl):
            Quizy.opdowiedz(i,gracz)

        Player.wynik(gracz)
            

     
         




