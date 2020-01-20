import os
import nowa_plansza
import lista_plansz
import getch
def plansza_menu ():
    os.system("cls")
    print("Generator plansz  ")
    print("")
    print("[1] Nowa plansza")
    print("[2] Wczytaj planszę")
    print("[3] Usuń planszę")
    print("[0] Wyjście")

    print("---------------------")
    wybor = str(getch.getch())
    if (wybor == '1'):
        os.system("cls")
        nowa_plansza.nowa_plansza()
    elif (wybor == '2'):
        lista_plansz.odczyt()
    elif (wybor == '3'):
        lista_plansz.usunplansze()
    elif (wybor == '0'):
        os.system("cls")
        return 0
    else:
        plansza_menu()