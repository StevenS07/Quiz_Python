# -*- coding: ISO-8859-2 -*-
#Autro Steven Sowa
from player import Player
from quiz import Quizy
from plik import Plik

class Start:
    
    def menugry():
        print("Menu główne")
        print("1.rzopocznij grę")
        print("2.tabela wyników")
        print("3.wyjd")
        a = int(input("wybierz numer "))
        if a == 1:
            imie = input("podaj imie ")
            gracz = Player(imie)
            Quizy.levels(gracz)
        if a == 2:
            Plik.tabelwynik

      

      







