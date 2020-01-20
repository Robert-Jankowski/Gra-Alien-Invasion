import os
import random
import generator_planszy
import getch
def graj(licznik_poziomow):
    i=losujplansze()
    while i==1:
        i=losujplansze()
        licznik_poziomow +=1
    ekrankoncowy(licznik_poziomow)
    return licznik_poziomow
def losujplansze():
    os.system("cls")
    pliki = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk('plansze/'):
        for file in f:
            if '.txt' in file:
                pliki.append(os.path.join(file))

    sep = '.'
    licznik = 1
    plikilista = []
    for i in range(len(pliki)):
        plikilista.append(str(licznik) + str('. ') + pliki[i][:-4])
        licznik += 1
    nr=(random.randint(0,len(plikilista)))
    nazwapliku =str('plansze/') + pliki[nr - 1]
    plik = open(nazwapliku, 'r')
    plansza = []
    n = 20
    x = plik.read().split('\n')
    plansza = []
    for i in range(n):
        plansza.append([])
        for j in range(n):
            b = x[i][j]
            plansza[i].append(b)
    os.system("cls")
    return(generator_planszy.generator_planszy(plansza, n, 2))

def ekrankoncowy(licznik_poziomow):
    os.system("cls")
    print("==================================")
    print("")
    print("           PRZEGRAŁEŚ             ")
    if(licznik_poziomow==0):
        print(" Przeszedłeś przez 0 pomieszczeń   ")
    elif(licznik_poziomow==1):
        print(" Przeszedłeś przez 1 pomieszczenie   ")
    elif(licznik_poziomow==2 or licznik_poziomow==3 or licznik_poziomow==4):
        print(" Przeszedłeś przez " + str(licznik_poziomow) + " pomieszczenia   ")
    else:
        print(" Przeszedłeś przez " + str(licznik_poziomow) + " pomieszczeń   ")
    print("")
    print("       ___")
    print("      /   \ ")
    print("     | RIP |")
    print("     |     |")
    print("     |     |")
    print("==================================")
    print("")
    print("WCISNIJ DOWOLNY KLAWISZ")
    i=getch.getch()
    os.system("cls")