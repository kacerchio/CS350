'''

Kristel Tan (ktan@bu.edu)
CAS CS350 Spring 2016 - Professor Bestavros
hw5 - fcfs.py

'''

import random 

# Given lambda, returns a random value according to an 
# exponential distribution using the built-in Python random function
def exponential(lamda):
    return random.expovariate(lamda)

# Simulates a first come first serve scheduler for I/O bound jobs
# with an arrival rate of 6 jobs per second and an exponential service time
# with mean 0.01 seconds    
def fcfs_io():
    
    print('')
    print('-------------------------------------------------------------')
    print('          First Come First Serve I/O Bound Results           ')
    print('-------------------------------------------------------------')
   
    n = input('Enter the total # of processes:')
    n = int(n)
    queue = []
    total_tw = 0
    total_ts = 0
    process_counter = 0
    
    for i in range(n):
        queue.append([])
        queue[i].append(process_counter)
        process_counter += 1
        queue[i].append(exponential(6))
        total_tw += queue[i][1]
        queue[i].append(exponential(.01))
        total_ts += queue[i][2]
        
    queue.sort(key = lambda queue:queue[1])
    
    print('')
    print('Process No.\tArrival Time\t\t Service Time')
    
    for i in range(n):
        print('Process ', queue[i][0], '\t', queue[i][1], '\t', queue[i][2])
    
    print('')
    print('Total waiting time: ', total_tw, ' sec')
    print('Average waiting time: ', (total_tw / n), ' sec')
    print('Average Tq: ', (n / 6))
    print('Average Ts: ', (total_ts / n), ' sec')
    print('Slowdown: ', (n / 6) / (total_ts / n))
 
# Simulates a first come first serve scheduler for CPU bound jobs
# with an arrival rate of 3 jobs per second and an exponential service time
# with mean 0.3 seconds      
def fcfs_cpu():
    
    print('')
    print('-------------------------------------------------------------')
    print('          First Come First Serve CPU Bound Results           ')
    print('-------------------------------------------------------------')
    
    n = input('Enter the total # of processes:')
    n = int(n)
    queue = []
    total_tw = 0
    total_ts = 0
    process_counter = 0
    
    for i in range(n):
        queue.append([])
        queue[i].append(process_counter)
        process_counter += 1
        queue[i].append(exponential(3))
        total_tw += queue[i][1]
        queue[i].append(exponential(0.3))
        total_ts += queue[i][2]
        
    queue.sort(key = lambda queue:queue[1])
    
    print('')
    print('Process No.\tArrival Time\t\t Service Time')
    
    for i in range(n):
        print('Process ', queue[i][0], '\t', queue[i][1], '\t', queue[i][2])
    
    print('')
    print('Total waiting time: ', total_tw, ' sec')
    print('Average waiting time: ', (total_tw / n), ' sec')
    print('Average Tq: ', (n / 3))
    print('Average Ts: ', (total_ts / n), ' sec')
    print('Slowdown: ', (n / 6) / (total_ts / n))

fcfs_io()
fcfs_cpu()