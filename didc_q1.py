# Q1: 
# - draw links represented as numbers from 1 to N
# - draw one link at a time
# - M = max subchain count; consecutive numbers form one subchain, all other numbers form one subchain by themselves
# OBJECTIVE: find mu and sigma of Ms for various Ns 

import os, random, math

#os.chdir("C:/Users/MelodyYin/Desktop")

# count_subchains : list-of-nums -> num
# counts the number of subchains in a list of nums
def count_subchains(arr):
	output = []
	ind = 0

	# value-index of sorted list finds consecutive groups 
	for link in sorted(arr):
		output.append(link-ind)
		ind+=1 

	# M = number of consecutive groups
	return len(set(output))

# std : num list-of-nums num -> num 
# calculates the standard deviation for a list of numbers given list's mean and length 
def std(mean, arr, l):
	var = float(sum([(x-mean)**2 for x in arr])) / (l-1)
	return math.sqrt(var)

# gen_chain : num -> void 
# prints the mean and standard deviation of subchain count distribution given chain length 
def gen_chain(N):
	chain = range(1, N+1)	# orig chain
	Ms = []	# store M here 

	# run 100 times to get distribution
	for i in range(100):
		res = []
		M = 0

		# keep drawing until all links drawn
		while len(res) != len(chain):
			res.append(random.choice(chain))
			sbc = count_subchains(res)
			# find the max subchain count 
			if sbc > M:
				M = sbc

		Ms.append(M) # add the largest M to the list 

	mu = sum(Ms) / float(len(Ms))
	sigma = std(mu, Ms, len(Ms))

	print "mean: ", mu
	print "stdv: ", sigma

def main():
	print "N=8"
	gen_chain(8)
	print "N=16"
	gen_chain(16)
	print "N=32"
	gen_chain(32)

if __name__ == '__main__':
    main()