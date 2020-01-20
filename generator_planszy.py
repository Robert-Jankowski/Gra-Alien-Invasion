import f_plansza
import f_ruch
import os
import getch
import graj
import f_wrog
def generator_planszy(plansza,n,stan):

    #USTAWIENIA POCZĄTKOWE#
    obiekty = {
        "sciana" : 'H',
        "gracz" : 'X',
        "wrog" : 'W',
        "ammo" : 'A',
        "puste_pole" : ' ',
        "pocisk_gracza" : '*',
        "pocisk_wroga" : '+',
        "portal" : '@'
    }
    kierunkistrzalu = {
        "lewo" : 4,
        "prawo" : 6,
        "gora" : 8,
        "dol" : 5
    }
    ruchy = {
        "lewo" : 'a',
        "prawo" : 'd',
        "gora" : 'w',
        "dol" : 's'
    }

    gy = 1  # y gracza (wiersz)
    gx = 2  # x gracza (kolumna)
    if stan==1: #jeśli tryb nowej planszy
        f_plansza.generujplansze(plansza, n, obiekty) #tworzenie nowej planszy
    plansza[1][1]= obiekty["portal"] #ustawienie portalu wejściowego
    plansza[18][18] = obiekty["portal"] #ustawienie portalu wyjściowego
    ax=None #zadeklarowanie pozycji amunicji
    ay=None #-----------------------------#
    if(stan==2): #jeżeli tryb gry
        wx,wy = f_wrog.losujpozycjewroga(plansza,'wrog',obiekty) #losowanie pozycji wroga
        ax,ay = f_wrog.losujpozycjewroga(plansza,'ammo',obiekty) #losowanie pozycji amunicji
        wrog=True #wróg żyje

    ammo = 0 #początkowa wartość
    plansza[gy][gx] = obiekty["gracz"]
    f_plansza.drukuj_plansze(plansza) #wyświetl planszę
    bufor_sciana = False
    debug = False
    strzalteraz = False
    strzal = False #czy gracz wystrzelił
    strzalwrog = False #czy wróg wystrzelił
    strzalkierunek = 0 #kierunek strzalu gracza
    strzalwrogkierunek = 0 #kierunek strzalu wroga
    sx = None #pozycja pocisku gracza
    sy = None #----------------------
    ruch = '' #input gracza


    while ruch != 'q': #dopóki gracz nie wyjdzie przez 'q' (lub nie przegra)
        if(stan==2): #czynności wykonywane tylko w trybie gry
            sx,sy = f_ruch.ustaw_pocisk(strzal,gx,gy,sx,sy) #ustaw pocisk w miejscu gracza, jeśli nie wystrzelony
            plansza[sy][sx] = obiekty["puste_pole"] #czyszczenie pocisku gracza
            if(wrog): #czynności jeśli wróg żyje
                if(strzalwrog==0): #jeśli pocisk wroga nie został wystrzelony
                    swy = wy #ustawienie pozycji pocisku wroga na pozycje wroga
                    swx = wx #-------------------------------------------------
                    if(f_wrog.czywrogmozestrzelic(plansza,wx,wy,gx,gy,obiekty)): #sprawdzenie, czy gracz jest w linii strzału
                        swx=wx #ustawienie pozycji pocisku wroga na pozycje wroga
                        swy=wy #-------------------------------------------------
                        strzalwrogkierunek=f_wrog.kierunekstrzaluwroga(wx,wy,gx,gy) #ustalenie kierunku wystrzału wroga
                        strzalwrog= True #pocisk się pojawia
                        strzalteraz= True #wróg właśnie strzela (nie poruszy się w tej turze)
            f_wrog.czyszczenie_pocisku_wroga(swx, swy, wx, wy, plansza,wrog,obiekty) #poprzednia pozycja pocisku wroga zostaje wyczyszczona
            swx,swy, strzalwrog = f_wrog.strzalwroga(strzalwrogkierunek, swx, swy, strzalwrog, plansza,obiekty,kierunkistrzalu) #pocisk wroga zmienia pozycję
            if (f_ruch.trafienie_gracza(gx, gy, swx, swy, strzalwrog)): #trafienie gracza pociskiem
                return 0 #przegranie gry

        ruch = getch.getch() #ruch gracza

        os.system("cls")
        f_plansza.czy_e_wcisniete(bufor_sciana,plansza,gx,gy,obiekty) #postawienie ściany jeśli e wciśnięte
        gx,gy = f_ruch.przemieszczenie(gx, gy, n, stan, plansza, ruch,obiekty,ruchy) #poruszenie gracza jeśli w,a,s,d wciśnięte
        ammo, strzal, strzalkierunek = f_ruch.wystrzal(ruch, ammo, stan, strzal, strzalkierunek,kierunkistrzalu) #strzał, jeśli 8,4,5,6 wciśnięte
        debug = f_ruch.wlacz_debug(ruch,debug,kierunkistrzalu,ruchy) #włącz debug jeśli p wciśnięte
        bufor_sciana = f_ruch.wlacz_budowanie(ruch,bufor_sciana,stan) #włączenie budowania jeśli e naciśnięte
        ax, ay, ammo = f_ruch.zebranie_amunicji(stan, gx, ax, gy, ay, ammo)  # zebranie amunicji

        if(stan==2):
            if (strzalteraz == False):
                plansza[wy][wx] = obiekty["puste_pole"] #czyszczenie poprzedniej pozycji wroga
                wx,wy = f_wrog.ruchwroga(wx, wy, plansza,obiekty) #poruszenie wroga, jeśli właśnie nie strzela
            strzalteraz = False #wróg znowu zaczyna się poruszać po wystrzale
            strzal, sx, sy, plansza = f_ruch.kontynuacja_strzalu(strzal, sx, sy, strzalkierunek, plansza,obiekty,kierunkistrzalu) #wystrzelony pocisk gracza leci dalej
            if(wx==sx and wy == sy): #jeśli pocisk trafi wroga
                wrog=False #wróg ginie
            if (gx == swx and gy == swy): #jeśli gracz wejdzie na pozycję pocisku
                return 0 #przegranie gry


        plansza[1][1] = obiekty["portal"]
        plansza[gy][gx] = obiekty["gracz"]
        plansza[18][18] = obiekty["portal"]
        if(stan==2): #jeśli tryb gry
            if(wrog): #jeśli wróg żyje
                plansza[wy][wx]=obiekty["wrog"] #ustawienie wizualnej pozycji wroga
        f_plansza.drukuj_plansze(plansza) #wyświetlanie planszy
        if(stan==2): #jeśli tryb gry
            f_plansza.ammo_wyswietl(ammo) #wyświetl stan amunicji
            f_plansza.debug_wyswietl(debug,ruch,gx,gy,swx,swy,strzalwrogkierunek,kierunkistrzalu,ruchy) #wyświetl debug jeśli włączony


        if (plansza[gy][gx] == obiekty["portal"]): #jeżeli gracz stanie na portalu wyjściowym
            if (stan == 2): #jeśli tryb gry
                if (wrog == False): #jeśli wróg nie żyje
                    return 1 #przejdź do kolejnego poziomu
        if (ruch == 'q'): #jeśli gracz wciśnie q
            if(stan==2): #jeśli tryb gry
                return 0 #przegranie gry
            else: #jeśli tryb budowy
                f_plansza.zapytaj_plansza(plansza) #rozpocznij proces zapisu
            break