Kristel Tan (ktan@bu.edu)
CAS CS350 Fundamentals of Computing Systems
Homework #2
Due: Tuesday, February 9, 2016 at 3PM

README.txt

Running the Program:

	- This program was run using Anaconda and the Spyder Python development environment. 
	- You will need distributions (i.e. NumPy, Matplotlib, & SciPy) from the Scipy stack to successfully run this file.
	- Used Python 3.5

All Files:

	hw2.py -- Contains source code for problems 3, 4, and 5 of this assignment

Functions: 

	Used in Question 3: 

	- empirical_exp(): returns a random value using the CDF for a uniformly distributed random variable y
	
	- analytical_exp(): returns a random value using the CDF for an exponentially distributed random variable x
	
	- Q3ab(): generates and plots the CDF using 100 exponentialy distributed random values (obtained empirically and analytically) and a given lambda of 4

	Used in Question 4: 

	- Q4d(): returns a random value in the list of t values with their calculated probabilities taken into account from the PMF described in part(a)

	Used in Question 5:

	- zrand(): returns a random value that is distributed according to a standard normal distribution by mapping a relationship between a uniform random variable from [0, 1] and a standard normal random variable 
	
	- norm_dist_cdf(): returns a value of a random variable according to the CDF equation of the standard normal distribution 
	
	- Q5ab(): uses the two functions above to generate 100 standard-normal random values. It then creates a plot of the empirical CDF and prints a comparison of the values with the actual CDF according to the normal distribution.
 

