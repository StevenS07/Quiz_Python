# -*- coding: ISO-8859-2 -*-
#Autro Steven Sowa
from player import Player
from quiz import Quizy
from plik import Plik

class Start:
    
    def menugry():
        print("Menu g��wne")
        print("1.rzopocznij gr�")
        print("2.tabela wynik�w")
        print("3.wyjd�")
        a = int(input("wybierz numer "))
        if a == 1:
            imie = input("podaj imie ")
            gracz = Player(imie)
            Quizy.levels(gracz)
        if a == 2:
            Plik.tabelwynik

      

      







