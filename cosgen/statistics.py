from matplotlib import pyplot as plt
import numpy as np
import warnings
from scipy.spatial.distance import hamming
import os.path

class Statistics:
	def __init__(self,storage_path):
		self.storage_path = storage_path
		self.max_fitness = []
		self.average_fitness = []
		self.population_diversity = []

	def add(self,population):
		n = len(population)
		maxfitness = 0
		avefitness = 0
		pop_diversity = 0
		for s in population:
			if s.fitness > maxfitness:
				maxfitness = s.fitness
			avefitness += s.fitness
		avefitness = avefitness/n
		for i in range(n):
			for j in range(i+1,n):
				pop_diversity += hamming(population[i].l,population[j].l)
		pop_diversity = pop_diversity/(n*(n-1))*2
		self.max_fitness.append(maxfitness)
		self.average_fitness.append(avefitness)
		self.population_diversity.append(pop_diversity)

	def show(self):
		f, axarr = plt.subplots(3,sharex=True)
		axarr[0].plot(self.max_fitness)
		axarr[0].set_title('Max fitness')
		axarr[1].plot(self.average_fitness)
		axarr[1].set_title('Average fitness')
		axarr[2].plot(self.population_diversity)
		axarr[2].set_title('Population diversity')
		plt.savefig(os.path.join(self.storage_path,'stats.pdf'))
