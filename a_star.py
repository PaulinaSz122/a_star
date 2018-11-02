import math
X = 20
Y = 20
S_X = 0
S_Y = 0
C_X = X - 1
C_Y = Y - 1
GORA = (0, -1)
DOL = (0, 1)
PRAWO = (1, 0)
LEWO = (-1, 0)


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
    plik.close()
    return mapa


def przeszukaj(lista, pole):
    found = False
    for field in lista:
        if field != None and field.x == pole.x and field.y == pole.y:
            found = True
            if field.l_krokow > pole.l_krokow:
                field.change(pole.l_krokow, pole.h, pole.rodzic_x, pole.rodzic_y)
    return found


def sprawdz_pole(pole, kierunek, lista_zamknieta, lista_otwarta, mapa):
    x = pole.x + kierunek[0]
    y = pole.y + kierunek[1]
    if mapa[x][y] != "5" and 0 >= x > X and 0 >= y > Y:
        l_krokow = pole.l_krokow + 1
        h = math.sqrt(pow(x - C_X, 2) + pow(y - C_Y, 2)) + l_krokow
        nowe = Pole(x, y, l_krokow, h, pole.x, pole.y)
        found_o = przeszukaj(lista_zamknieta, nowe)
        found_z = przeszukaj(lista_otwarta, nowe)
        if not found_o and not found_z:
            lista_otwarta.append(nowe)


def szukaj_min(lista):
    h = 100
    pole = None
    for field in lista:
        if h > field.h:
            pole = field
            h = field.h
    return pole


def main():
    mapa = wczytaj_grid("grid.txt")
    lista_zamknieta = stworz_liste_z(X, Y)
    lista_otwarta = []
    x = S_X
    y = S_Y
    ostatnie = Pole(x, y, 0, 0, x, y)
    lista_zamknieta[x][y] = ostatnie

    while not x == C_X and not y == C_Y:
        sprawdz_pole(ostatnie, GORA, lista_zamknieta, lista_otwarta, mapa)
        sprawdz_pole(ostatnie, DOL, lista_zamknieta, lista_otwarta, mapa)
        sprawdz_pole(ostatnie, PRAWO, lista_zamknieta, lista_otwarta, mapa)
        sprawdz_pole(ostatnie, LEWO, lista_zamknieta, lista_otwarta, mapa)
        if not lista_otwarta == []:
            ostatnie = szukaj_min(lista_otwarta)
            lista_otwarta.remove(ostatnie)




main()
