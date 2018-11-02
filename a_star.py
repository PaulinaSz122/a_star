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


def stworz_liste_z():
    """Utworzenie tablicy do wpisywania wartości listy zamkniętej"""
    lista = []
    for i in range(X):
        lista.append([])
        for j in range(Y):
            lista[i].append(None)
    return lista
