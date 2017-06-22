"""This file holds functions to mutate sequences."""
import random

class InvalidFractionError(Exception):
	pass

def mutate(sequence,mutation_fraction):
	"""
	Mutate sequence with given probability.

	This function randomly changes 'mutation_fraction' of the entires
	of the sequence given and returns the changes sequence.

	Parameters
	----------
	sequence : cosgen.sequence.Sequence
	    Sequence to be mutated.
	mutation_fraction : float
	    Fraction of sequence elements to be changed. Has to be between
	    0 and 1.

	Returns
	-------
	cosgen.sequence.Sequence
	    Altered sequence.
	"""
	
	if mutation_fraction<0 or mutation_fraction>1:
		raise InvalidFractionError('mutation_fraction has to be between 0 and 1. Value given was {0}'.format(mutation_fraction))

	length = len(sequence.l)
	idxs = random.sample(range(length),int(length*mutation_fraction))
	for i in idxs:
		sequence.l[i] = random.randrange(sequence.nstimtypes+1)
	return sequence
