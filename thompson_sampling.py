
import random 
import numpy as np
import pdb

def thompson_sampling(p,numSamples):
	###########################################################################
	# Thompason Sampling Algorthm
	#
	# a = # numbers of successes of each variant 
	# b = # numbers of failures of each variant
	# Initialize priors with ignorant state of Beta(1,1) (Uniform distribution)
	#
	a = np.ones( np.size(p) )
	b = np.ones( np.size(p) )

	# draw from beta distribution for each variant
	for i in range(numSamples):
		draw = np.zeros( np.size(p) )
		for i in range( np.size(a) ):
			draw[i] = random.betavariate(a[i],b[i])
		
		# Select the variant with the largest numbers drawn from the beta distribution
		selected_arm = np.amax(draw) == draw
		
		# Test and observe the result of the selcted arm
		U = random.random()
		success = U < p[selected_arm]
		failure = U > p[selected_arm]
		
		# Update prior beta distribution for selected arm
		a[selected_arm] = a[selected_arm] + success
		b[selected_arm] = b[selected_arm] + failure
		
	return a, b
	

if __name__ == "__main__":
	
	### Initial test - 3 variants 
	# Test
	# p ~ probability of success of each variant in test
	p = np.array([.5,.333333,.166666])
	numSuccesses = np.zeros(3) 
	numSamples = 10**6
		
	a, b = thompson_sampling(p, numSamples)
	percent_wins = a/(a+b)
	print percent_wins
	
	
	
