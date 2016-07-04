'''

Kristel Tan (ktan@bu.edu)
CAS CS350 Spring 2016 - Professor Bestavros
hw4 - hw4_q2.py

'''

import random 
from enum import Enum  
from collections import deque
import statistics as stats
import sys
import math

avg_qs = []         # Keep track of q's returned from monitoring queue
avg_ws = []         # Keep track of w's returned from monitoring queue
ts = []             # Keep track of mean service times returned from monitoring queue
tws = []            # Keep track of mean wait times returned from monitoring queue

# Resets monitoring queue statistical trackers
def clear_trackers(avg_qs, avg_ws, ts, tws):
    del avg_qs[:]         
    del avg_ws[:]         
    del ts[:]             
    del tws[:]

# Enumerated type of event types (i.e. death and birth)
class EventType(Enum):
    death = 0
    birth = 1
    
# Event object with initialized with arrival time, service start time,
# service time (i.e. Ts), and the event type
class Event(object):
        
    def __init__(self, arrival_time, serv_start, serv_time, event_type):
        
        self.arrival_time = arrival_time
        self.serv_start = serv_start
        self.serv_time = serv_time
        self.end_time = self.serv_start + self.serv_time
        self.wait_time = self.serv_start - self.arrival_time
        
        if type(event_type) is not EventType:
            raise ValueError("Event type is unknown")
        self.event_type = event_type

# Given lambda, returns a random value according to an 
# exponential distribution using the built-in Python random function
def exponential(lamda):
    return random.expovariate(lamda)

# monitor() prints some statistical analysis based on the current 
# state of the system including mean Ts, std deviation, w, and q
def monitor(q, lamda):  
    
    print("\n--------------------------------")
    print("    Monitoring Current Queue      ")
    print("--------------------------------\n")
    
    serv_times = [event.serv_time for event in list(q)]
    mean = stats.mean(serv_times)
    ts.append(mean)
    print("mean Ts = ", mean)
    
    if (len(serv_times) > 1):
        std_dev = stats.stdev(serv_times)
        print("std dev = ", std_dev) 
    
    wait_times = [event.wait_time for event in list(q)]
    avg_wait_time = stats.mean(wait_times)
    tws.append(avg_wait_time)
    w = lamda * avg_wait_time
    avg_ws.append(w)
    print("w = ", w)    
    
    total_times = [event.wait_time + event.serv_time for event in list(q)]
    avg_time_in_system = stats.mean(total_times)
    q = lamda * avg_time_in_system
    avg_qs.append(q)
    print("q = ", q)
    
    print("--------------------------------\n")
    
# The mmk1() function handles both the controller and the simulator
# of an M/M/1/K system. It services births and their corresponding deaths
# based on the given k (queue size), lambda, and simulation time
def mmk1(k, lamda, sim_time):
    
    clock = 0           # Initialize the clock to 0
    server = []         # Initialize server to be empty
    busy = False        # Set server to not busy status
    q = deque([], k)    # Intialize empty queue of size k
    num_rejects = 0     # Counter for number of rejections
    num_served = 0      # Counter for number of serviced events
    
    # Queue first event
    arrival_time = exponential(lamda)
    serv_start = arrival_time
    serv_time = exponential(lamda)
    q.append(Event(arrival_time, serv_start, serv_time, EventType.birth))
  
    # Begin simulation
    while(clock < sim_time):
        
        if (len(q) > 0):
            
            # Store the first event in the queue as the current event
            current_event = list(q)[0]
            
            # Generate a random new event with random arrival time
            # and random service time according to an exponential distribution
            arrival_time += exponential(lamda)
            serv_start = max(arrival_time, list(q)[-1].end_time)
            serv_time = exponential(lamda)
            event_type = random.choice(list(EventType))
            new_event = Event(arrival_time, serv_start, serv_time, event_type)
            
            # If the new event generated is a birth and the queue has space,
            # add the event to the queue
            if ((new_event.event_type == EventType.birth) and (len(q) < 3)):
                print('Adding new event to queue...')
                
                # Add the new event to the queue based on sooner arrival time
                if (new_event.arrival_time > current_event.arrival_time):
                    q.appendleft(new_event)
                    current_event = list(q)[0]
                else:
                    q.append(new_event)
                
                print('Queue peek:')
                for event in list(q): print(event.event_type, 'Arrival time: ', event.arrival_time)
                print('')
                
                # Do a random monitor check on the queue
                monitor_check = random.choice([0, 1])
                if (monitor_check == 1 and len(q) > 0):
                    monitor(q, lamda)
                    
            # Else, if the event is a death event or the queue is full, reject event
            else:
                print('Event rejected!')
                print('Queue peek:')
                for event in list(q): print(event.event_type, 'Arrival time: ', event.arrival_time)
                print('')
                num_rejects += 1 
    
                # Do a random monitor check on the queue
                monitor_check = random.choice([0, 1])
                if (monitor_check == 1 and len(q) > 0):
                    monitor(q, lamda)
                    
            # Move the current event to the server if it is not busy
            if (busy is False):   
                print('Server is not busy, serving event now...\n')
                num_served += 1
                q.pop()                         # Pop event from queue
                server.append(current_event)    # Add event to the server
                busy = True                     # Set server to busy
          
                current_event.event_type = EventType.death      # Update event type to death
                server.remove(current_event)                    # Remove event from server
                busy = False                                    # Set server to not busy

            clock = arrival_time
            
        else:
            
            print('Queue is empty, adding a new event...\n')
            arrival_time += exponential(lamda)
            serv_start = arrival_time
            q.append(Event(arrival_time, serv_start, serv_time, EventType.birth))
            
            clock = arrival_time
            
    # Generate statistical analysis for M/M/1/K queue 
    
    print('Simulation finished. \n')
    q = stats.mean(avg_qs)
    w = stats.mean(avg_ws)
    p = lamda * serv_time
    pr_rej = num_rejects / num_served
    
    lamda_prime = lamda*(1-pr_rej)
    
    Tq = q / lamda_prime
    Ts = stats.mean(ts)
    Tw = stats.mean(tws)

    print("\n--------------------------------")
    print("     M/M/1/K Queue Analysis       ")
    print("--------------------------------\n")
    print("p = ", p, "\n")
    print("pr(rej) = ", pr_rej, "\n")
    print("Tq = ", Tq, "\n")
    print("mean Ts = ", Ts, "\n")
    print("mean Tw = ", Tw, "\n")
    print("q = ", q, "\n")
    print("w = ", w, "\n")
    print("--------------------------------\n")

# The md1() function handles both the controller and the simulator
# of an M/D/1 system. It schedules births and their corresponding deaths
# based on the given k (queue size), lambda, service time, and simulation time
def md1(k, lamda, serv_time, sim_time):
    
    clock = 0           # Initialize the clock to 0
    server = []         # Initialize server to be empty
    busy = False        # Set server to not busy status
    q = deque([], k)    # Intialize empty queue of size k
    num_rejects = 0     # Counter for number of rejections
    num_served = 0      # Counter for number of serviced events
    
    # Queue first event
    arrival_time = exponential(lamda)
    serv_start = arrival_time
    q.append(Event(arrival_time, serv_start, serv_time, EventType.birth))
  
    # Begin simulation
    while(clock < sim_time):
        
        if (len(q) > 0):
            
            # Store the first event in the queue as the current event
            current_event = list(q)[0]
            
            # Generate a random new event with random arrival time
            # according to an exponential distribution
            arrival_time += exponential(lamda)
            serv_start = max(arrival_time, list(q)[-1].end_time)
            event_type = random.choice(list(EventType))
            new_event = Event(arrival_time, serv_start, serv_time, event_type)
            
            # If the new event generated is a birth and the queue has space,
            # add the event to the queue
            if ((new_event.event_type == EventType.birth) and (len(q) < 3)):
                print('Adding new event to queue...')
                
                # Add the new event to the queue based on sooner arrival time
                if (new_event.arrival_time > current_event.arrival_time):
                    q.appendleft(new_event)
                    current_event = list(q)[0]
                else:
                    q.append(new_event)
                
                print('Queue peek:')
                for event in list(q): print(event.event_type, 'Arrival time: ', event.arrival_time)
                print('')
                
                # Do a random monitor check on the queue
                monitor_check = random.choice([0, 1])
                if (monitor_check == 1 and len(q) > 0):
                    monitor(q, lamda)
                    
            # Else, if the event is a death event or the queue is full, reject event
            else:
                print('Event rejected!')
                print('Queue peek:')
                for event in list(q): print(event.event_type, 'Arrival time: ', event.arrival_time)
                print('')
                num_rejects += 1 
    
                # Do a random monitor check on the queue
                monitor_check = random.choice([0, 1])
                if (monitor_check == 1 and len(q) > 0):
                    monitor(q, lamda)
                    
            # Move the current event to the server if it is not busy
            if (busy is False):   
                print('Server is not busy, serving event now...\n')
                num_served += 1
                q.pop()                         # Pop event from queue
                server.append(current_event)    # Add event to the server
                busy = True                     # Set server to busy
          
                current_event.event_type = EventType.death      # Update event type to death
                server.remove(current_event)                    # Remove event from server
                busy = False                                    # Set server to not busy

            clock = arrival_time
            
        else:
            
            print('Queue is empty, adding a new event...\n')
            arrival_time += exponential(lamda)
            serv_start = arrival_time
            q.append(Event(arrival_time, serv_start, serv_time, EventType.birth))
            
            clock = arrival_time
            
    # Generate statistical analysis for M/M/1/K queue 
    
    print('Simulation finished. \n')
    q = stats.mean(avg_qs)
    w = stats.mean(avg_ws)
    p = lamda * serv_time
    pr_rej = num_rejects / num_served
    
    lamda_prime = lamda*(1-pr_rej)
    
    Tq = q / lamda_prime
    Tw = stats.mean(tws)

    print("\n--------------------------------")
    print("     M/D/1/K Queue Analysis       ")
    print("--------------------------------\n")
    print("p = ", p, "\n")
    print("pr(rej) = ", pr_rej, "\n")
    print("Tq = ", Tq, "\n")
    print("fixed Ts = ", serv_time, "\n")
    print("mean Tw = ", Tw, "\n")
    print("q = ", q, "\n")
    print("w = ", w, "\n")
    print("--------------------------------\n")

# Generate log files for Problem 2
# Comparisons are made for theoretical vs. experimental values of M/M/1/K system

sys.stdout = open('log_2ab.txt', 'w')

mmk1(3, 50, 100)
p1 = 50 * 0.020
q1 = 3/2
pr_rej1 = 1/(3+1)
lamda_prime = 50*(1-pr_rej1)
tq1 = q1 / lamda_prime
tw1 = tq1 - 0.020
w1 = tw1 * lamda_prime
print('Part a')
print("\n---------------------------------")
print("M/M/1/K Queue Analytical Analysis ")
print("---------------------------------\n")
print("p = ", p1, "\n")
print("pr(rej) = ", pr_rej1, "\n")
print("Tq = ", tq1, "\n")
print("Ts = ", 0.020, "\n")
print("mean Tw = ", tw1, "\n")
print("q = ", q1, "\n")
print("w = ", w1, "\n")
print("--------------------------------\n")

p1 = 50 * 0.015
q1 = (p1 / (1 - p1)) - ((4*math.pow(p1,4)) / (1-math.pow(p1,4)))
pr_rej1 = ((1-p1)*math.pow(p1, 3)) / (1-math.pow(p1,4))
lamda_prime = 50*(1-pr_rej1)
tq1 = q1 / lamda_prime
tw1 = tq1 - 0.015
w1 = tw1 * lamda_prime
print('Part b')
print("\n---------------------------------")
print("M/M/1/K Queue Analytical Analysis ")
print("---------------------------------\n")
print("p = ", p1, "\n")
print("pr(rej) = ", pr_rej1, "\n")
print("Tq = ", tq1, "\n")
print("Ts = ", 0.015, "\n")
print("mean Tw = ", tw1, "\n")
print("q = ", q1, "\n")
print("w = ", w1, "\n")
print("--------------------------------\n")
clear_trackers(avg_qs, avg_ws, ts, tws)

sys.stdout.flush()
sys.stdout = open('log_2c.txt', 'w') 

mmk1(3, 65, 100)
p2 = 65 * 0.015
q2 = (p2 / (1 - p2)) - ((4*math.pow(p2,4)) / (1-math.pow(p2,4)))
pr_rej2 = 1/(3+1)
lamda_prime = 65*(1-pr_rej1)
tq2 = q2 / lamda_prime
tw2 = tq2 - 0.015
w2 = tw2 * lamda_prime
print("\n---------------------------------")
print("M/M/1/K Queue Analytical Analysis ")
print("---------------------------------\n")
print("p = ", p2, "\n")
print("pr(rej) = ", pr_rej2, "\n")
print("Tq = ", tq2, "\n")
print("Ts = ", 0.015, "\n")
print("mean Tw = ", tw2, "\n")
print("q = ", q2, "\n")
print("w = ", w2, "\n")
print("--------------------------------\n")
clear_trackers(avg_qs, avg_ws, ts, tws)

sys.stdout.flush()
sys.stdout = open('log_2d.txt', 'w')
md1(3, 50, 0.015, 100)
clear_trackers(avg_qs, avg_ws, ts, tws)

sys.stdout.flush()
sys.stdout = open('log_2e.txt', 'w')
md1(3, 65, 0.015, 100)
clear_trackers(avg_qs, avg_ws, ts, tws)
