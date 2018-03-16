import math
import random
import copy

class Taboo(object):
	def __init__(self, parcour, graphe):
		self.parcour = parcour
		self.n = len(parcour)
		
		self.matrice_distance = graphe
		self.t=[]
		self.nbr_max_it = 200

	def f(self, sol):
		'''la fonction li katrj3lna cout dyal parcours''' 
		return sum( [ self.matrice_distance[sol[i-1]-1][sol[i]-1] for i in range(1,self.n) ] ) + self.matrice_distance[sol[0]-1][sol[self.n-1]-1]

	def khalat(self, p):
		l = random.randint(2, self.n-1)
		i = random.randint(0, self.n-l)
		p[i:(i+l)] = reversed(p[i:(i+l)])
		return p


	def Tboo(self):
		k=0
		best_solution = copy.copy(self.parcour)
		while k<self.nbr_max_it:
			k = k+1
			v={}
			a= copy.copy(best_solution)
			for i in range(self.n*(self.n-2)+2):
				a= copy.copy(best_solution)
				a = self.khalat(a)
				
				if (self.f(a) < self.f(best_solution)):
					if a not in v.values():
						if a not in self.t:
							v[self.f(a)]=a
							
			if(len(v)>0):
				b=min(v,key=v.get)
				self.t.append(v[b])
				best_solution = copy.copy(v[b])

		self.parcour.append(self.parcour[0])
		print("parcours initial")
		print(self.parcour)
		print("distance parcours initial")
		print((self.f(self.parcour)))
		print("parcours ameliore:")
		best_solution.append(best_solution[0])
		print(best_solution)
		print("distance parcours ameliore:")
		print((self.f(best_solution)))
		



