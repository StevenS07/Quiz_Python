# -*- coding: ISO-8859-2 -*-
#Autro Steven Sowa
class Pytania:
    
    pytania = [
        "wybierz błędny zapis działania \nA: print(a**b) \nBprint(a*b) \nC: print(a/b) \nD: print(a\\b)",
        "Wybierz poprawny zapis \nA: if(warunek)  \nB:if(warunek):  \nC:if warunek  \nD: if warunek:",
        "\nCo zwróci funkcj po wpiasniu do niej Adam\ndef sprawdz(imie):\ndl=len(imie)\n if imie[dl-1]==a :\n  return True\n else:\n  return False \nA: true \nB: false ",
        "Ile pojawi się * po wypisaniu wypisuj(6)\ndef wypisuj(n):\nif n == 0:\n    print(*, end=)\nreturn\n    wypisuj(n - 1)\n    wypisuj(n - 1) \nA: 32 \nB: 16 \nC: 64 \nD: 36",
        "Jaka będzie wartoć zmiennej a po wykonaniu poniższego kodu programu?\nimport math\ndef met(x):\n  if x==0:\n      return 1\n      else:\n     return x * met(x-1)\nprint(met(5)) \nA: 10 \nB: 15 \nC: 25 \nD: 30",
        "Co stanie się z listš M = ['nsrfvgtazirmjiu', 'nyxixskska', 'oxmvg'] po użyciu tego kodu:\nfor i in M:\n   print(list(i)) \nA: Wypisze każdy element jako podlistę\nB: Wypisze każdy element\nC:Nic się nie stanie błędny zapis\nD:Wypisze tylko po pierwszej literce każdego elementu",
        "Mamy litsę L składajšcš się z 500 losowych liczb \nL = list(set(L))\n  print(L) \nCo zostanie wypisane na ekranie?\nA: Lista z uniętymi duplikatami \nB: Posegregowana lista\nC: lista liczb przekonwertowana na string\nD: nic się nie wypiszę błędny zapis",
        "Jaki zapis słownika jest poprawny\nwskaż poprawne odpowiedzi:\nA: k = {'Jan' : 1}\nB: k = {1: Jan} \nC: k = ['Jan'] = 1 \nD: k = [1] = 'Jan''",
        "Jaki typ wykresu wypisze kod:\ndane=[30, 50, 40, 100]\nkto=['Antek', 'Zosia', 'Kuba', 'Karol']\nimport matplotlib, matplotlib.pyplot, pandas\nfig, ax = matplotlib.pyplot.subplots(figsize=(10,7))\nax.pie(dane, labels=kto)\nax.legend()\nA: Liniowy\nB: Kolumnowy\nC: Kołowy\nD: punktowy",
        "co stanie się ze zdjęciem po użyciu tego kodu: \nplt.imshow(photo[:, ::-1])\nA: zostanie obrócone o 90 stopni\nB: zostanie odwrócone lustrzanie\nC: zostanie obrócone o 180 stopni   \nD: zostanie zmniejszone o połowę    ",
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

    




