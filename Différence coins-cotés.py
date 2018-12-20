# -*- coding: utf-8 -*-
"""
Created on Mon May 18 13:35:56 2015

@author: Jean
"""
""" Différence coins/cotés """

import numpy as np
import numpy.random as rd


def sallalea(cote1,cote2):
    l=[]
    for i in range(cote1):
        for j in range(cote2):
            l+=[[i,j]]
    rd.shuffle(l)
    return l

def un(x):
    if x==0:
        return 0
    else:
        return 1

def agglutinement(direction,piece,i,j, probabilite):
    c=0
    e=rd.random()
    if direction==12:
        c=un(piece[i-1][j-1])+un(piece[i][j-1])+un(piece[i-1][j+1])+un(piece[i][j+1])
    elif direction==6:
        c=un(piece[i+1][j-1])+un(piece[i][j-1])+un(piece[i+1][j+1])+un(piece[i][j+1])
    elif direction==3:
        c=un(piece[i-1][j])+un(piece[i-1][j+1])+un(piece[i+1][j+1])+un(piece[i+1][j])
    elif direction==9:
        c=un(piece[i-1][j-1])+un(piece[i-1][j])+un(piece[i+1][j])+un(piece[i+1][j-1])
    elif direction==1:
        c=un(piece[i-1][j])+un(piece[i-1][j-1])+un(piece[i][j+1])+un(piece[i+1][j+1])
    elif direction==5:
        c=un(piece[i-1][j+1])+un(piece[i][j+1])+un(piece[i+1][j])+un(piece[i+1][j-1])
    elif direction==7:
        c=un(piece[i+1][j+1])+un(piece[i+1][j])+un(piece[i][j-1])+un(piece[i-1][j-1])
    elif direction==11:
        c=un(piece[i+1][j-1])+un(piece[i][j-1])+un(piece[i-1][j])+un(piece[i-1][j+1]) 
    if e<probabilite[c]:
        return True
    else: 
        return False
                
        
def matnul(n,p):
    c=[]
    for i in range(n):
        c+=[[]]
        for k in range(p):
            c[i]+=[0]
    return c    
      
def construction(Npersonnes,cote1,cote2,listeporte):
    piece=matnul(cote1,cote2)
    total=0
    for i in range(cote1):
        for j in range(cote2):
            if i in [0,cote1-1] or j in [0,cote2-1]:
                 piece[i][j]=2
    for e in range(len(listeporte)):
        [i,j]=listeporte[e]
        piece[i][j]=3
    while total<Npersonnes:
        i=rd.randint(1,(cote1-1))
        j=rd.randint(1,(cote2-1))
        if piece[i][j]==0:
            piece[i][j]=1
            total+=1
    return piece

def listemin(l):
    c,e=[],[]
    if l==[]:
        return []
    else:
     for i in range(len(l)):
         c+=[l[i][0]]
     d=min(c)
     for j in range(len(l)):
        if l[j][0]==d:
            e+=[l[j][1]]
    return e

def distance(piece,listporte,i,j):
       d=[]
       casel,hautl,basl,droitel,gauchel,hautgauchel,hautdroitl,basdroitl,basgauchel=[],[],[],[],[],[],[],[],[]
       for e in range(len(listporte)):         
           casel       += [ np.sqrt(((i-listporte[e][0])**2)   + ((j-listporte[e][1])**2))  ]
           hautl       += [ np.sqrt(((i-listporte[e][0]-1)**2) + ((j-listporte[e][1])**2))  ]
           basl        += [ np.sqrt(((i-listporte[e][0]+1)**2) + ((j-listporte[e][1])**2))  ]
           droitel     += [ np.sqrt(((i-listporte[e][0])**2)   + ((j-listporte[e][1]+1)**2))]
           gauchel     += [ np.sqrt(((i-listporte[e][0])**2)   + ((j-listporte[e][1]-1)**2))]
           hautgauchel += [ np.sqrt(((i-listporte[e][0]-1)**2) + ((j-listporte[e][1]-1)**2))]
           hautdroitl  += [ np.sqrt(((i-listporte[e][0]-1)**2) + ((j-listporte[e][1]+1)**2))]
           basdroitl   += [ np.sqrt(((i-listporte[e][0]+1)**2) + ((j-listporte[e][1]+1)**2))]
           basgauchel  += [ np.sqrt(((i-listporte[e][0]+1)**2) + ((j-listporte[e][1]-1)**2))]
       case,haut,bas,droite,gauche,hautgauche,hautdroit,basdroit,basgauche=min(casel),min(hautl),min(basl),min(droitel),min(gauchel),min(hautgauchel),min(hautdroitl),min(basdroitl),min(basgauchel) 
       if piece[i-1][j]==0 and haut<=case:
           d.append([haut,12])
       if piece[i+1][j]==0 and bas<=case:
           d.append([bas,6])
       if piece[i][j+1]==0 and droite<=case:
           d.append([droite,3])
       if piece[i][j-1]==0 and gauche<=case:
           d.append([gauche,9])
       if piece[i-1][j-1]==0 and hautgauche<=case:
           d.append([hautgauche,11])
       if piece[i+1][j-1]==0 and basgauche<=case:
           d.append([basgauche,7])
       if piece[i-1][j+1]==0 and hautdroit<=case:
           d.append([hautdroit,1])
       if piece[i+1][j+1]==0 and basdroit<=case:
           d.append([basdroit,5])
       l=listemin(d)
       return l

       
def proche_porte(listeporte,i,j):
    for k in [i-1,i,i+1]:
        for l in [j-1,j,j+1]:
            if [k,l] in listeporte:
               return True
    return False


def evacuation(Npersonnes,cote1,cote2,listeporte,probabilite):
    piece=construction(Npersonnes,cote1,cote2,listeporte)
    total=Npersonnes
    compte=0
    while total>0:
      print piece
      print ''
      for [i,j] in sallalea(cote1,cote2):          
            if piece[i][j]==1:
                if proche_porte(listeporte,i,j): 
                    piece[i][j]=0
                    total-=1
                else:
                    l=distance(piece,listeporte,i,j)
                    if l==[]:
                      piece[i][j]=1
                    else:
                      a=rd.randint(0,len(l))
                      if l[a]==12 and agglutinement(12,piece,i,j,probabilite): 
                          piece[i-1][j]=5
                          piece[i][j]=0
                      elif l[a]==6 and agglutinement(6,piece,i,j,probabilite):
                          piece[i+1][j]=5
                          piece[i][j]=0
                      elif l[a]==3 and agglutinement(3,piece,i,j,probabilite):
                          piece[i][j+1]=5
                          piece[i][j]=0
                      elif l[a]==9 and agglutinement(9,piece,i,j,probabilite): 
                          piece[i][j-1]=5
                          piece[i][j]=0
                      elif l[a]==1 and agglutinement(1,piece,i,j,probabilite):
                          piece[i-1][j+1]=5
                          piece[i][j]=0
                      elif l[a]==5 and agglutinement(5,piece,i,j,probabilite): 
                          piece[i+1][j+1]=5
                          piece[i][j]=0
                      elif l[a]==11 and agglutinement(11,piece,i,j,probabilite):
                          piece[i-1][j-1]=5
                          piece[i][j]=0
                      elif l[a]==7 and agglutinement(7,piece,i,j,probabilite):
                          piece[i+1][j-1]=5
                          piece[i][j]=0                    
      for [i,j] in sallalea(cote1,cote2):
                if piece[i][j]==5:
                   piece[i][j]=1
      compte+=1
    return (piece,compte)

def test(Npersonnes,cote1,cote2,listeporte,probabilite,essaie):
    c=0
    for i in range(essaie):
        print i
        c+=evacuation(Npersonnes,cote1,cote2,listeporte,probabilite)[1]
    return float(c)/float(essaie)
    