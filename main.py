def read_file(nazwa, tab1, tab2):
    with open(nazwa, "r") as odczyt:
        ilosc = int(odczyt.readline())

        for i in range(ilosc):
            wart1, wart2 = map(float, odczyt.readline().split())
            tab1.append(wart1)
            tab2.append(wart2)

        return ilosc

def interpolacja_newtona(ilosc, xi, fxi, punkt, wspolczynnik_b):
    wspolczynnik_p = []
    wspolczynnik_p.append(1)

    wspolczynnik_b.append(fxi[0])

    for h in range(1, ilosc):
        b_k = 0
        for i in range(0, h+1):
            licznik = fxi[i]
            mianownik = 1
            for j in range(0, h+1):
                if i != j:
                    mianownik *= (xi[i]-xi[j])

            b_k += (licznik/mianownik)

        wspolczynnik_b.append(b_k)

    for h in range(1, ilosc):
        p_k = 1
        for i in range(0, h):
            p_k *= (punkt - xi[i])

        wspolczynnik_p.append(p_k)

    wynik = 0
    for i in range(0, ilosc):
        wynik += wspolczynnik_p[i]*wspolczynnik_b[i]

    return wynik

def main():
    xi = []
    fxi = []
    ilosc = read_file("MN_02.txt", xi, fxi)
    print(f"Liczba wezlow interpolacji wynosi {ilosc}")
    print(f"Wezly interpolacji: {xi}")
    print(f"Wartosci funkcji w wezlach: {fxi}")
    punkt = float(input("Podaj wartosc punktu do obliczen: "))
    b_k = []
    wynik = interpolacja_newtona(ilosc, xi, fxi, punkt, b_k)
    print(f"Wartosc funkcji dla danego punktu: {wynik}")
    print(f"Wspolczynniki wielomianu Newtona: {b_k}")



if __name__ == "__main__":
    main()