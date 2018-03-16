import math
import random
import copy

class SimRecuit(object):

    def __init__(self, parcour,graphe):
        self.parcour = parcour
        self.N = len(parcour)
        
        self.T=6
        self.alpha = 0.995
        self.stop_temp = 0.00000001

        self.matrice_distance = graphe

        self.sol_cour = parcour
        self.best_solution = copy.copy(self.sol_cour)
        

        self.sol_cour_f = self.f(self.sol_cour)
        self.best_f = self.sol_cour_f
        

    def f(self, sol):
        
        return sum( [ self.matrice_distance[sol[i-1]-1][sol[i]-1] for i in range(1,self.N) ] ) + self.matrice_distance[sol[0]-1][sol[self.N-1]-1]

    def P_accept(self, candidat_f):
        '''
        probabilite daccepter un voisin plus mauvais
        exp(-delta f ij/t)page 5
        '''
        return math.exp( -abs(candidat_f-self.sol_cour_f) / self.T  )

    def accept(self, candidat):
        '''
        accepter si meilleur avec p=1
        accepter avec p=exp(-delta f ij/t) si mauvais
        '''
        candidat_f = self.f(candidat)
        if candidat_f < self.sol_cour_f:
            self.sol_cour_f = candidat_f
            self.sol_cour = candidat
            if candidat_f < self.best_f:
                self.best_f = candidat_f
                self.best_solution = candidat

        else:
            if random.random() < self.P_accept(candidat_f):
                self.sol_cour_f = candidat_f
                self.sol_cour = candidat

    def Recuit(self):
        '''
        algorithme 
        '''
        while self.T >= self.stop_temp:
            candidat = copy.copy(self.sol_cour) 

            l = random.randint(2, self.N-1)
            i = random.randint(0, self.N-l)
            candidat[i:(i+l)] = reversed(candidat[i:(i+l)])

            self.accept(candidat)
            self.T *= self.alpha

        

        self.parcour.append(self.parcour[0])
        print("parcours initial")
        print(self.parcour)
        print("distance parcours initial")
        print((self.f(self.parcour)))
        print("parcours ameliore:")
        self.best_solution.append(self.best_solution[0])
        print(self.best_solution)
        print("distance parcours ameliore:")
        print((self.f(self.best_solution)))



