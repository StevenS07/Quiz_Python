# -*- coding: ISO-8859-2 -*-
#Autro Steven Sowa
class Pytania:
    
    pytania = [
        "wybierz b��dny zapis dzia�ania \nA: print(a**b) \nBprint(a*b) \nC: print(a/b) \nD: print(a\\b)",
        "Wybierz poprawny zapis \nA: if(warunek)  \nB:if(warunek):  \nC:if warunek  \nD: if warunek:",
        "\nCo zwr�ci funkcj po wpiasniu do niej Adam\ndef sprawdz(imie):\ndl=len(imie)\n if imie[dl-1]==a :\n  return True\n else:\n  return False \nA: true \nB: false ",
        "Ile pojawi si� * po wypisaniu wypisuj(6)\ndef wypisuj(n):\nif n == 0:\n    print(�*�, end=��)\nreturn\n    wypisuj(n - 1)\n    wypisuj(n - 1) \nA: 32 \nB: 16 \nC: 64 \nD: 36",
        "Jaka b�dzie warto�� zmiennej a po wykonaniu poni�szego kodu programu?\nimport math\ndef met(x):\n  if x==0:\n      return 1\n      else:\n     return x * met(x-1)\nprint(met(5)) \nA: 10 \nB: 15 \nC: 25 \nD: 30",
        "Co stanie si� z list� M = ['nsrfvgtazirmjiu', 'nyxixskska', 'oxmvg'] po u�yciu tego kodu:\nfor i in M:\n   print(list(i)) \nA: Wypisze ka�dy element jako podlist�\nB: Wypisze ka�dy element\nC:Nic si� nie stanie b��dny zapis\nD:Wypisze tylko po pierwszej literce ka�dego elementu",
        "Mamy lits� L sk�adaj�c� si� z 500 losowych liczb \nL = list(set(L))\n  print(L) \nCo zostanie wypisane na ekranie?\nA: Lista z u�ni�tymi duplikatami \nB: Posegregowana lista\nC: lista liczb przekonwertowana na string\nD: nic si� nie wypisz� b��dny zapis",
        "Jaki zapis s�ownika jest poprawny\nwska� poprawne odpowiedzi:\nA: k = {'Jan' : 1}\nB: k = {1: Jan} \nC: k = ['Jan'] = 1 \nD: k = [1] = 'Jan''",
        "Jaki typ wykresu wypisze kod:\ndane=[30, 50, 40, 100]\nkto=['Antek', 'Zosia', 'Kuba', 'Karol']\nimport matplotlib, matplotlib.pyplot, pandas\nfig, ax = matplotlib.pyplot.subplots(figsize=(10,7))\nax.pie(dane, labels=kto)\nax.legend()\nA: Liniowy\nB: Kolumnowy\nC: Ko�owy\nD: punktowy",
        "co stanie si� ze zdj�ciem po u�yciu tego kodu: \nplt.imshow(photo[:, ::-1])\nA: zostanie obr�cone o 90 stopni\nB: zostanie odwr�cone lustrzanie\nC: zostanie obr�cone o 180 stopni   \nD: zostanie zmniejszone o po�ow�    ",
        ]
    dl = len(pytania)
    poprawne = [
        "D",
        "D",
        "A",
        "C",
        "B",
        "A",
        "A",
        "C",
        "C",
        "B"
        
        ]

    




