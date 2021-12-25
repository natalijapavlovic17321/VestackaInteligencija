def a_star(p,k):
    return True
def statesOfPlayer(koIgra):
    if(koIgra==" X "):
        states('px2')
        print(len(listaStates))
        states('px1')
        #print(states('px2'))
        #print(states('px1'))
        print(len(listaStates))
        update()
    else: print(states('po1')+states('po2'))
def states(koIgra):
    global xZidovi
    global oZidovi
    zidovi=0
    if(koIgra=='px1' or koIgra=='px2'):
        zidovi=xZidovi
    else: zidovi=oZidovi
    global pozicije
    pom=pozicije[koIgra]
    global tabla
    global listaStates
    if(pom[0]!=0 and pom[0]!=2 and pom[0]!=1 and tabla[pom[0]-3][pom[1]]!="===" and tabla[pom[0]-1][pom[1]]!="===" ): #u
        potez="u" #koji je potez
        if(zidovi>0):
            zidStates(potez,koIgra)
        else: 
            listaStates.append(makeNewState(koIgra,[0,0],"",potez))
    if(pom[0]!=n-2 and pom[0]!=n-4 and tabla[pom[0]+3][pom[1]]!="===" and tabla[pom[0]+1][pom[1]]!="===" ): #d
        potez="d"
        if(zidovi>0):
            zidStates(potez,koIgra)
        else: listaStates.append(makeNewState(koIgra,[0,0],"",potez))
    if(pom[1]!=0 and pom[1]!=2 and pom[1]!=1 and tabla[pom[0]][pom[1]-3]!=" ǁ " and tabla[pom[0]][pom[1]-1]!=" ǁ " ): #l
        potez="l"
        if(zidovi>0):
            zidStates(potez,koIgra)
        else: listaStates.append(makeNewState(koIgra,[0,0],"",potez))
    if(pom[1]!=m-2 and pom[1]!=m-4 and tabla[pom[0]][pom[1]+3]!=" ǁ " and tabla[pom[0]][pom[1]+1]!=" ǁ " ): #r
        potez="r"
        if(zidovi>0):
            zidStates(potez,koIgra)
        else: listaStates.append(makeNewState(koIgra,[0,0],"",potez))
    if((pom[0]!=0) and (pom[1]!=m-2 and pom[1]!=m-4) 
                    and (tabla[pom[0]-1][pom[1]]!="===" or tabla[pom[0]-1][pom[1]+2]!="===")
                    and (tabla[pom[0]-2][pom[1]+1]!=" ǁ " or tabla[pom[0]][pom[1]+1]!=" ǁ ")
                    and (tabla[pom[0]-1][pom[1]+2]!="===" or tabla[pom[0]-2][pom[1]+1]!=" ǁ ")
                    and (tabla[pom[0]-1][pom[1]]!="===" or tabla[pom[0]][pom[1]+1]!=" ǁ ")): #ur
        potez="ur"
        if(zidovi>0):
            zidStates(potez,koIgra)
        else: listaStates.append(makeNewState(koIgra,[0,0],"",potez))
    if((pom[0]!=0) and (pom[1]!=0 and pom[1]!=1)
                    and (tabla[pom[0]-1][pom[1]-2]!="===" or tabla[pom[0]-1][pom[1]]!="===")
                    and (tabla[pom[0]][pom[1]-1]!=" ǁ " or tabla[pom[0]-2][pom[1]-1]!=" ǁ ")
                    and (tabla[pom[0]-1][pom[1]-2]!="===" or tabla[pom[0]-2][pom[1]-1]!=" ǁ ")
                    and (tabla[pom[0]-1][pom[1]]!="===" or tabla[pom[0]][pom[1]-1]!=" ǁ ")): #ul
        potez="ul"
        if(zidovi>0):
            zidStates(potez,koIgra)
        else: listaStates.append(makeNewState(koIgra,[0,0],"",potez))
    if((pom[0]!=n-2) and(pom[1]!=m-2 and pom[1]!=m-4)
                    and (tabla[pom[0]+1][pom[1]]!="===" or tabla[pom[0]+1][pom[1]+2]!="===" )
                    and (tabla[pom[0]][pom[1]+1]!=" ǁ " or tabla[pom[0]+2][pom[1]+1]!=" ǁ " )
                    and (tabla[pom[0]+1][pom[1]+2]!="===" or tabla[pom[0]+2][pom[1]+1]!=" ǁ ")
                    and (tabla[pom[0]+1][pom[1]]!="===" or tabla[pom[0]][pom[1]+1]!=" ǁ ")): #dr
        potez="dr"
        if(zidovi>0):
            zidStates(potez,koIgra)
        else: listaStates.append(makeNewState(koIgra,[0,0],"",potez))
    if((pom[0]!=n-2) and (pom[1]!=0 and pom[1]!=1)
                    and (tabla[pom[0]+1][pom[1]]!="===" or tabla[pom[0]+1][pom[1]-2]!="===" )
                    and (tabla[pom[0]][pom[1]-1]!=" ǁ " or tabla[pom[0]+2][pom[1]-1]!=" ǁ " )
                    and (tabla[pom[0]+1][pom[1]]!="===" or tabla[pom[0]][pom[1]-1]!=" ǁ ")
                    and (tabla[pom[0]+1][pom[1]-2]!="===" or tabla[pom[0]+2][pom[1]-1]!=" ǁ ")): #dl
        potez="dl"
        if(zidovi>0):
            zidStates(potez,koIgra) 
        else: listaStates.append(makeNewState(koIgra,[0,0],"",potez))
    return len(listaStates)
def zidStates(potez,koIgra):
    global tabla
    global n
    global m 
    global pozicije
    global listaStates
    p=[]
    z=[]
    for i in range(n-2):
        for j in range(m-2):
            if i%2==1 and j%2==0:
                if(i<n-1 and j<m-1 and i > 0 and j > 0 and tabla[i-1][j-2] != "===" and tabla[i-1][j] != "===" and tabla[i-2][j-1] != " ǁ " or tabla[i][j-1] != " ǁ "):
                    p=[i,j]
                    if(True):
                        makeNewState(koIgra,p,"plavi",potez)
            if j%2==1 and i%2==0:
                if(i<n-1 and j<m-1 and i > 0 and j > 0 and tabla[i-1][j-2] != "===" or tabla[i-1][j] != "===" and tabla[i-2][j-1] != " ǁ " and tabla[i][j-1] != " ǁ "):
                    z=[i,j]
                    if(a_star(pozicije['px1'],o1) and a_star(pozicije['px1'],o2) and a_star(pozicije['px2'],o1) and a_star(pozicije['px2'],o1)
                    and a_star(pozicije['po1'],x1) and a_star(pozicije['po1'],x2) and a_star(pozicije['po2'],x1) and a_star(pozicije['po2'],x2)):
                        makeNewState(koIgra,z,"zeleni",potez)
def makeNewState(koIgra,zid,vrstaZida,potez):
    global pozicije
    global x1
    global x2
    global o1
    global o2
    pom=pozicije[koIgra]
    ispis=""
    tablaDup = [ [" "  for i in range(m)] for j in range(n) ]
    for i in range (n-1):
        for j in range(m):
            tablaDup[i][j]=tabla[i][j]
    #tablaDup=tabla #novo stanje
    if(koIgra=='px1' or koIgra=='px2'):
        ispis=" X "
    else: ispis=" O "
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
        tablaDup[zid[0]][zid[1]-2] = "==="
        tablaDup[zid[0]][zid[1]] = "===" 
    else:
        if(vrstaZida=="zeleni"):
            tablaDup[zid[0]-2][zid[1]] = " ǁ "
            tablaDup[zid[0]][zid[1]] = " ǁ "
    listaStates.append(tablaDup)
    return tablaDup
