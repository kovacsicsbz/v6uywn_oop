import datetime
from abc import ABC, abstractmethod


class Szoba(ABC):

    @property
    @abstractmethod
    def ar(self):
        return self.ar

    @property
    @abstractmethod
    def szobaszam(self):
        return self.szobaszam

    def __str__(self):
        return f"Szobaszám: {self._szobaszam} Ár: {self._ar}"


class EgyagyasSzoba(Szoba):

    def __init__(self, ar, szobaszam):
        self._ar = ar
        self._szobaszam = szobaszam
        self._minibar = True

    def ar(self):
        return self._ar

    def szobaszam(self):
        return self._szobaszam


class KetagyasSzoba(Szoba):

    def __init__(self, ar, szobaszam):
        self._ar = ar
        self._szobaszam = szobaszam

    def ar(self):
        return self._ar

    def szobaszam(self):
        return self._szobaszam


class Szalloda:

    def __init__(self, nev, szobak):
        self._nev = nev
        self._szobak = szobak
        pass

    def listSzobak(self):
        print(f"Szálloda neve: {self._nev}")
        print(f"Szobák:")
        for szoba in self._szobak:
            print(szoba)

    def get_nev(self):
        return self._nev

    def set_nev(self, nev):
        self._nev = nev

    def get_szobak(self):
        return self._szobak


class Foglalas:

    def __init__(self, szalloda):
        self._szalloda = szalloda
        self._foglalasiLista = {}

    def printMenu(self):
        print(f"")
        print(f"--------{self._szalloda.get_nev()} foglalási rendszer---------")
        print(f"#" * 50)
        print(f"Válasszon az alábbi menüpontok közül")
        print(f"Foglalás - nyomja meg az 'f' billentyűt")
        print(f"Lemondás - nyomja meg az 'l' billentyűt")
        print(f"Foglalások listája - nyomja meg az 'm' billentyűt")
        print(f"Program bezárása - nyomja meg az 'k' billentyűt")
        print(f"#" * 50)
        print(f"")
        print(f"")
    def foglal(self, szobaszam, datum, csendben):

        if (datetime.date.today() > datum):
            if not csendben:
                print(f"Foglalás nem lehetséges, adjon meg egy jövőbeli dátumot!")
            return

        strDdatum = str(datum)

        napiSzobaLista = None

        if self._foglalasiLista is None:
            napiSzobaLista[szobaszam]
        else:
            if strDdatum in self._foglalasiLista:
                napiSzobaLista = self._foglalasiLista[strDdatum]
                if napiSzobaLista is not None and szobaszam in napiSzobaLista:
                    if not csendben:
                        print(f"A megadott napra a megadott szoba már foglalt!")
                    return
            else:
                napiSzobaLista = []

        napiSzobaLista.append(szobaszam)

        szoba = list(self._szalloda.get_szobak())[0]

        self._foglalasiLista[strDdatum] = napiSzobaLista

        if not csendben:
            print(f"A foglalás sikeres!")
            print(f"Ár: {szoba.ar()}")

    def lemond(self, szobaszam, datum, csendben):
        napiSzobaLista = None
        strDdatum = str(datum)

        if self._foglalasiLista is None:
            if not csendben:
                print("Nincs iylen foglalás!")
            return
        else:
            if strDdatum in self._foglalasiLista:
                napiSzobaLista = self._foglalasiLista[strDdatum]
                if napiSzobaLista is not None and szobaszam not in napiSzobaLista:
                    if not csendben:
                        print(f"Nincs iylen foglalás!")
                    return
            else:
                if not csendben:
                    print(f"Nincs iylen foglalás!")
                return

        napiSzobaLista.remove(szobaszam)

        if not napiSzobaLista:
            del self._foglalasiLista[strDdatum]

        if not csendben:
            print(f"A foglalás törölve!")

    def foglalasLista(self):
        for key in list(self._foglalasiLista.keys()):
            print(f"{key}:")
            for value in self._foglalasiLista.get(key):
                print(f"{value}. szoba")

    def getElerhetoSzobak(self):
        for szoba in self._szalloda.get_szobak():
            print(szoba)


szoba1 = EgyagyasSzoba(30000, 1)
szoba2 = EgyagyasSzoba(35000, 2)
szoba3 = KetagyasSzoba(75000, 3)

szalloda = Szalloda("Teszt szálloda", {szoba1, szoba2, szoba3})
foglalas = Foglalas(szalloda)

foglalas.foglal(1, datetime.date(2023, 12, 1), True)
foglalas.foglal(2, datetime.date(2023, 12, 1), True)
foglalas.foglal(1, datetime.date(2023, 12, 4), True)
foglalas.foglal(3, datetime.date(2023, 12, 5), True)
foglalas.foglal(2, datetime.date(2023, 12, 5), True)

mainMenuKey = ''

while mainMenuKey != 'k':

    if mainMenuKey == '':
        foglalas.printMenu()

    if mainMenuKey == 'f':

        print(f"A foglaláshoz adja meg az adatokat")
        ev = input("Adja meg az évet (ÉÉÉÉ):")
        honap = input("Adja meg a hónapot (HH):")
        nap = input("Adja meg a napot (NN):")
        szobaszam = input("Adja meg a szobaszamot (1-3):")

        print(f"")
        print(f"")


        foglalas.printMenu()

        if ev is None or honap is None or nap is None or szobaszam is None or ev == '' or honap == '' or nap == '' or szobaszam == '':
            print(f"Hibás adatbevitel!")
        else:
            try:

                datum = datetime.date(int(ev), int(honap), int(nap))

                if (int(szobaszam) < 1 or int(szobaszam) > 3):
                    print(f"Hibás adatbevitel!")
                else:
                    foglalas.foglal(int(szobaszam), datum, False)
            except ValueError:
                print(f"Hibás adatbevitel!")

    if mainMenuKey == 'l':

        print(f"A lemondáshoz adja meg az adatokat")
        ev = input("Adja meg az évet (ÉÉÉÉ):")
        honap = input("Adja meg a hónapot (HH):")
        nap = input("Adja meg a napot (NN):")
        szobaszam = input("Adja meg a szobaszamot (1-3):")

        print(f"")
        print(f"")

        foglalas.printMenu()

        if ev is None or honap is None or nap is None or szobaszam is None or ev == '' or honap == '' or nap == '' or szobaszam == '':
            print(f"Hibás adatbevitel!")
        else:
            try:

                datum = datetime.date(int(ev), int(honap), int(nap))

                if (int(szobaszam) < 1 or int(szobaszam) > 3):
                    print(f"Hibás adatbevitel!")
                else:
                    foglalas.lemond(int(szobaszam), datum, False)
            except ValueError:
                print(f"Hibás adatbevitel!")

    if mainMenuKey == 'm':

        foglalas.printMenu()

        print(f"Az alábbi foglalások találhatók a rendszerben:")
        foglalas.foglalasLista()


    print(f"")
    mainMenuKey = input(" Válasszon menüpontot ::>> ")
