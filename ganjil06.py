# Numpy digunakan untuk memproses array
# Matplotlib digunakan untuk memvisualisasikan data kordinat menjadi garis

import numpy as np
import matplotlib.pyplot as grafik

# menginput koordinat (x1,y1) dan koordinat (x2,y2)
x1 = int(input('Masukan nilai x1 : '))
y1 = int(input('Masukan nilai y1 : '))
x2 = int(input('Masukan nilai x2 : '))
y2 = int(input('Masukan nilai y2 : '))

# N adalah banyaknya iterasi yang dilakukan apabila x1 tidak sama dengan x2 atau y1 tidak sama dengan y2
nilaiY = y2 - y1
nilaiX = x2 - x1
N = x2 - x1 + 1

# titik awal x dan y
x = x1
y = y1


# Jika x1 = x2 (garis vertikal), maka :
# 1. y = y + 1 dan x tetap
# 2. gambar titik kordinat (x,y) 
# 3. tampilkan grafik 

if x1 == x2:
    titikA = []
    titikB = []
    for i in range (0,y2,1):
        print('Garis yang di lewati yaitu', x, ',', y+i)
        titikA.append(x)
        titikB.append(y+i)
    grafik.plot(titikA,titikB)
    grafik.show()
        
# Jika y1 = y2 (garis horizontal), maka :
# 1. x = x + 1 dan y tetap
# 2. gambar titik kordinat (x,y)
# 3. tampilkan grafik

elif y1 == y2:
    titikA = []
    titikB = []
    for i in range (0,x2,1):
        print('Garis yang di lewati yaitu', x+i, ',', y)
        titikA.append(x+i)
        titikB.append(y)
    grafik.plot(titikA,titikB)
    grafik.show()
      
# Jika 2 kondisi di atas salah, maka :
# 1. hitung kemiringan garis dengan m = (y2 - y1) / (x2 - x1) 
# 2. iterasi diulang sebanyak N
# 3. y = m ( x - x1 ) + y1
# 4. lakukan pembulatan pada y
# 5. gambar titik (x, y(pembulatan))
# 6. x = x + 1
        
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
        
# apppend digunakan untuk menambah item ke dalam array atau list
# grafik.plot digunakan agar mathplotlib membuat titik pertemuan kordinat x,y
# grafik.show digunakan agar mathplotlib menampilkan titik kordinat dari garis yang di lalui
        
    grafik.plot(titikA,titikB)
    grafik.show()
