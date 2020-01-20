import plansza_menu
import graj
import os
import getch

def usun_gracza():
    plik = open("gracze.txt", 'r')
    gracze = []
    bufor = plik.read().splitlines()
    plik.close()
    for i in range(len(bufor)):
        j = bufor[i].split()
        gracze.append(j)
    for i in range(len(bufor)):
        print(str(i + 1) + ". " + str(gracze[i][0] + " | Rekord: " + str(gracze[i][1])))
    print("--------------------")
    print("Podaj numer gracza: ")
    nr = int(input())
    nr = nr - 1
    plik = open("gracze.txt", 'w')
    zapis = []
    for k in range(len(bufor)):
        zapis.append(str(gracze[k][0]) + ' ' + str(gracze[k][1]))
    licznik=0
    for m in zapis:
        if(licznik!=nr):
            plik.writelines(m)
            plik.write('\n')
            licznik+=1
        else:
            licznik+=1

def nadpisz_wynik(nr,rekord):
    plik = open("gracze.txt", 'r')
    gracze = []
    bufor = plik.read().splitlines()
    plik.close()
    for i in range(len(bufor)):
        j = bufor[i].split()
        gracze.append(j)
    gracze[nr][1] = rekord
    zapis = []
    for k in range(len(bufor)):
        zapis.append(str(gracze[k][0]) + ' ' +str(gracze[k][1]))
    plik = open("gracze.txt", 'w')
    for m in zapis:
        plik.writelines(m)
        plik.write('\n')

def nowy_gracz(j):
    plik = open("gracze.txt", 'a')
    gracz=str(j) + " 0"
    plik.write(gracz)
    plik.write("\n")

    plik.close()

def odczyt_graczy():
    plik = open("gracze.txt", 'r')
    gracze = []
    bufor = plik.read().splitlines()
    plik.close()
    for i in range(len(bufor)):
        j = bufor[i].split()
        gracze.append(j)
    for i in range(len(bufor)):
        print(str(i+1) + ". " + str(gracze[i][0] + " | Rekord: " + str(gracze[i][1])))
    print("--------------------")
    print("Podaj numer gracza: ")
    nr = int(input())
    nr = nr-1
    j = str(gracze[nr][0])
    k = str(gracze[nr][1])
    return j, k, nr

def menu(gracz,nr):
    max = int(gracz["punkty"])
    print("  __                        _")
    print(" / o|  ____                /_\ ")
    print(" |  /_/___/=              (@ @)")
    print(" | ====/            ____   \-/")
    print(" | \ \            o|_/==\__/ \ ")
    print(" | | |                     \ /\ ")
    print(" | | |                    _| |_ ")
    print("")
    print("         ALIEN INVASION         ")
    print("--------------------------------")
    print("[1] Graj")
    print("[2] Generator planszy")
    print("[3] Sterowanie")
    print("[4] Wyjdź")
    print("--------------------------------")
    print("Obecny gracz: " +  str(gracz["nick"]))
    print("Obecny rekord: " + str(gracz["punkty"]))
    wybor = str(getch.getch())
    if (wybor == '1'):
        rekord = graj.graj(0)
        if(rekord > max):
            gracz["punkty"]= rekord
            nadpisz_wynik(nr,rekord)

    elif (wybor == '2'):
        plansza_menu.plansza_menu()
    elif (wybor == '3'):
        os.system("cls")
        print("OGOLNE")
        print("---------")
        print("w | Ruch w gore")
        print("a | Ruch w lewo")
        print("s | Ruch w dol")
        print("d | Ruch w prawo")
        print("")
        print("TRYB GRY")
        print("---------")
        print("8 | Strzal w gore")
        print("4 | Strzal w lewo")
        print("5 | Strzal w dol")
        print("6 | Strzal w prawo")
        print("")
        print("TRYB BUDOWY")
        print("---------")
        print("e | Stawiaj za soba sciany/przestan stawiac")
        print("")
        print("INNE")
        print("---------")
        print("p | DEBUG")
        print("")
        print("WCISNIJ DOWOLNY KLAWISZ")
        i= getch.getch()
        os.system("cls")
    elif (wybor == '4'):
        return False
    else:
        os.system("cls")
        return True
    return True
def wyborgracza():
    i= '3'
    while(i=='3'):
        os.system("cls")
        print("[1] ISTNIEJĄCY GRACZ")
        print("[2] NOWY GRACZ")
        print("[3] USUŃ GRACZA")
        i = str(getch.getch())

        if(i=='1'):
            os.system("cls")
            j,k,nr = odczyt_graczy()
            gracz = {
                "nick": j,
                "punkty": k
            }
        elif(i=='2'):
            os.system("cls")
            print("Podaj nick: ")
            j = input()
            nowy_gracz(j)
            gracz = {
                "nick" : j,
                "punkty" : 0
            }
            nr = sum(1 for line in open('gracze.txt')) + 1
        elif(i=='3'):
            os.system("cls")
            usun_gracza()
            i='3'
        else:
            i='3'
        os.system("cls")

    gra = True
    while gra == True:
        gra = menu(gracz,nr)

