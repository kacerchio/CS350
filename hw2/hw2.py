'''

Kristel Tan (ktan@bu.edu)
CAS CS350 Spring 2016 - Professor Bestavros
hw2.py

'''

import math
import random
from matplotlib import pyplot as plt
import numpy as np
import scipy

# Question 3

# empirical_exp() returns a random value using the
# cumulative distribution function for a uniformly
# distributed random variable y

def empirical_exp(y, lamb):
    return -math.log(1.0 - y) / lamb

# analytical_exp() returns a random value using the
# cumulative distribution function for an exponentially
# distributed random variable x

def analytical_exp(x, lamb):
    return 1 - math.exp(-(lamb) * x)
    
# Question 3a & 3b
    
# Q3ab() generates and plots the CDF using 100 
# exponentialy distributed random values (obtained
# empirically and analytically) and a given lambda of 4.

def Q3ab():
    
    y_data = []
    emp_data = []
    for i in range(100):
        y = random.uniform(0, 1)
        e = empirical_exp(y, 4)
        emp_data.append(e)
        y_data.append(y)

    x_data = np.arange(0, max(emp_data), 0.01)
    ana_data = []
    for i in x_data:
        a = analytical_exp(i, 4)
        ana_data.append(a)

    plt.figure(1)
    plt.plot(emp_data, y_data, 'ro')
    plt.plot(x_data, ana_data, 'bo')
    plt.title('Exponential Distributions: Empirical vs. Analytical')
    plt.ylabel('Probability')
    plt.ylim(0.0, 1.2)
    plt.xlabel('Random Values')

    bins = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2]
    plt.figure(2)
    plt.hist(emp_data, bins, normed = True, color = 'r')
    plt.title('Relative Frequency of Random Variable Queries')
    plt.ylabel('Frequency')
    plt.ylim(0.0, 3.6)
    plt.xlabel('0.1-second Intervals')
    
    plt.show()

Q3ab()

# Question 4d

# Q4d() returns a random value in the list of t values
# with their calculated probabilities taken into account
# from the PMF described in part(a)

def Q4d():
    
    ts = [1, 3, 10, 30]
    probs = [0.5, 0.3 ,0.14, 0.06]
    n = random.uniform(0, 1)
    cumulative_prob = 0.0
    
    for t, t_prob in zip(ts, probs):
        cumulative_prob += t_prob
        if n < cumulative_prob:
            break
        
    return t
    
# Question 5
    
# zrand() returns a random value that is distributed according to 
# a standard normal distribution by mapping a relationship between
# a uniform random variable from [0, 1] and a standard normal 
# random variable
    
def zrand(mu, sigma, y):
    return mu + (math.sqrt(2)* sigma * scipy.special.erfinv((2*y) - 1))

def norm_dist_cdf(mu, sigma, x):
    return 0.5 * (1 + math.erf((x - sigma) / (math.sqrt(2)* sigma )))

# Question 5a & 5b

# Q5ab() uses the two functions above to generate 100
# standard-normal random values. It then creates a plot of the 
# empirical CDF and prints a comparison of the values 
# with the actual CDF according to the normal distribution.
 
def Q5ab():
    
    zrand_data = []
    y_data = []
    
    for i in range(100):
        y = random.uniform(0,1)
        y_data.append(y)
        z = zrand(0, 1, y)
        zrand_data.append(z)

    plt.figure(1)
    plt.plot(zrand_data, y_data, 'bo')
    plt.title('CDF of Standard Normal Distribution')
    plt.ylabel('Probability')
    plt.ylim(0.0, 1.2)
    plt.xlabel('Z Scores')
    plt.show()
    
    mu = sum(zrand_data) / 100
    sigma = 0
    
    for z in zrand_data:
        sigma += pow(z - mu, 2)
    sigma = sigma/99
    
    print('\n')
    
    print('Empirical CDF of 0: ', norm_dist_cdf(mu, sigma, 0))
    print('Actual CDF of 0:    ', norm_dist_cdf(0, 1, 0), '\n')
    
    print('Empirical CDF of 1: ', norm_dist_cdf(mu, sigma, 1))
    print('Actual CDF of 1:    ', norm_dist_cdf(0, 1, 1), '\n')
    
    print('Empirical CDF of 2: ', norm_dist_cdf(mu, sigma, 2))
    print('Actual CDF of 2:    ', norm_dist_cdf(0, 1, 2), '\n')
    
    print('Empirical CDF of 3: ', norm_dist_cdf(mu, sigma, 3))
    print('Actual CDF of 3:    ', norm_dist_cdf(0, 1, 3), '\n')
    
    print('Empirical CDF of 4: ', norm_dist_cdf(mu, sigma, 4))
    print('Actual CDF of 4:    ', norm_dist_cdf(0, 1, 4), '\n')
    
    print(norm_dist_cdf(72, 256, 80) - norm_dist_cdf(72, 256, 66))
    
Q5ab()
        

    


