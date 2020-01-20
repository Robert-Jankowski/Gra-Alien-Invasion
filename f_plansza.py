import os
import getch
import f_ruch
def zapis(plansza):
    print('Podaj nazwe pliku: ')
    nazwa=str('plansze/')+str(input())+str('.txt')
    plik = open(nazwa, 'w+')
    for i in plansza:
        plik.writelines(i)
        plik.write('\n')
    plik.close()
def zapytaj_plansza(plansza):
    print("Czy chcesz zapisać planszę ? (t/n)")
    odpowiedz = getch.getch()
    if(odpowiedz=='t'):
        os.system("cls")
        zapis(plansza)
        os.system("cls")
    elif(odpowiedz=='n'):
        os.system("cls")
    else:
        zapytaj_plansza(plansza)

def drukuj_plansze(plansza):
    for i in plansza:
        for j in i:
            print(j + ' ',end='')
        print()

def generujplansze(plansza,n,obiekty):
    for i in range(n):
        plansza.append([])  # generowanie wierszy
        for j in range(n):
            plansza[i].append([])  # generowanie kolumn
    for i in range(n):
        for j in range(n):
            if (i == 0 or i == (n - 1) or j == 0 or j == (n - 1)):
                plansza[j][i] = obiekty["sciana"]         #wypelnianie scian 'H'
            else:
                plansza[j][i] = obiekty["puste_pole"]         #wypelnianie wnetrza

def postawsciane(plansza,gy,gx):
    plansza[gy][gx]='H'

def debug_wyswietl(debug,ruch,gx,gy,swx,swy,strzalwrogkierunek,kierunkistrzalu,ruchy):
    if (debug == True):
        f_ruch.wyswietlruch(ruch,kierunkistrzalu,ruchy)
        print('gX: ' + str(gx) + ' gY: ' + str(gy))
        print('sX: ' + str(swx) + ' sY: ' + str(swy))

def czy_e_wcisniete(bufor_sciana,plansza,gx,gy,obiekty):
    if (bufor_sciana == True):
        plansza[gy][gx]=obiekty["sciana"]
    else:
        plansza[gy][gx]=obiekty["puste_pole"]

def ammo_wyswietl(ammo):
    print('Ammo | ' + str(ammo) + ' | 20 |')