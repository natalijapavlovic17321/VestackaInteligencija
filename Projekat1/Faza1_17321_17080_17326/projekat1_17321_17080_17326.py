import numpy as np
import random

tabla=[]
x1=()
x2=()
o1=()
o2=()
player1=True
moved=False
n=0
m=0
pozicije={}
cijiPotez="x"
xZidovi=0
oZidovi=0
def Tabla(n, m ,p1,p2,p3,p4):
    tabla = [ [" "  for i in range(m)] for j in range(n) ]
    for i in range(n-1):
        for j in range(m-1):
            if(i%2==0 and j%2==0):
                tabla[i][j]="   "
            elif i%2==1 and j%2==1:
                tabla[i][j]="   "
            if i%2==1 and j%2==0:
                tabla[i][j]="___"
            if j%2==1 and i%2==0:
                tabla[i][j]=" | "
 
    tabla[p1[0]][p1[1]]=" X "
    tabla[p2[0]][p2[1]]=" X "
    tabla[p3[0]][p3[1]]=" O "
    tabla[p4[0]][p4[1]]=" O "
    return tabla

def printT():
    global n
    global m
    a = np.array(tabla)
    for line in a:
       print ('  '.join(map(str, line)))

def endGame():
    global pozicije 
    global x1
    global x2
    global o1
    global o2
    px1i=[x1[0],x1[1]]
    px2i=[x2[0],x2[1]]
    po1i=[o1[0],o1[1]]
    po2i=[o2[0],o2[1]]
    if (pozicije["px1"]==po1i or pozicije["px1"]==po2i or pozicije["px2"]==po1i or pozicije["px2"]==po2i ):
        print("Korisnik X je pobedio")
        return True
    if (pozicije["po1"]==px1i or pozicije["po1"]==px2i or pozicije["po2"]==px1i or pozicije["po2"]==px2i ):
        print("Korisnik O je pobedio")
        return True
    return False
    
def inputT():
    global n
    global m
    global x1
    global x2
    global o1
    global o2
    print("Unesite n da bude neparan broj. Ukoliko ne zelite unesite 0")
    n=(int)(input())
    while (n%2 == 0 and n!=0) or (n<=11 and n>=22):
        print("Unesite n da bude neparan broj. Ukoliko ne zelite unesite 0")
        n=(int)(input())
    if(n == 0):
       n=11
    n=2*n
    print("Unesite m da bude paran broj. Ukoliko ne zelite unesite 0")
    m=(int)(input())
    while (m%2!=0 and m!=0) or (m<=14 and m>=28):
        print("Unesite m da bude paran broj. Ukoliko ne zelite unesite 0")
        m=(int)((int)(input()))
    if(m == 0):
       m=14
    m=2*m
    print()
    print("Unesite pocetna polja prve figure, ukoliko ne zelite unesite 0 0")
    a, b = input().split()     
    if(int(a)==1 or int(a)==n or int(b)==1 or int(b)==m):
        print("Unesite pocetna polja prve figure, nije moguce postaviti figure na ivicama table, ukoliko ne zelite unesite 0 0")
        a, b = input().split()
    if(int(a)==0 or int(b)==0):
       a=4
       b=4
    x1=(2*(int(a)-1),2*(int(b)-1))
    print("Unesite pocetna polja druge figure, ukoliko ne zelite unesite 0 0")
    a, b = input().split()
    if(int(a)==1 or int(a)==n or int(b)==1 or int(b)==m):
        print("Unesite pocetna polja prve figure, nije moguce postaviti figure na ivicama table, ukoliko ne zelite unesite 0 0")
        a, b = input().split()
    if(int(a)==0 or int(b)==0):
       a=8
       b=4
    x2=(2*(int(a)-1),2*(int(b)-1))
    o1=x1
    o2=x2
    brojZidova()
    XorO()
    Mirror()
def XorO():
    global player1
    pom=random.randint(0, 1)
    if(pom == 0):
        print("Korisnik je X. Prvi igrate.")
        player1=True
    else: 
        print("Korisnik je O. Sacekajte na svoj potez.")
        player1=False
def Mirror():
    global x1
    global x2
    global o1
    global o2
    global pozicije
    pom1=int(((n-x1[0])-4))
    pom2=int(((m-x1[1])-4))
    pom3=int(((n-x2[0])-4))
    pom4=int(((m-x2[1])-4))
    if(player1):
        o1=(pom1,pom2)
        o2=(pom3,pom4)
    else:
        x1=(pom1,pom2)
        x2=(pom3,pom4)
    px1i=[x1[0],x1[1]]
    px2i=[x2[0],x2[1]]
    po1i=[o1[0],o1[1]]
    po2i=[o2[0],o2[1]]
    pozicije['px1']=px1i
    pozicije['px2']=px2i
    pozicije['po1']=po1i
    pozicije['po2']=po2i

def brojZidova():
    global n
    global xZidovi
    global oZidovi
    print("Unesite broj zidova koji zelite da koristite tokom partije. (broj mora biti manji od 19 i veci od 8)")
    print("Ukoliko zelite koristiti defaultne vrednosti unesite 0")
    xZidovi=(int)(input())
    while xZidovi!=0 and (xZidovi<9 and xZidovi>18):
        print("Broj zidova mora biti veci od 9(ili 9) i manji od 18 (ili 18)")
        xZidovi=(int)((int)(input()))
    if(xZidovi == 0):
        if(n==22):
            xZidovi=18
        else:
            xZidovi=n-2
    oZidovi = xZidovi
    print(xZidovi)

def findShortestPath(player, end):
    path = []
    queue = [[player]]
    while queue:
        curr, *queue = queue
        pos = curr[-1]
        if end[0] > pos[0] and end[1] > pos[1]:
            nextPos = (pos[0] + 1, pos[1] + 1)
        elif end[0] > pos[0] and end[1] < pos[1]:
            nextPos = (pos[0] + 1, pos[1] - 1)
        elif end[0] < pos[0] and end[1] > pos[1]:
            nextPos = (pos[0] - 1, pos[1] + 1)
        elif end[0] < pos[0] and end[1] < pos[1]:
            nextPos = (pos[0] - 1, pos[1] - 1)
        elif end[0] > pos[0]:
            nextPos = (pos[0] + 1, pos[1])
        elif end[0] < pos[0]:
            nextPos = (pos[0] - 1, pos[1])
        elif end[1] > pos[1]:
            nextPos = (pos[0], pos[1] + 1)
        else:
            nextPos = (pos[0], pos[1] - 1)
        if nextPos == end and (not path or len(curr) + 1 < len(path)):
            path = curr + [end]
        elif nextPos not in curr:
            queue += [curr + [nextPos]]
    return path


print(findShortestPath((5, 5), (4, 3)))
    
def plavi():
    global tabla
    global n
    global m 
    global xZidovi
    global oZidovi
    print("Unesite vrstu i kolonu")
    try:
        x, y = [int(i) for i in input().split()]
        x *= 2
        y *= 2
        while (x>=n-1 or y>=m-1 or x <= 0 or y <= 0 or tabla[x-1][y-2] == "===" or tabla[x-1][y] == "===" or tabla[x-2][y-1] == " ?? " and tabla[x][y-1] == " ?? "):
            print("Ne mozete tu postaviti zid, unesite neku drugu vrednost za vrstu i kolonu")
            
            x, y = [int(i) for i in input().split()]
            x *= 2
            y *= 2 
            
        tabla[x-1][y-2] = "==="
        tabla[x-1][y] = "==="            
    except ValueError:
            print("Nevalidan unos")
            plavi()    
              
def zeleni():
    global tabla
    global n
    global m
    print("Unesite vrstu i kolonu")
    try:
        x, y = [int(i) for i in input().split()]
        x *= 2
        y *= 2
        while (x>=n-1 or y>=m-1 or x <= 0 or y <= 0 or tabla[x-1][y-2] == "===" and tabla[x-1][y] == "===" or tabla[x-2][y-1] == " ?? " or tabla[x][y-1] == " ?? "):
            print("Ne mozete tu postaviti zid, unesite neku drugu vrednost za vrstu i kolonu")
            
            x, y = [int(i) for i in input().split()]
            x *= 2
            y *= 2   
            
        tabla[x-2][y-1] = " ?? "
        tabla[x][y-1] = " ?? "
    except ValueError:
        print("Nevalidan unos")
        zeleni()    
def zid():
    global xZidovi
    global oZidovi
    global cijiPotez   
    if (cijiPotez == 'x'):
        if (xZidovi == 0 ):
            print("Nemate vise zidova za postavljanje")
            return
        print("Unesite p ukoliko zelite da postavite plavi zid (horizontalni) ili z ukoliko zelite zeleni (vertikalni)")
        slovo = input()
        while (slovo != 'p' and slovo != 'z'):
            print("Nevalidan unos, unesite ponovo")
            slovo = input()  
        if (slovo == 'p'):
            print("Plavi zid:")
            plavi()
            xZidovi -= 1
        elif (slovo == 'z'):
            print("Zeleni zid:")
            zeleni()
            xZidovi -= 1
    else:
        if (oZidovi == 0 ):
            print("Nemate vise zidova za postavljanje")
            return
        print("Unesite p ukoliko zelite da postavite plavi zid ili z ukoliko zelite zeleni")
        slovo = input()
        while (slovo != 'p' and slovo != 'z'):
            print("Nevalidan unos, unesite ponovo")
            slovo = input()  
        if (slovo == 'p'):
            print("Plavi zid:")
            plavi()
            oZidovi -= 1
        elif (slovo == 'z'):
            print("Zeleni zid:")
            zeleni()
            oZidovi -= 1 
              
def move():
    global tabla
    global pozicije
    global n
    global m
    global x1
    global x2
    global o1
    global o2
    global cijiPotez
    global moved
    print("Unesite figuru (px1, px2, po1, po2) i smer pomeranja figure (u, d, l, r, ur, ul, dr, dl)")
    try:
        p, where = input().split()   
        while (p not in pozicije): 
                print("Ime figure nije korektno")
                print("Unesite figuru (px1, px2, po1, po2) i smer pomeranja figure (u, d, l, r, ur, ul, dr, dl)")
                p, where = input().split()
        while (cijiPotez not in p): 
                print("Ime figure nije korektno")
                print("Unesite figuru (px1, px2, po1, po2) i smer pomeranja figure (u, d, l, r, ur, ul, dr, dl)")
                p, where = input().split()
        pom=pozicije[p]
        if (where=="u" and  (pom[0]==0 or pom[0]==1 or tabla[pom[0]-3][pom[1]]=="===" or tabla[pom[0]-1][pom[1]]=="===" )):
                print("Nije moguce pomeranje figure u tom smeru, promenite smer kretanja")
        elif(where=="d" and  (pom[0]==n-2 or pom[0]==n-4 or tabla[pom[0]+3][pom[1]]=="===" or tabla[pom[0]+1][pom[1]]=="===" )):
                print("Nije moguce pomeranje figure u tom smeru, promenite smer kretanja")
        elif (where=="l" and  (pom[1]==0 or pom[1]==1 or tabla[pom[0]][pom[1]-3]==" ?? " or tabla[pom[0]][pom[1]-1]==" ?? " )):
                print("Nije moguce pomeranje figure u tom smeru, promenite smer kretanja")
        elif (where=="r" and  (pom[1]==m-2 or pom[1]==m-4 or tabla[pom[0]][pom[1]+3]==" ?? " or tabla[pom[0]][pom[1]+1]==" ?? " )):
                print("Nije moguce pomeranje figure u tom smeru, promenite smer kretanja")
        elif (where=="ur" and  ((pom[0]==0 or pom[0]==1) or (pom[1]==m-2 or pom[1]==m-4) 
                    or (tabla[pom[0]-1][pom[1]]=="===" and tabla[pom[0]-1][pom[1]+2]=="===")
                    or (tabla[pom[0]-2][pom[1]+1]==" ?? " and tabla[pom[0]][pom[1]+1]==" ?? ")
                    or (tabla[pom[0]-1][pom[1]+2]=="===" and tabla[pom[0]-2][pom[1]+1]==" ?? ")
                    or (tabla[pom[0]-1][pom[1]]=="===" and tabla[pom[0]][pom[1]+1]==" ?? ")
                    )):
                print("Nije moguce pomeranje figure u tom smeru, promenite smer kretanja")
        elif (where=="ul" and  ((pom[0]==0 or pom[0]==1) or (pom[1]==0 or pom[1]==1)
                    or (tabla[pom[0]-1][pom[1]-2]=="===" and tabla[pom[0]-1][pom[1]]=="===")
                    or (tabla[pom[0]][pom[1]-1]==" ?? " and tabla[pom[0]-2][pom[1]-1]==" ?? ")
                    or (tabla[pom[0]-1][pom[1]-2]=="===" and tabla[pom[0]-2][pom[1]-1]==" ?? ")
                    or (tabla[pom[0]-1][pom[1]]=="===" and tabla[pom[0]][pom[1]-1]==" ?? "))):
                print("Nije moguce pomeranje figure u tom smeru, promenite smer kretanja")
        elif(where=="dr" and  ((pom[0]==n-2 or pom[0]==n-4 ) or(pom[1]==m-2 or pom[1]==m-4)
                    or (tabla[pom[0]+1][pom[1]]=="===" and tabla[pom[0]+1][pom[1]+2]=="===" )
                    or (tabla[pom[0]][pom[1]+1]==" ?? " and tabla[pom[0]+2][pom[1]+1]==" ?? " )
                    or (tabla[pom[0]+1][pom[1]+2]=="===" and tabla[pom[0]+2][pom[1]+1]==" ?? ")
                    or (tabla[pom[0]+1][pom[1]]=="===" and tabla[pom[0]][pom[1]+1]==" ?? "))):
                print("Nije moguce pomeranje figure u tom smeru, promenite smer kretanja")
        elif(where=="dl" and  ((pom[0]==n-2 or pom[0]==n-4 ) or (pom[1]==0 or pom[1]==1)
                    or (tabla[pom[0]+1][pom[1]]=="===" and tabla[pom[0]+1][pom[1]-2]=="===" )
                    or (tabla[pom[0]][pom[1]-1]==" ?? " and tabla[pom[0]+2][pom[1]-1]==" ?? " )
                    or (tabla[pom[0]+1][pom[1]]=="===" and tabla[pom[0]][pom[1]-1]==" ?? ")
                    or (tabla[pom[0]+1][pom[1]-2]=="===" and tabla[pom[0]+2][pom[1]-1]==" ?? ")
                    )):
                print("Nije moguce pomeranje figure u tom smeru, promenite smer kretanja")
        else:
            moved=True
            Moving(p,where)
    except ValueError:
        print("Nevalidan unos")
        move()
    return 
def Moving(p, where):
    global tabla
    global pozicije
    global n
    global m
    global x1
    global x2
    global o1
    global o2
    global cijiPotez
    pom=pozicije[p]
    lista = []
    lista2 = []
    lista3=[]
    lista3.append([x1[0],x1[1]])
    lista3.append([x2[0],x2[1]])
    lista3.append([o1[0],o1[1]])
    lista3.append([o2[0],o2[1]])
    lista2.append(" O ")
    lista2.append(" X ")
    for key in pozicije.keys():
            lista.append(key)
    if (where=="u"):
        p1=int(pom[0]-4)
        p2=int(pom[0]-2)
        if([p2,pom[1]] in lista3):
            tabla[pom[0]][pom[1]]="   "
            pom[0]-=2  
        elif((tabla[p1][pom[1]] in lista) or (tabla[p2][pom[0]] in lista2)):
            tabla[pom[0]][pom[1]]="   "
            pom[0]-=2
        else:
            tabla[pom[0]][pom[1]]="   "
            pom[0]-=4  
    elif (where=="d"):
        p1=int(pom[0]+4)
        p2=int(pom[0]+2)
        if([p1,pom[1]] in lista3):
            tabla[pom[0]][pom[1]]="   "
            pom[0]+=4
        elif((tabla[p1][pom[1]] in lista) or (tabla[p2][pom[0]] in lista2)):
            tabla[pom[0]][pom[1]]="   "
            pom[0]+=2
        else:
            tabla[pom[0]][pom[1]]="   "
            pom[0]+=4
    elif (where=="l"):
        p1=int(pom[1]-4)
        p2=int(pom[1]-2)
        if([pom[0],p1] in lista3):
            tabla[pom[0]][pom[1]]="   "
            pom[1]-=4
        elif((tabla[pom[0]][p1] in lista) or (tabla[pom[0]][p2] in lista2)):
            tabla[pom[0]][pom[1]]="   "
            pom[1]-=2
        else:
            tabla[pom[0]][pom[1]]="   "
            pom[1]-=4        
    elif (where=="r"):
        p1=int(pom[1]+4)
        p2=int(pom[1]+2)
        if([pom[0],p2] in lista3):
            tabla[pom[0]][pom[1]]="   "
            pom[1]+=2  
        elif((tabla[pom[0]][p1] in lista) or (tabla[pom[0]][p2] in lista2)):
            tabla[pom[0]][pom[1]]="   "
            pom[1]+=2
        else:
            tabla[pom[0]][pom[1]]="   "
            pom[1]+=4  
    elif (where=="ur"):
            tabla[pom[0]][pom[1]]="   "
            pom[0]-=2  
            pom[1]+=2  
    elif (where=="ul"):
            tabla[pom[0]][pom[1]]="   "
            pom[0]-=2  
            pom[1]-=2  
    elif (where=="dr"):
            tabla[pom[0]][pom[1]]="   "
            pom[0]+=2  
            pom[1]+=2  
    elif (where=="dl"):
            tabla[pom[0]][pom[1]]="   "
            pom[0]+=2  
            pom[1]-=2  
    startPos()
    if cijiPotez=="o":
        cijiPotez="x"
    elif  cijiPotez=="x":
        cijiPotez="o"
    return
def update():
    global tabla
    global pozicije
    global x1
    global x2
    global o1
    global o2
    global n
    global m    
    tabla[x1[0]][x1[1]]=" X "
    tabla[x2[0]][x2[1]]=" X "
    tabla[o1[0]][o1[1]]=" O "
    tabla[o2[0]][o2[1]]=" O "
    for key in pozicije.keys():
        pom=pozicije[key]
        tabla[pom[0]][pom[1]]=key
    a = np.array(tabla)
    for line in a:
       print ('  '.join(map(str, line)))
def startPos():
    global tabla
    global x1
    global x2
    global o1
    global o2
    tabla[x1[0]][x1[1]]=" X "
    tabla[x2[0]][x2[1]]=" X "
    tabla[o1[0]][o1[1]]=" O "
    tabla[o2[0]][o2[1]]=" O "
def deleteLast(p):
    global tabla
    global x1
    global x2
    global o1
    global o2
    pom=pozicije[p]
    
    if(tabla[pom[0]][pom[1]] != x1 or tabla[pom[0]][pom[1]] != x2 or tabla[pom[0]][pom[1]] != o1 or tabla[pom[0]][pom[1]] != o2):
        tabla[pom[0]][pom[1]]="  "
    tabla[x1[0]][x1[1]]=" X "
    tabla[x2[0]][x2[1]]=" X "
    tabla[o1[0]][o1[1]]=" O "
    tabla[o2[0]][o2[1]]=" O "
def game():
    global tabla
    global x1
    global x2
    global o1
    global o2
    global pozicije
    global n
    global m
    global xZidovi
    global oZidovi
    global moved
    inputT()
    tabla=Tabla(n,m,x1,x2,o1,o2)
    
    update()
    while (not endGame()):
        print("Korisnik " + cijiPotez +" je na potezu")
        zid()
        update()
        while(not moved):
            move()
        moved=False
        update()
def main():
    game()
    print("Da li zelite da igrate ponovo?")
    p=input()
    while ("da" in p) or ("Da" in p) :
        game()
        print("Da li zelite da igrate ponovo?")
        p=input()

main()


            