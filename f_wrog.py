import random
import f_ruch

def losujpozycjewroga(plansza,czywrog,obiekty):
    wlasciwa_pozycja=0
    while(wlasciwa_pozycja==0):
        wx = (random.randint(1, 18))
        wy = (random.randint(1, 18))
        if(plansza[wy][wx]==' '):
            wlasciwa_pozycja=1
    if(czywrog == 'wrog'):
        plansza[wy][wx] = obiekty["wrog"]
    else:
        plansza[wy][wx] = obiekty["ammo"]
    return wx,wy

def czywrogmozestrzelic(plansza,wx,wy,gx,gy,obiekty):
    if(gx==wx or gy==wy):
        if(gy==wy):
            if(gx<wx):
                bufor=gx
                while(bufor!=wx):
                    if(plansza[gy][bufor]==obiekty["sciana"]):
                        return False
                    bufor=bufor + 1
                return True
            if (gx > wx):
                bufor = gx
                while (bufor != wx):
                    if (plansza[gy][bufor] == obiekty["sciana"]):
                        return False
                    bufor = bufor - 1
                return True
        if (gx == wx):
            if (gy < wy):
                bufor = gy
                while (bufor != wy):
                    if (plansza[bufor][gx] == obiekty["sciana"]):
                        return False
                    bufor = bufor + 1
                return True
            if (gy > wy):
                bufor = gy
                while (bufor != wy):
                    if (plansza[bufor][gx] == obiekty["sciana"]):
                        return False
                    bufor = bufor - 1
                return True

    else:
        return False

def kierunekstrzaluwroga(wx,wy,gx,gy):
    if(gx==wx):
        if(gy>wy):
            return 5
        else:
            return 8
    if (gy == wy):
        if (gx > wx):
            return 6
        else:
            return 4

def ruchwroga(wx,wy,plansza,obiekty):
    i = random.randint(1, 4)

    if(i == 1):
        if(not(plansza[wy-1][wx]== obiekty["sciana"] or plansza[wy-1][wx]== obiekty["ammo"] or plansza[wy-1][wx]== obiekty["gracz"] or plansza[wy-1][wx]==obiekty["pocisk_gracza"])):
            wy=wy-1
        else:
            wx,wy = ruchwroga(wx,wy,plansza,obiekty)
            return wx,wy
    if (i == 2):
        if (not(plansza[wy + 1][wx] == obiekty["sciana"] or plansza[wy + 1][wx] == obiekty["ammo"] or plansza[wy + 1][wx] == obiekty["gracz"] or plansza[wy-1][wx]==obiekty["pocisk_gracza"])):
            wy = wy + 1
        else:
            wx, wy = ruchwroga(wx, wy, plansza,obiekty)
            return wx, wy
    if (i == 3):
        if (not(plansza[wy][wx-1] == obiekty["sciana"] or plansza[wy][wx-1] == obiekty["ammo"] or plansza[wy][wx-1] == obiekty["gracz"] or plansza[wy-1][wx]==obiekty["pocisk_gracza"])):
            wx = wx - 1
        else:
            wx, wy = ruchwroga(wx, wy, plansza,obiekty)
            return wx, wy
    if (i == 4):
        if (not(plansza[wy][wx + 1] == obiekty["sciana"] or plansza[wy][wx + 1] == obiekty["ammo"] or plansza[wy][wx + 1] == obiekty["gracz"] or plansza[wy-1][wx]==obiekty["pocisk_gracza"])):
            wx = wx + 1
        else:
            wx, wy = ruchwroga(wx, wy, plansza,obiekty)
            return wx, wy

    return wx,wy

def strzalwroga(strzalwrogkierunek, swx,swy,strzalwrog,plansza,obiekty,kierunkistrzalu):
    if (strzalwrogkierunek == kierunkistrzalu["gora"]):
        swy = f_ruch.strzalgora(swx, swy, plansza,obiekty)
    elif (strzalwrogkierunek == kierunkistrzalu["dol"]):
        swy = f_ruch.strzaldol(swx, swy, plansza,obiekty)
    elif (strzalwrogkierunek == kierunkistrzalu["lewo"]):
        swx = f_ruch.strzallewo(swx, swy, plansza,obiekty)
    elif (strzalwrogkierunek == kierunkistrzalu["prawo"]):
        swx = f_ruch.strzalprawo(swx, swy, plansza,obiekty)
    if (swy == None or swx == None):
        strzalwrog = False
    if (strzalwrog == True):
        plansza[swy][swx] = obiekty["pocisk_wroga"]
    return swx,swy,strzalwrog

def czyszczenie_pocisku_wroga(swx,swy,wx,wy,plansza,wrog,obiekty):
    if(wrog):
        if (not (swx == wx and swy == wy)):
            plansza[swy][swx] = obiekty["puste_pole"]
    else:
        if(swx!=None and swy!=None):
            plansza[swy][swx]= obiekty["puste_pole"]