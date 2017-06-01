#!/usr/bin/python3

try:
	from cosgen.functions import functions
	from cosgen.algorithms import ga
	import cosgen.fitness_measures as fitness_measures
	from cosgen.sequence import sequence
	from cosgen.mutate import mutate
	from cosgen.cross_over import cross_over
	from cosgen.immigrants import generate_immigrants
	import cosgen.models as models
except ImportError:
	from functions import functions
	from algorithms import ga
	import fitness_measures
	from sequence import sequence
	from mutate import mutate
	from cross_over import cross_over
	from immigrants import generate_immigrants
	import models

import argh
from os.path import expanduser
from functools import partial
import numpy as np

def cli_algorithm(population_size=20, library_size=10, storage_path='~/.cosgen/sequences', seqlength=100, nstimtypes=1, generations=10000, survivors=5):
	storage_path = expanduser(storage_path)
	fcts = functions()
#	def design_mat(x):
#		return np.diag(x.l)
#	def cov_mat(x):
#		return np.identity(len(x[0]))
#	model = models.Model(design_mat, cov_mat)
	gamma_hrf = models.get_gamma_hrf(1,40,5,1,10,1,1)
	ar1_cov = models.get_ar1_cov(139,0.5)
#	import math
#	gamma_hrf = np.zeros(40)
#	gamma_hrf[0:len(gamma_hrf):2]=1
#	ar1_cov = np.identity(139)
	model = models.DetectionModel(gamma_hrf,err_cov_mat=ar1_cov)
	fcts.add_fitness_measure('cov',partial(fitness_measures.estimator_variance,model=model,optimality='a'))
#	fcts.add_fitness_measure('test', fitness_measures.test)
	fcts.set_mutate(mutate)
	fcts.set_cross_over(cross_over)
	fcts.set_generate_immigrants(generate_immigrants)
	population = [sequence(seqlength,nstimtyps) for i in range(population_size)]
	population = ga(population,fcts,generations,survivors)
	for seq in fcts.find_best(population,library_size):
		#seq.dump(storage_path)
		print(seq.l)

def main():
	argh.dispatch_command(cli_algorithm)

if __name__ == '__main__':
	main()
