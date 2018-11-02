import math
X = 20
Y = 20


class Pole(object):
    def __init__(self, x, y, l_krokow, h, rodzic_x, rodzic_y):
        self.x = x
        self.y = y
        self.l_krokow = l_krokow
        self.h = h
        self.rodzic_x = rodzic_x
        self.rodzic_y = rodzic_y

    def change(self, l_krokow, h, rodzic_x, rodzic_y):
        self.l_krokow = l_krokow
        self.h = h
        self.rodzic_x = rodzic_x
        self.rodzic_y = rodzic_y


def dodaj_o(lista, x, y, l_krokow, h, rodzic_x, rodzic_y):
    pole = Pole(x, y, l_krokow, h, rodzic_x, rodzic_y)
    lista.append(pole)


def dodaj_z(lista_zamknieta, pole_o, lista_otwarta):
    lista_zamknieta[pole_o.x][pole_o.y] = pole_o
    lista_otwarta.delete(pole_o)


def stworz_liste_z(x, y):
    """Utworzenie tablicy do wpisywania wartości listy zamkniętej"""
    lista = []
    for i in range(x):
        lista.append([])
        for j in range(y):
            lista[i].append(None)
    return lista


def wczytaj_grid(nazwa_pliku):
    mount_of_lines = 0
    mapa = []
    plik = open(nazwa_pliku, "r")
    for line in plik:
        mapa.append([])
        for field in line:
            if field != " " and field != "\n":
                mapa[mount_of_lines].append(field)
        mount_of_lines += 1
    return mapa


mapa = wczytaj_grid("grid.txt")
for line in mapa:
    for field in line:
        print(field, end=" ")
    print()

