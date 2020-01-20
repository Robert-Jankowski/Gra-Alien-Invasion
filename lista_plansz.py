import os
import generator_planszy

def usunplansze():
    nazwapliku=lista_plansz()
    if (nazwapliku == 0):
        os.system("cls")
        return 0
    nazwapliku = str('plansze/') + nazwapliku
    os.remove(nazwapliku)
    os.system("cls")

def lista_plansz():
    os.system("cls")
    pliki = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk('plansze/'):
        for file in f:
            if '.txt' in file:
                pliki.append(os.path.join(file))

    sep = '.'
    licznik=1
    plikilista = []
    for i in range(len(pliki)):
        plikilista.append(str(licznik) + str('. ') + pliki[i][:-4])
        licznik+=1
    print("0. [Wyjście]")
    for f in plikilista:
        print(f)
    print('-------------')
    print('Wybierz numer pliku: ')
    nr=int(input())
    if(nr==0):
        return 0
    nazwapliku =pliki[nr-1]
    return nazwapliku

def odczyt():
    nazwapliku=lista_plansz()
    if(nazwapliku==0):
        os.system("cls")
        return 0
    nazwapliku=str('plansze/') + nazwapliku
    plik = open(nazwapliku,'r')
    plansza = []
    n=20
    x=plik.read().split('\n')
    plansza= []
    for i in range(n):
        plansza.append([])
        for j in range(n):
            b = x[i][j]
            plansza[i].append(b)
    os.system("cls")
    generator_planszy.generator_planszy(plansza, n,0)