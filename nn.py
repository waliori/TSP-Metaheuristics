import time,sys
from alg1 import SimRecuit
from taboooooo import Taboo

class Graphe:
    def __init__(self,graphe):
        self.graphe =graphe
    def arcExist(self,i,j):
        if self.graphe[i][j]!=None:
            return True
        return False
    def longueur(self,seq):
        return len(seq)
    def distance(self,seq):
        cout=0
        if self.longueur(seq)>1:
            for i in range(self.longueur(seq)-1):
                if self.arcExist(seq[i],seq[i+1]):
                    cout+=self.graphe[seq[i]][seq[i+1]]
        return cout
    def plusProche(self,nb_sommet,sommet):
        tete=sommet
        parcours=[]
        cycle=[]
        parcours.append(tete)
        while(len(parcours)<nb_sommet):
            minArc=sys.maxint
            minSommet=None
            for i in range(nb_sommet):
                i=i+1
                if i not in parcours:
                    if self.graphe[parcours[-1]][i]<minArc:
                        minArc=self.graphe[parcours[-1]][i]
                        minSommet=i
            parcours.append(minSommet)
        #print("distance parcours")
        #print self.distance(parcours)
        return parcours
                    
                
        
tps1 = time.clock() 

w=[None,[None,None,5,8,4,3,2],
   [None,5,None,4,2,1,3],
   [None,8,4,None,7,5,4],
   [None,4,2,7,None,9,8],
   [None,3,1,5,9,None,4],
   [None,2,3,4,8,4,None]]

e=[[0,5,8,4,3,2],
   [5,0,4,2,1,3],
   [8,4,0,7,5,4],
   [4,2,7,0,9,8],
   [3,1,5,9,0,4],
   [2,3,4,8,4,0]]


g=Graphe(w)
a = g.plusProche(6,1)


#####################################(decommentez lalgorithme avec le quel vous voulez ameliorer et commenter l'autre votre parcours --par defaut taboo)
#### amelioration avec taboo
print 'amelioration avec tabou'
t=Taboo(a,e)
t.Tboo()

#### amelioration avec recuit simule 
#print 'amelioration avec recuit simule'
#sa = SimRecuit(a,e)
#sa.Recuit()

