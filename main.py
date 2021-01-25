tekst = str(input("Podaj Tekst do zaszyfrowania: "))
klucz = int(input("Podaj przesunięcie: "))
def szyfrowanie(tekst = tekst):
    dlugosc_tekstu = len(tekst) # Sprawdzamy ile znaków zawiera tekst
    dac = [] # Lista na zbiory wydzielone z tekstu
    wynik = [] # Lista na odwrócone zbiory
    wynik2 = "" # Potrzebne podczas konwersji listy na string
    iteracje = 0
    while iteracje < dlugosc_tekstu // klucz: # Dzielimy tekst na zbiory
        dac.append(tekst[:klucz])
        tekst = tekst.replace(tekst[:klucz], "")
        iteracje = iteracje + 1
    for i in dac: # Szyfrujemy zbiory
        odwrocone = "" # Potrzebne do przechowania zbioru, aby potem dodać go do listy
        odwrocone = odwrocone + i[-1]
        if klucz != 2: # Jeśli przesuwamy o więcej niż dwa, trzeba dodać znaki pośrednie
            odwrocone = odwrocone + i[1:len(i) - 1]
        odwrocone = odwrocone + i[0]
        wynik.append(odwrocone)
    if klucz / 2 != klucz // 2: # Jeśli liczba znaków w tekscie była nieparzysta, dodaj zostawioną końcówkę
        for i in wynik:
            wynik2 = wynik2 + i
            wynik = wynik2
        print(str(wynik) + tekst)
    else: # W przeciwnym razie nie dodawaj końcówki
        for i in wynik:
            wynik2 = wynik2 + i
            wynik = wynik2
        print(wynik)

szyfrowanie()

