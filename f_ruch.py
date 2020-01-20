import f_plansza
import os
def ruchgora(gy,gx,n,stan,plansza,obiekty):
    if(stan==2):
        if(plansza[gy - 1][gx]== obiekty["sciana"] or plansza[gy - 1][gx]==obiekty["wrog"]):
            return gy
    if(gy>1):
        gy = gy - 1
    return gy
def ruchdol(gy,gx,n,stan,plansza,obiekty):
    if (stan == 2):
        if (plansza[gy + 1][gx] == obiekty["sciana"] or plansza[gy + 1][gx] == obiekty["wrog"]):
            return gy
    if (gy < n-2):
        gy = gy + 1
    return gy
def ruchlewo(gx,gy,n,stan,plansza,obiekty):
    if (stan == 2):
        if (plansza[gy][gx - 1] == obiekty["sciana"] or plansza[gy][gx - 1] == obiekty["wrog"]):
            return gx
    if (gx > 1):
        gx = gx - 1
    return gx
def ruchprawo(gx,gy,n,stan,plansza,obiekty):
    if (stan == 2):
        if (plansza[gy][gx + 1] == obiekty["sciana"] or plansza[gy][gx + 1] == obiekty["wrog"]):
            return gx
    if (gx < n - 2):
        gx = gx + 1
    return gx
def wyswietlruch(ruch,kierunkistrzalu,ruchy):
    if(ruch==ruchy["gora"]):
        print("Ruch w górę")
    elif (ruch == ruchy["dol"]):
        print("Ruch w dół")
    elif (ruch == ruchy["lewo"]):
        print("Ruch w lewo")
    elif (ruch == ruchy["prawo"]):
        print("Ruch w prawo")
    elif (ruch == str(kierunkistrzalu["gora"])):
        print("Strzal w gore")
    elif (ruch == str(kierunkistrzalu["dol"])):
        print("Strzal w dol")
    elif (ruch == str(kierunkistrzalu["lewo"])):
        print("Strzal w lewo")
    elif (ruch == str(kierunkistrzalu["prawo"])):
        print("Strzal w prawo")

def strzalgora(sx,sy,plansza,obiekty):
    if(sx == None or sy == None):
        return None
    if(plansza[sy-1][sx]!=obiekty["sciana"]):
        sy=sy-1
        return sy
    else:
        return None

def strzaldol(sx,sy,plansza,obiekty):
    if (sx == None or sy == None):
        return None
    if(plansza[sy+1][sx]!=obiekty["sciana"]):
        sy=sy+1
        return sy
    else:
        return None

def strzallewo(sx,sy,plansza,obiekty):
    if (sx == None or sy == None):
        return None
    if(plansza[sy][sx-1]!=obiekty["sciana"]):
        sx=sx-1
        return sx
    else:
        return None

def strzalprawo(sx,sy,plansza,obiekty):
    if (sx == None or sy == None):
        return None
    if(plansza[sy][sx+1]!=obiekty["sciana"]):
        sx=sx+1
        return sx
    else:
        return None

def kontynuacja_strzalu(strzal, sx, sy,strzalkierunek, plansza,obiekty,kierunkistrzalu):
    if (strzal == True):
        if (strzalkierunek == kierunkistrzalu["gora"]):
            sy = strzalgora(sx, sy, plansza,obiekty)
        elif (strzalkierunek == kierunkistrzalu["dol"]):
            sy = strzaldol(sx, sy, plansza,obiekty)
        elif (strzalkierunek == kierunkistrzalu["lewo"]):
            sx = strzallewo(sx, sy, plansza,obiekty)
        elif (strzalkierunek == kierunkistrzalu["prawo"]):
            sx = strzalprawo(sx, sy, plansza,obiekty)
        if (sy == None or sx == None):
            strzal = False
        if (strzal == True):
            plansza[sy][sx] = obiekty["pocisk_gracza"]
    return strzal, sx, sy, plansza

def przemieszczenie(gx,gy,n,stan,plansza,ruch,obiekty,ruchy):
    if (ruch == str(ruchy["gora"])):
        gy = ruchgora(gy, gx, n, stan, plansza,obiekty)
    elif (ruch == str(ruchy["dol"])):
        gy = ruchdol(gy, gx, n, stan, plansza,obiekty)
    elif (ruch == str(ruchy["lewo"])):
        gx = ruchlewo(gx, gy, n, stan, plansza,obiekty)
    elif (ruch == str(ruchy["prawo"])):
        gx = ruchprawo(gx, gy, n, stan, plansza,obiekty)
    return gx,gy

def wystrzal(ruch,ammo,stan,strzal,strzalkierunek,kierunkistrzalu):
    if (ruch == str(kierunkistrzalu["gora"]) and ammo > 0 and stan == 2 and strzal == False):
            ammo = ammo - 1
            strzal = True
            strzalkierunek = 8
    if (ruch == str(kierunkistrzalu["dol"]) and ammo > 0 and stan == 2 and strzal == False):
            ammo = ammo - 1
            strzal = True
            strzalkierunek = 5
    if (ruch == str(kierunkistrzalu["lewo"]) and ammo > 0 and stan == 2 and strzal == False):
            ammo = ammo - 1
            strzal = True
            strzalkierunek = 4
    if (ruch == str(kierunkistrzalu["prawo"]) and ammo > 0 and stan == 2 and strzal == False):
            ammo = ammo - 1
            strzal = True
            strzalkierunek = 6
    return ammo, strzal, strzalkierunek

def wlacz_debug(ruch,debug,kierunkistrzalu,ruchy):
    if (ruch == 'p'):
        if (debug == True):
            debug = False
        else:
            debug = True
    return debug

def wlacz_budowanie(ruch,bufor_sciana,stan):
    if (ruch == 'e'):
        if (stan != 2):
            if (bufor_sciana == True):
                bufor_sciana = False
            else:
                bufor_sciana = True
    return bufor_sciana

def innyruch(ruch,plansza,gy,gx):
    if(ruch!='w' or ruch!='a' or ruch!='s' or ruch!='d' or ruch!='p' or ruch!='q' or ruch!='e' or ruch!='4' or ruch!='8' or ruch!='5' or ruch!='6'):
        bufor_sciana = False
        f_plansza.postawsciane(plansza, gy, gx)

def trafienie_gracza(gx,gy,swx,swy,strzalwrog):
    if (strzalwrog == True):
        if (gx == swx and gy == swy):
            os.system("cls")
            return True

def ustaw_pocisk(strzal,gx,gy,sx,sy):
    if (strzal == 0):
        sy = gy
        sx = gx
        return sx,sy
    else:
        return sx,sy

def zebranie_amunicji(stan,gx,ax,gy,ay,ammo):
    if (stan == 2):
        if(gx == ax and gy == ay):
            ax=None
            ay=None
            ammo=20
    return ax,ay,ammo