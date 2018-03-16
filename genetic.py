import copy
from random import *
import random

class Gen(object):

	def __init__(self,g):
		self.matrice_distance =g

	def charbak(self,a,i,j):
		
		if (i < j):
			b = a[:i]
			b.extend(reversed(a[i:j])) 
			b.extend(a[j:])
		else:
			b = a[:j]
			b.extend(reversed(a[j:i]))
			b.extend(a[i:])

		return b

	def longueur(self,seq):
		return len(seq)

	def f(self,parcour):
		if self.longueur(parcour)>1:
			cout=0
			for i in range(self.longueur(parcour)-1):
				cout = sum( [ self.matrice_distance[parcour[i-1]-1][parcour[i]-1] for i in range(1,len(parcour)) ] ) + self.matrice_distance[parcour[0]-1][parcour[len(parcour)-1]-1]
				return cout
			else:
				return None

	def genetic(self):
		taille_population=10 
		prob=0.5
		population=[]
		sol=[1,2,3,4,5,6]
		st=0
		it = 0
		repeter=True
		best_f=None
		best_f_old=None
		best_sol=[]
		bes_sol_old=[]
		inversions = 0
		
		
		for x in range(0,taille_population):
			shuffle(sol)
			if sol not in population:
				population.append(copy.copy(sol))

		while(st < 10):
			it =it+1
			for i in range(0,len(population)):
				t = copy.copy(population[i])
				ville = t[random.randint(0,len(t)-1)]
				repeter = True
				best_f = None
				while repeter:
					
					
					
					if(random.random()<= prob): 
						ville2=t[random.randint(0, len(t) - 1)]
						
						while (ville == ville2):
							ville2 = t[random.randint(0, len(t) - 1)]
						

					
					else:
						sol2=population[random.randint(0, len(population) - 1)]

						
						if(sol2.index(ville) == (len(sol2) - 1)):
							ville2 = sol2[0]
						else:
							ville2=sol2[sol2.index(ville) + 1]


					
					if((t.index(ville2) + 1 == t.index(ville)) or (t.index(ville2) - 1 == t.index(ville)) or ((t.index(ville2) == 0) and (t.index(ville) == len(t) - 1)) or ((t.index(ville) == 0) and (t.index(ville2) == len(t) - 1))):
						repeter =False
					else: 
						t = copy.copy(self.charbak(t, t.index(ville), t.index(ville2)))
						inversions = inversions + 1

				if(self.f(t) <= self.f(population[i])):
					population[i] = copy.copy(t)

				if (best_f == None) or (self.f(population[i]) < best_f): 
					best_f = self.f(population[i])
					best_sol = copy.copy(population[i])
					


			
			if (best_f_old == None) or (best_f < best_f_old):
				best_f_old = best_f
				bes_sol_old = copy.copy(best_sol)
				st = 0
			else:
				st += 1


		bes_sol_old.append(bes_sol_old[0])
		print "meilleur sol tourve: "
		print bes_sol_old
		print "cout sol trouve: "
		print best_f_old

		
		print "Inversions: "
		print inversions
		print "Iterations: "
		print it


e=[[0,5,8,4,3,2],
   [5,0,4,2,1,3],
   [8,4,0,7,5,4],
   [4,2,7,0,9,8],
   [3,1,5,9,0,4],
   [2,3,4,8,4,0]]

g=Gen(e)
g.genetic() 