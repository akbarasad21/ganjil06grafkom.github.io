import numpy as np
import matplotlib.pyplot as grafik

x1 = int(input('Masukan x1 : '))
y1 = int(input('Masukan y1 : '))
x2 = int(input('Masukan x2 : '))
y2 = int(input('Masukan y2 : '))

nilaiY = y2 - y1
nilaiX = x2 - x1
N = x2 - x1 + 1

x = x1
y = y1

i = 1


if x1 == x2:
    titikA = []
    titikB = []
    for i in range (1,y2,1):
        grafik.plot(titikA,titikB)
        grafik.show()

elif y1 == y2:
    titikA = []
    titikB = []
    for i in range (1,y2,1):
        grafik.plot(titikA,titikB)
        grafik.show()
        
else:
    titikA = []
    titikB = []
    for i in range (0,N,1):
        m = nilaiY / nilaiX
        rumusY = m * (x - x1) + y1
        kordinatY = round(rumusY)
        print('Garis yang di lewati yaitu', x,',', kordinatY)
        titikA.append(x)
        titikB.append(kordinatY)
        x+=1
