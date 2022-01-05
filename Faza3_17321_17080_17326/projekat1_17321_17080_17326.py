import numpy as np
import random
from queue import PriorityQueue
from functools import partial

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
listaStates=list()
tabla1=[]
def Tabla(n, m ,p1,p2,p3,p4):
    tabla = [ [" "  for i in range(m)] for j in range(n) ]
    '''for i in range(n-1):
        for j in range(m-1):
            if(i%2==0 and j%2==0):
                tabla[i][j]="   "
            elif i%2==1 and j%2==1:
                tabla[i][j]="   "
            if i%2==1 and j%2==0:
                tabla[i][j]="___"
            if j%2==1 and i%2==0:
                tabla[i][j]=" | "'''
    for i in range(n-1):
        for j in range(m):
            if(j<m-1):
                if(i%2==0 and j%2==0):
                    tabla[i][j]="   "
                elif i%2==1 and j%2==1:
                    tabla[i][j]="   "
                if i%2==1 and j%2==0:
                    tabla[i][j]="___"
                if j%2==1 and i%2==0:
                    tabla[i][j]=" | "
            else: 
                if(i%2==0):
                    tabla[i][j]= int(i/2)+1
 
    tabla[p1[0]][p1[1]]=" X "
    tabla[p2[0]][p2[1]]=" X "
    tabla[p3[0]][p3[1]]=" O "
    tabla[p4[0]][p4[1]]=" O "
    return tabla

def printT(stanje):
    global n
    global m
    a = np.array(stanje)
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
    while (n%2 == 0 or n<11 or n>22) and n!=0:
        print("Unesite n da bude neparan broj. Ukoliko ne zelite unesite 0")
        n=(int)(input())
        
    if(n == 0):
       n=11
    n=2*n
    print("Unesite m da bude paran broj. Ukoliko ne zelite unesite 0")
    m=(int)(input())
    while (m%2!=0 or m<14 or m>28) and m!=0:
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
    if(x1==(6,6)):
        o1=(6,20)
    else: 
        pom1=int(((n-x1[0])-4))
        pom2=int(((m-x1[1])-4))
        o1=(pom1,pom2)
    if(x2==(14,6)):
        o2=(14,20)
    else: 
        pom3=int(((n-x2[0])-4))
        pom4=int(((m-x2[1])-4))
        o2=(pom3,pom4)
    if(not player1):
        pom=x1
        x1=o1
        o1=pom
        pom=x2
        x2=o2
        o2=pom
    '''if(x2==(14,6) and player1):
        o2=(14,20)
    pom1=int(((n-x1[0])-4))
    pom2=int(((m-x1[1])-4))
    pom3=int(((n-x2[0])-4))
    pom4=int(((m-x2[1])-4))
    if(player1):
        o1=(pom1,pom2)
        o2=(pom3,pom4)
    else:
        x1=(pom1,pom2)
        x2=(pom3,pom4)'''
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
        while (x>=n-1 or y>=m-1 or x <= 0 or y <= 0 or tabla[x-1][y-2] == "===" or tabla[x-1][y] == "===" or tabla[x-2][y-1] == " ǁ " and tabla[x][y-1] == " ǁ "):
            print("Ne mozete tu postaviti zid, unesite neku drugu vrednost za vrstu i kolonu")
            
            x, y = [int(i) for i in input().split()]
            x *= 2
            y *= 2 
            
        tabla[x-1][y-2] = "==="
        tabla[x-1][y] = "==="   
        if(checkWall()==False):
                tabla[x-1][y-2] = "___"
                tabla[x-1][y] = "___"
                print("Ne mozete tu postaviti zid, unesite neku drugu vrednost za vrstu i kolonu")                
                plavi()         
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
        while (x>=n-1 or y>=m-1 or x <= 0 or y <= 0 or tabla[x-1][y-2] == "===" and tabla[x-1][y] == "===" or tabla[x-2][y-1] == " ǁ " or tabla[x][y-1] == " ǁ "):
            print("Ne mozete tu postaviti zid, unesite neku drugu vrednost za vrstu i kolonu")
            
            x, y = [int(i) for i in input().split()]
            x *= 2
            y *= 2   
            
        tabla[x-2][y-1] = " ǁ "
        tabla[x][y-1] = " ǁ "
        
        if(checkWall()==False):
                tabla[x-2][y-1] = " | "
                tabla[x][y-1] = " | "
                print("Ne mozete tu postaviti zid, unesite neku drugu vrednost za vrstu i kolonu")                
                zeleni()       
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
        if (where=="u" and  (pom[0]==0 or pom[0]==2 or pom[0]==1 or tabla[pom[0]-3][pom[1]]=="===" or tabla[pom[0]-1][pom[1]]=="===" )):
                print("Nije moguce pomeranje figure u tom smeru, promenite smer kretanja")
        elif(where=="d" and  (pom[0]==n-2 or pom[0]==n-4 or tabla[pom[0]+3][pom[1]]=="===" or tabla[pom[0]+1][pom[1]]=="===" )):
                print("Nije moguce pomeranje figure u tom smeru, promenite smer kretanja")
        elif (where=="l" and  (pom[1]==0 or pom[1]==2 or pom[1]==2 or tabla[pom[0]][pom[1]-3]==" ǁ " or tabla[pom[0]][pom[1]-1]==" ǁ " )):
                print("Nije moguce pomeranje figure u tom smeru, promenite smer kretanja")
        elif (where=="r" and  (pom[1]==m-2 or pom[1]==m-4 or tabla[pom[0]][pom[1]+3]==" ǁ " or tabla[pom[0]][pom[1]+1]==" ǁ " )):
                print("Nije moguce pomeranje figure u tom smeru, promenite smer kretanja")
        elif (where=="ur" and  ((pom[0]==0) or (pom[1]==m-2 or pom[1]==m-4) 
                    or (tabla[pom[0]-1][pom[1]]=="===" and tabla[pom[0]-1][pom[1]+2]=="===")
                    or (tabla[pom[0]-2][pom[1]+1]==" ǁ " and tabla[pom[0]][pom[1]+1]==" ǁ ")
                    or (tabla[pom[0]-1][pom[1]+2]=="===" and tabla[pom[0]-2][pom[1]+1]==" ǁ ")
                    or (tabla[pom[0]-1][pom[1]]=="===" and tabla[pom[0]][pom[1]+1]==" ǁ ")
                    )):
                print("Nije moguce pomeranje figure u tom smeru, promenite smer kretanja")
        elif (where=="ul" and  ((pom[0]==0 ) or (pom[1]==0 or pom[1]==1)
                    or (tabla[pom[0]-1][pom[1]-2]=="===" and tabla[pom[0]-1][pom[1]]=="===")
                    or (tabla[pom[0]][pom[1]-1]==" ǁ " and tabla[pom[0]-2][pom[1]-1]==" ǁ ")
                    or (tabla[pom[0]-1][pom[1]-2]=="===" and tabla[pom[0]-2][pom[1]-1]==" ǁ ")
                    or (tabla[pom[0]-1][pom[1]]=="===" and tabla[pom[0]][pom[1]-1]==" ǁ "))):
                print("Nije moguce pomeranje figure u tom smeru, promenite smer kretanja")
        elif(where=="dr" and  ((pom[0]==n-2  ) or(pom[1]==m-2 or pom[1]==m-4)
                    or (tabla[pom[0]+1][pom[1]]=="===" and tabla[pom[0]+1][pom[1]+2]=="===" )
                    or (tabla[pom[0]][pom[1]+1]==" ǁ " and tabla[pom[0]+2][pom[1]+1]==" ǁ " )
                    or (tabla[pom[0]+1][pom[1]+2]=="===" and tabla[pom[0]+2][pom[1]+1]==" ǁ ")
                    or (tabla[pom[0]+1][pom[1]]=="===" and tabla[pom[0]][pom[1]+1]==" ǁ "))):
                print("Nije moguce pomeranje figure u tom smeru, promenite smer kretanja")
        elif(where=="dl" and  ((pom[0]==n-2 ) or (pom[1]==0 or pom[1]==1)
                    or (tabla[pom[0]+1][pom[1]]=="===" and tabla[pom[0]+1][pom[1]-2]=="===" )
                    or (tabla[pom[0]][pom[1]-1]==" ǁ " and tabla[pom[0]+2][pom[1]-1]==" ǁ " )
                    or (tabla[pom[0]+1][pom[1]]=="===" and tabla[pom[0]][pom[1]-1]==" ǁ ")
                    or (tabla[pom[0]+1][pom[1]-2]=="===" and tabla[pom[0]+2][pom[1]-1]==" ǁ ")
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
        if([p1,pom[1]] in lista3):
            tabla[pom[0]][pom[1]]="   "
            pom[0]-=4  
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
        if([pom[0],p1] in lista3):
            tabla[pom[0]][pom[1]]="   "
            pom[1]+=4  
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
    niz=[" "  for i in range(m)]
    for j in range(m):
                if(j%2==0):
                    a=str(int(j/2)+1)
                    if(int(a)>=10):
                        niz[j]=" "+a
                    else: niz[j]=" "+a+" "
                else: niz[j]= "   "
    a = np.array(tabla)
    for line in a:
       print ('  '.join(map(str, line)))
    print ('  '.join(map(str, niz)))
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
    lista=nova_stanja(tabla,"x")
    printT(lista[1])
    #statesOfPlayer("x",np.copy(tabla))
    while (not endGame()):
        print("Korisnik " + cijiPotez +" je na potezu")
        #zid()
        #update()
        while(not moved):
            move()
        moved=False
        update()
        zid()
        update()
def main():
    game()
    print("Da li zelite da igrate ponovo?")
    p=input()
    while ("da" in p) or ("Da" in p) :
        game()
        print("Da li zelite da igrate ponovo?")
        p=input()
def findPath(start, end):
    global n
    global m
    def h(x):
        return abs(end[0]-x[0])+abs(end[1]-x[1])
    found_end = False
    open_set = set()
    open_set.add(start)
    pq = PriorityQueue()
    pq.put((0, start))
    closed_set = set()
    g = {}
    prev_nodes = {}
    g[start] = 0
    prev_nodes[start] = None
    
    while len(open_set) > 0 and (not found_end):
        node = pq.get()[1]
        
        if node not in open_set:
            continue
        if node == end:
            found_end = True
            break
        for dx, dy in zip([-2, 2, 0, 0, -2, -2, 2, 2], [0, 0, -2, 2, 2, -2, 2, -2]):
            c = (node[0]+dx, node[1]+dy)
            if c[0] >= 0 and c[1] >= 0 and c[0] <= n-1 and c[1] <= m-1 and isValid(c,open_set,closed_set,dx,dy):
                f = g[node] + 1 + h(c)
                if c not in open_set and c not in closed_set:
                #if(isValid(c,open_set,closed_set)):
                    open_set.add(c)
                    prev_nodes[c] = node
                    g[c] = g[node] + 1
                    pq.put((f,c))
                else:
                    '''prev_nodes[c] = node
                    if c in closed_set:
                        closed_set.remove(c)
                        open_set.add(c)
                    pq.put((f,c))'''
                    #continue
                    if g[c] > g[node] + 1 :
                        g[c] = g[node] + 1
                        prev_nodes[c] = node
                        if c in closed_set:
                                closed_set.remove(c)
                                open_set.add(c)
                        pq.put((f,c))
        open_set.remove(node)
        closed_set.add(node)
    path = []
    if found_end:
        prev = end
        while prev_nodes[prev] is not None:
            path.append(prev)
            prev = prev_nodes[prev]
        path.append(start)
        path.reverse()
    return path
def isValid(c,open_set,closed_set,dx,dy):
        global tabla
        global n
        global m
        #if( c[0]-2<0 or c[0]+2>n-1 or c[1]-2<0 or c[1]+2>m-1 or c[0]-1<0 or c[0]+1>n-1 or c[1]-1<0 or c[1]+1>m-1):
         #   return False
    #if( c not in open_set and c not in closed_set):
        if(( c[0]+1>n-1) and dx==2 and dy==0):
            return False
        else:
            if(tabla[c[0]+1][c[1]]=="===" and dx==-2 and dy==0): #u
                return False
            
        if(( c[1]+1>m-1) and dx==0 and dy==2):
            return False
        else:
            if(tabla[c[0]][c[1]+1]==" ǁ "and dx==0 and dy==-2):#l
                    return False
            
        if(( c[0]-1<0 ) and (dx==-2 and dy==0)):
            return False
        else:
            if(tabla[c[0]-1][c[1]]=="==="and dx==2 and dy==0): #d
                return False
                
        if(( c[1]-1<0 ) and dx==0 and dy==-2):
            return False
        else:
            if ( tabla[c[0]][c[1]-1]==" ǁ " and dx==0 and dy==2): # r
                return False
        if(dx==-2 and dy==2):
            if( c[0]-2<0 or c[0]+2>n-1 or c[1]-2<0 or c[1]+2>m-1 or c[0]-1<0 or c[0]+1>n-1 or c[1]-1<0 or c[1]+1>m-1):
                return False
            else:
                if (dx==-2 and dy==2 and (tabla[c[0]+1][c[1]]=="===" and tabla[c[0]+1][c[1]-2]=="===")
                        or (tabla[c[0]+2][c[1]-1]==" ǁ " and tabla[c[0]][c[1]-1]==" ǁ ")
                        or (tabla[c[0]+1][c[1]-2]=="===" and tabla[c[0]+2][c[1]-1]==" ǁ ")
                        or (tabla[c[0]+1][c[1]]=="===" and tabla[c[0]][c[1]-1]==" ǁ ")): #ur
                        return False   
        if(dx==-2 and dy==-2):        
            if( c[0]-2<0 or c[0]+2>n-1 or c[1]-2<0 or c[1]+2>m-1 or c[0]-1<0 or c[0]+1>n-1 or c[1]-1<0 or c[1]+1>m-1):
                return False
            else:
                if (dx==-2 and dy==-2 and (tabla[c[0]+1][c[1]+2]=="===" and tabla[c[0]+1][c[1]]=="===")
                            or (tabla[c[0]][c[1]+1]==" ǁ " and tabla[c[0]+2][c[1]+1]==" ǁ ")
                            or (tabla[c[0]+1][c[1]+2]=="===" and tabla[c[0]+2][c[1]+1]==" ǁ ")
                            or (tabla[c[0]+1][c[1]]=="===" and tabla[c[0]][c[1]+1]==" ǁ ")): # ul
                            return False
        if(dx==+2 and dy==+2):
            if( c[0]-2<0 or c[0]+2>n-1 or c[1]-2<0 or c[1]+2>m-1 or c[0]-1<0 or c[0]+1>n-1 or c[1]-1<0 or c[1]+1>m-1):
                return False
            else:
                if (dx==+2 and dy==+2 and (tabla[c[0]-1][c[1]]=="===" and tabla[c[0]-1][c[1]-2]=="===" )
                        or (tabla[c[0]][c[1]-1]==" ǁ " and tabla[c[0]-2][c[1]-1]==" ǁ " )
                        or (tabla[c[0]-1][c[1]-2]=="===" and tabla[c[0]-2][c[1]-1]==" ǁ ")
                        or (tabla[c[0]-1][c[1]]=="===" and tabla[c[0]][c[1]-1]==" ǁ ")): # dr
                        return False
        if(dx==+2 and dy==-2):
            if( c[0]-2<0 or c[0]+2>n-1 or c[1]-2<0 or c[1]+2>m-1 or c[0]-1<0 or c[0]+1>n-1 or c[1]-1<0 or c[1]+1>m-1):
                return False
            else:
                    if (dx==+2 and dy==-2 and (tabla[c[0]-1][c[1]]=="===" and tabla[c[0]+1][c[1]-2]=="===" )
                            or (tabla[c[0]][c[1]+1]==" ǁ " and tabla[c[0]-2][c[1]+1]==" ǁ " )
                            or (tabla[c[0]-1][c[1]]=="===" and tabla[c[0]][c[1]+1]==" ǁ ")
                            or (tabla[c[0]-1][c[1]+2]=="===" and tabla[c[0]-2][c[1]+1]==" ǁ ")): # dl
                            return False    
        return True
def checkWall():
    global pozicije
    global x1
    global x2
    global o1
    global o2
    pom=True
    lista=[]
    for key in pozicije.keys():
            lista.append(key)
    for l in lista:
        if(findPath((pozicije[l][0],pozicije[l][1]),x1)==[]):         
            return False
        if(findPath((pozicije[l][0],pozicije[l][1]),x2)==[]):
            return False
        if(findPath((pozicije[l][0],pozicije[l][1]),o1)==[]):
            return False
        if(findPath((pozicije[l][0],pozicije[l][1]),o2)==[]):
            return False
    return True
def statesOfPlayer(koIgra,stanje):
    if(koIgra=="x"):
        states('px2',stanje)
        states('px1',stanje)
        #print(len(listaStates))
        update()
    else: 
        states('po1',stanje)
        states('po2',stanje)
        #print(len(listaStates))
def states(koIgra,stanje):
    global xZidovi
    global oZidovi
    zidovi=0
    if(koIgra=='px1' or koIgra=='px2'):
        zidovi=xZidovi
    else: zidovi=oZidovi
    pom=[]
    for i in range(n-1):
        for j in range(m-1):
            if(i%2==0 and j%2==0):
               if(stanje[i][j]==koIgra):
                  pom=[i,j]
    global listaStates
    if(pom[0]!=0 and pom[0]!=2 and pom[0]!=1 and stanje[pom[0]-3][pom[1]]!="===" and stanje[pom[0]-1][pom[1]]!="===" ): #u
        potez="u" #koji je potez
        if(zidovi>0):
            zidStates(potez,koIgra,stanje)
        else: 
            listaStates.append(makeNewState(koIgra,[0,0],"",potez,stanje))
    if(pom[0]!=n-2 and pom[0]!=n-4 and stanje[pom[0]+3][pom[1]]!="===" and stanje[pom[0]+1][pom[1]]!="===" ): #d
        potez="d"
        if(zidovi>0):
            zidStates(potez,koIgra,stanje)
        else: listaStates.append(makeNewState(koIgra,[0,0],"",potez,stanje))
    if(pom[1]!=0 and pom[1]!=2 and pom[1]!=1 and stanje[pom[0]][pom[1]-3]!=" ǁ " and stanje[pom[0]][pom[1]-1]!=" ǁ " ): #l
        potez="l"
        if(zidovi>0):
            zidStates(potez,koIgra,stanje)
        else: listaStates.append(makeNewState(koIgra,[0,0],"",potez,stanje))
    if(pom[1]!=m-2 and pom[1]!=m-4 and stanje[pom[0]][pom[1]+3]!=" ǁ " and stanje[pom[0]][pom[1]+1]!=" ǁ " ): #r
        potez="r"
        if(zidovi>0):
            zidStates(potez,koIgra,stanje)
        else: listaStates.append(makeNewState(koIgra,[0,0],"",potez,stanje))
    if((pom[0]!=0) and (pom[1]!=m-2 and pom[1]!=m-4) 
                    and (stanje[pom[0]-1][pom[1]]!="===" or stanje[pom[0]-1][pom[1]+2]!="===")
                    and (stanje[pom[0]-2][pom[1]+1]!=" ǁ " or stanje[pom[0]][pom[1]+1]!=" ǁ ")
                    and (stanje[pom[0]-1][pom[1]+2]!="===" or stanje[pom[0]-2][pom[1]+1]!=" ǁ ")
                    and (stanje[pom[0]-1][pom[1]]!="===" or stanje[pom[0]][pom[1]+1]!=" ǁ ")): #ur
        potez="ur"
        if(zidovi>0):
            zidStates(potez,koIgra,stanje)
        else: listaStates.append(makeNewState(koIgra,[0,0],"",potez,stanje))
    if((pom[0]!=0) and (pom[1]!=0 and pom[1]!=1)
                    and (stanje[pom[0]-1][pom[1]-2]!="===" or stanje[pom[0]-1][pom[1]]!="===")
                    and (stanje[pom[0]][pom[1]-1]!=" ǁ " or stanje[pom[0]-2][pom[1]-1]!=" ǁ ")
                    and (stanje[pom[0]-1][pom[1]-2]!="===" or stanje[pom[0]-2][pom[1]-1]!=" ǁ ")
                    and (stanje[pom[0]-1][pom[1]]!="===" or stanje[pom[0]][pom[1]-1]!=" ǁ ")): #ul
        potez="ul"
        if(zidovi>0):
            zidStates(potez,koIgra,stanje)
        else: listaStates.append(makeNewState(koIgra,[0,0],"",potez,stanje))
    if((pom[0]!=n-2) and(pom[1]!=m-2 and pom[1]!=m-4)
                    and (stanje[pom[0]+1][pom[1]]!="===" or stanje[pom[0]+1][pom[1]+2]!="===" )
                    and (stanje[pom[0]][pom[1]+1]!=" ǁ " or stanje[pom[0]+2][pom[1]+1]!=" ǁ " )
                    and (stanje[pom[0]+1][pom[1]+2]!="===" or stanje[pom[0]+2][pom[1]+1]!=" ǁ ")
                    and (stanje[pom[0]+1][pom[1]]!="===" or stanje[pom[0]][pom[1]+1]!=" ǁ ")): #dr
        potez="dr"
        if(zidovi>0):
            zidStates(potez,koIgra,stanje)
        else: listaStates.append(makeNewState(koIgra,[0,0],"",potez,stanje))
    if((pom[0]!=n-2) and (pom[1]!=0 and pom[1]!=1)
                    and (stanje[pom[0]+1][pom[1]]!="===" or stanje[pom[0]+1][pom[1]-2]!="===" )
                    and (stanje[pom[0]][pom[1]-1]!=" ǁ " or stanje[pom[0]+2][pom[1]-1]!=" ǁ " )
                    and (stanje[pom[0]+1][pom[1]]!="===" or stanje[pom[0]][pom[1]-1]!=" ǁ ")
                    and (stanje[pom[0]+1][pom[1]-2]!="===" or stanje[pom[0]+2][pom[1]-1]!=" ǁ ")): #dl
        potez="dl"
        if(zidovi>0):
            zidStates(potez,koIgra,stanje) 
        else: listaStates.append(makeNewState(koIgra,[0,0],"",potez,stanje))
    return len(listaStates)
def zidStates(potez,koIgra,stanje):
    
    global n
    global m 
    global pozicije
    global listaStates
    p=[]
    z=[]
    for i in range(n-2):
        for j in range(m-2):
            if i%2==1 and j%2==0:
                if(i<n-1 and j<m-1 and stanje[i][j+2] != "===" and stanje[i][j] != "===" and stanje[i-1][j+1] != " ǁ " or stanje[i+1][j+1] != " ǁ "):
                    p=[i,j]
                    copy=np.copy(stanje)
                    stanje[i][j+2] = "==="   
                    stanje[i][j] = "===" 
                    if(checkWall()):
                        listaStates.append(makeNewState(koIgra,p,"plavi",potez,stanje))
                    stanje=copy
            if j%2==1 and i%2==0:
                if(i<n-1 and j<m-1  and stanje[i+2][j] != "===" or stanje[i][j] != "===" and stanje[i+1][j-1] != " ǁ " and stanje[i+1][j+1] != " ǁ "):
                    z=[i,j]
                    copy=np.copy(stanje)
                    stanje[i+2][j] = " ǁ " 
                    stanje[i][j] = " ǁ "
                    if(checkWall()):
                        listaStates.append(makeNewState(koIgra,z,"zeleni",potez,stanje))
                    stanje=copy
def makeNewState(koIgra,zid,vrstaZida,potez,stanje):
    global pozicije
    global x1
    global x2
    global o1
    global o2
    pom=[]
    for i in range(n-1):
        for j in range(m-1):
            if(i%2==0 and j%2==0):
               if(stanje[i][j]==koIgra):
                  pom=[i,j]
    ispis=koIgra
    tablaDup=np.copy(stanje)
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
    if (potez=="u"):
        p1=int(pom[0]-4) 
        p2=int(pom[0]-2) 
        if([p1,pom[1]] in lista3):
            tablaDup[pom[0]][pom[1]]="   "
            tablaDup[pom[0]-4][pom[1]]=ispis
        elif((tablaDup[p1][pom[1]] in lista) or (tablaDup[p2][pom[0]] in lista2)):
            tablaDup[pom[0]][pom[1]]="   "
            tablaDup[pom[0]-2][pom[1]]=ispis
        else:
            tablaDup[pom[0]][pom[1]]="   "
            tablaDup[pom[0]-4][pom[1]]=ispis
    elif (potez=="d"):
        p1=int(pom[0]+4)
        p2=int(pom[0]+2)
        if([p1,pom[1]] in lista3):
            tablaDup[pom[0]][pom[1]]="   "
            tablaDup[pom[0]+4][pom[1]]=ispis
        elif((tablaDup[p1][pom[1]] in lista) or (tablaDup[p2][pom[0]] in lista2)):
            tablaDup[pom[0]][pom[1]]="   "
            tablaDup[pom[0]+2][pom[1]]=ispis
        else:
            tablaDup[pom[0]][pom[1]]="   "
            tablaDup[pom[0]+4][pom[1]]=ispis
    elif (potez=="l"):
        p1=int(pom[1]-4)
        p2=int(pom[1]-2)
        if([pom[0],p1] in lista3):
            tablaDup[pom[0]][pom[1]]="   "
            tablaDup[pom[0]][pom[1]-4]=ispis
        elif((tablaDup[pom[0]][p1] in lista) or (tablaDup[pom[0]][p2] in lista2)):
            tablaDup[pom[0]][pom[1]]="   "
            tablaDup[pom[0]][pom[1]-2]=ispis
        else:
            tablaDup[pom[0]][pom[1]]="   "
            tablaDup[pom[0]][pom[1]-4]=ispis     
    elif (potez=="r"):
        p1=int(pom[1]+4)
        p2=int(pom[1]+2)
        if([pom[0],p1] in lista3):
            tablaDup[pom[0]][pom[1]]="   "
            tablaDup[pom[0]][pom[1]+4]=ispis
        elif((tablaDup[pom[0]][p1] in lista) or (tablaDup[pom[0]][p2] in lista2)):
            tabla[pom[0]][pom[1]]="   "
            tablaDup[pom[0]][pom[1]+2]=ispis
        else:
            tablaDup[pom[0]][pom[1]]="   "
            tablaDup[pom[0]][pom[1]+4]=ispis
    elif (potez=="ur"):
            tablaDup[pom[0]][pom[1]]="   "
            tablaDup[pom[0]-2][pom[1]+2]=ispis
    elif (potez=="ul"):
            tablaDup[pom[0]][pom[1]]="   "
            tablaDup[pom[0]-2][pom[1]-2]=ispis
    elif (potez=="dr"):
            tablaDup[pom[0]][pom[1]]="   "
            tablaDup[pom[0]+2][pom[1]+2]=ispis
    elif (potez=="dl"):
            tablaDup[pom[0]][pom[1]]="   "
            tablaDup[pom[0]+2][pom[1]-2]=ispis
    if(vrstaZida=="plavi"):
        tablaDup[zid[0]][zid[1]+2] = "==="  
        tablaDup[zid[0]][zid[1]] = "===" 
    else:
        if(vrstaZida=="zeleni"):
            tablaDup[zid[0]+2][zid[1]] = " ǁ "  
            tablaDup[zid[0]][zid[1]] = " ǁ "
    if(ispis=="px1"):
        tablaDup[x1[0]][x1[1]]=" X "
    else: 
        if(ispis=="px2"):
             tablaDup[x2[0]][x2[1]]=" X "
        else:
            if(ispis=="po1"):
                tablaDup[o1[0]][o1[1]]=" O "
            else: tablaDup[o2[0]][o2[1]]=" O "
    #listaStates.append(tablaDup) 
    return tablaDup
    #sva sledeca stanja se cuvaju u globalnoj promeljivoj listaStates
    #ukoliko se ona koristi mora da se ociste rpethodna stanja tj lista pre racunanja ostalih stanja inc ce da ostane u promenljivoj!!!!!!!!!
    #moze da se prebaci u dictionary za px1 i px2 npr
    #ili da se prebaci u return da se vraca lista umesto da se cuva u globalnoj promenljivoj   
def minimax(stanje,dubina,moj_potez, potez=None,alpha=(), beta=()):
    #def minimax(stanje,dubina,moj_potez: -lBodsecanje gde je A pocetno stanje
    #napise poziv fje sa primenom max_value i min_value uemsto max_stanje..alpha = (A, 0),beta = (A, 10)
    #alfa je najbolja vrednost za igraca max a beta je najbolja vrednost za igraca min 
    '''oceni- heuristika
    kraj-ispituje jek je kraj igre?
    full-puna tabla
    igraj- odigravanje potez'''
    if kraj(stanje):
        return (potez, kraj(stanje))
    if (player1):
        igrac = "o" if moj_potez else "x"
    else: 
        igrac = "x" if moj_potez else "o"
    fja = max_value(stanje,dubina,alpha,beta) if moj_potez else min_value(stanje,dubina,alpha,beta)
    lp = nova_stanja(stanje,igrac)
    if dubina == 0:
        return (potez, proceni_stanje(stanje))
    if lp is None or len(lp) == 0:
        return (potez, proceni_stanje(stanje))
    return fja([minimax(x, dubina - 1, not moj_potez, x if potez is None else potez,alfa=(x,proceni_stanje(x)),beta=(x,proceni_stanje(x))) for x in lp])
    #lp = nova_stanja(stanje)
    #fja = max_stanje if moj_potez else min_stanje
    #if dubina == 0 or lp is None:
        #return (stanje, proceni_stanje(stanje))
    #return fja([minimax(x, dubina - 1, not moj_potez) for x in lp])
def nova_stanja(stanje,igrac):#u koja se sve stanja moze preci iz zadatog stanja (fja promene stanja)
    statesOfPlayer(igrac,stanje)
    copy=np.copy(listaStates)
    listaStates.clear()
    return copy
def proceni_stanje(stanje): #koliko konkretno stanje vodi igraca ka pobedi
    global tabla1

    tabla1[x1[0]][x1[1]]=" X "
    tabla1[x2[0]][x2[1]]=" X "
    tabla1[o1[0]][o1[1]]=" O "
    tabla1[o2[0]][o2[1]]=" O "
    for key in pozicije.keys():
        pom=pozicije[key]
        tabla1[pom[0]][pom[1]]=key
    niz=[" "  for i in range(m)]
    for j in range(m):
                if(j%2==0):
                    a=str(int(j/2)+1)
                    if(int(a)>=10):
                        niz[j]=" "+a
                    else: niz[j]=" "+a+" "
                else: niz[j]= "   "
    p=pozicije["px1"]
    tabla1[p[0]][p[1]]="   "
    tabla1[p[0]-4][p[1]]="px1"
    tabla1[x1[0]][x1[1]]=" X "
    
    tabla1[0][1]=" ǁ "
    tabla1[2][1]=" ǁ "
    a = np.array(tabla1)
    for line in a:
       print ('  '.join(map(str, line)))
    print ('  '.join(map(str, niz)))
    for i in range(n-1):
      for j in range(m-1):
         if (stanje[i][j] != tabla1[i][j]):
            return 616
    
    return 0
'''def max_stanje(lsv):#odredjuje koje stanje ima najvecu vrednost fje procene za zadatu listu stanja 
       #bez lBodsecanje
    return max(lsv,key=lambda x:x[1])
def min_stanje(lsv):    #bez lBodsecanje
    return min(lsv,key=lambda x:x[1])'''
def max_value(stanje, dubina, alpha, beta):   #lBodsecanje
    if dubina == 0:#jer dubnu smanjujemo svaki sledeci put
        return (stanje, proceni_stanje(stanje))#vracamo tuple sa stanjem i njegovom vrednosti
    else:
        for s in nova_stanja(stanje):#odredjujemo sva nova stanja i prolazimo kroz njih
            alpha = max(alpha, min_value(s, dubina - 1, alpha, beta), key=lambda x: x[1])
            #odredjujemo alfa, kao maksimum izmedju alfa i minimalne vrednosti, vracamo kljuc cija je vrednost 1 jer vrsimo proveru po proceni ne po stanju
            if alpha[1] >= beta[1]:
                return beta
    return alpha
def min_value(stanje, dubina, alpha, beta):
    if dubina == 0:
        return (stanje, proceni_stanje(stanje))   #lBodsecanje
    else:
        for s in nova_stanja(stanje):
            beta = min(beta, max_value(s, dubina - 1, alpha, beta),key=lambda x: x[1])
            if beta[1] <= alpha[1]:
                return alpha
    return beta    
def kraj(stanje):
    ppx1=[]
    ppx2=[]
    ppo1=[]
    ppo2=[]
    for i in range(n-1):
        for j in range(m-1):
            if( stanje[i][j]=="px1"):
                ppx1=[i,j]
            if( stanje[i][j]=="px2"):
                ppx2=[i,j]
            if( stanje[i][j]=="po1"):
                ppo1=[i,j]
            if( stanje[i][j]=="po2"):
                ppo2=[i,j]
    px1i=[x1[0],x1[1]]
    px2i=[x2[0],x2[1]]
    po1i=[o1[0],o1[1]]
    po2i=[o2[0],o2[1]]
    if (ppx1==po1i or ppx1==po2i or ppx2==po1i or ppx2==po2i ):
        return 0
    if (ppo1==px1i or ppo1==px2i or ppo2==px1i or ppo2==px2i ):
        return 0
    return proceni_stanje(stanje)
def igraj():
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
    while (not endGame()):
        if(player1):
            #while(kraj(tabla)==0):
            rez=minimax(tabla,3,"x",(tabla, 0),(tabla, 617))
            naj=rez[0]
            tabla=naj
            update()
            if cijiPotez=="o":
                cijiPotez="x"
            elif  cijiPotez=="x":
                cijiPotez="o"
            while(not moved):
                move()
            moved=False
            update()
            zid()
            update()
        else:
            while(not moved):
                move()
                moved=False 
                update()
                zid()
                update()
            
            rez=minimax(tabla,3,"x",(tabla, 0),(tabla, 617))
            naj=rez[0]
            tabla=naj
            update()
            if cijiPotez=="o":
                cijiPotez="x"
            elif  cijiPotez=="x":
                cijiPotez="o"

n=22
m=28
'''inputT()
tabla=Tabla(n,m,x1,x2,o1,o2)
tabla1=np.copy(tabla)
print()
update()'''
#print(minimax(tabla,3,"x",(tabla, 0),(tabla, 617)))
#print(proceni_stanje(tabla))
#print(minimax(np.copy(tabla),1,"x",(np.copy(tabla), 0),(np.copy(tabla), 617))[0])
#tabla=np.copy(minimax(tabla,3,"x",(tabla, 0),(tabla, 617))[0])
#print(x1)
#update()
'''
tabla[7][6] = "==="
tabla[5][6] = "==="
tabla[6][5] = " ǁ "
tabla[13][6] = "==="
tabla[4][17] = " ǁ "
tabla[6][17] = " ǁ "
tabla[6][7] = " ǁ "
print(findPath((8,22),(16,8)))

update()'''
#checkWall()
#print(tabla[6][4])
#print(findPath((8, 4), (8, 16)))

main()











 


            