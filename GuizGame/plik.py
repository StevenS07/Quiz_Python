# -*- coding: ISO-8859-2 -*-
#Autro Steven Sowa

class Plik:
    def zapiszwynik(imie, punkty, procent):
        plik = open("wyniki.txt", "a")
        tekst = "\nGracz "+str(imie)+" zdobyl "+str(punkty)+" punktow i uzyskal "+str(procent)+"% "
        plik.write(str(tekst))
        plik.close()
       

    def tabelwynik():
        plik = open("wyniki.txt", "r")
        print(plik.read())
        plik.close()
        





