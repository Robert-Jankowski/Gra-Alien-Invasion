# Alien Invasion
A command line Python game made in 2019 for Introduction to Programming course at University of Gdańsk. It is not an advanced and well-written program, but I like it anyway :)

## Running
---
```
python URUCHOM_GRE.py
```

## Controls
---
```
GENERAL
---------
w | Move up
a | Move left
s | Move down
d | Move right

FIGHT MODE
---------
8 | Shoot up
4 | Shoot left
5 | Shoot down
6 | Shoot right

BUILD MODE
---------
e | Place walls/stop placing

OTHER
---------
p | DEBUG
```

## Game rules
---
- The goal is to collect ammunition, which allows to shoot.
- You cannot pass current level without taking down your enemy.
- Ammunition appears randomly in every level.
- You can also create your own levels.

## Preview
---


### Menu
```
  __                        _
 / o|  ____                /_\
 |  /_/___/=              (@ @)
 | ====/            ____   \-/
 | \ \            o|_/==\__/ \
 | | |                     \ /\
 | | |                    _| |_

         ALIEN INVASION
--------------------------------
[1] Graj
[2] Generator planszy
[3] Sterowanie
[4] Wyjdź
--------------------------------
Obecny gracz: Robii
Obecny rekord: 31
```

### Game board
```
H H H H H H H H H H H H H H H H H H H H
H @         H                         H
H           H               H     H H H
H           H               H         H
H           H               H         H
H A   H H H H               H         H
H                           H         H
H           H     H H H H   H H H H H H
H           H           H             H
H   X       H           H             H
H           H           H             H
H           H           H             H
H           H H H H H H H             H
H                                     H
H   +                                 H
H     H H H       H H H H H     H H   H
H         H       H               H   H
H   W     H       H               H   H
H         H       H               H @ H
H H H H H H H H H H H H H H H H H H H H
Ammo | 0 | 20 |
```