'''

Kristel Tan (ktan@bu.edu)
CAS CS350 Spring 2016 - Professor Bestavros
hw4 - hw4_q3.py

'''

import random 
from enum import Enum  
from collections import deque
import sys

# Given lambda, returns a random value according to an 
# exponential distribution using the built-in Python random function
def exponential(lamda):
    return random.expovariate(lamda)  

cpu = deque()     # Initalize cpu queue to be empty, cpu_q[0] = server 1 and cpu_q[1] = server 2
disk = deque()    # Intialize disk queue to be empty, disk_q[0] = disk server
net = deque()     # Intialize network resource to be empty, net[0] = network server
sched = deque()   # Intialize schedule
    
# Enumerated type of event types (i.e. death and birth)
class EventType(Enum):
    death = 0
    birth = 1

# Enumerated type of resource types (i.e. death and birth)
class Resource(Enum):
    cpu = 'c'
    disk = 'd'
    net = 'n'

# Event object with initialized with arrival time, service start time,
# service time (i.e. Ts), and the event type
class Event(object):
        
    def __init__(self, arrival_time, serv_start, serv_time, event_type, res):
        
        self.arrival_time = arrival_time
        self.serv_start = serv_start
        self.serv_time = serv_time
        self.end_time = self.serv_start + self.serv_time
        self.wait_time = self.serv_start - self.arrival_time
        self.res = res
        
        if type(event_type) is not EventType:
            raise ValueError("Event type is unknown")
        self.event_type = event_type
        
        if type(res) is not Resource:
            raise ValueError("Resource type is unknown")
        self.res = res

# sim_cpu() handles where an event passed to the CPU should go        
def sim_cpu(clock, event, arrival_time):
    
    print('CPU queue peek: ')
    for event in list(cpu): print(event.event_type, 'Arrival time: ', event.arrival_time, '\n')
    
    # Put birth event in a CPU server or CPU queue depending on what's available
    if (event.event_type == EventType.birth): 
    
        if (len(cpu) == 0 or len(cpu) == 1): 
            print('A CPU server is free, serving event now...\n')
            cpu.append(event)         # Add event to the server
            
            # Schedule death event of event being served
            death_event = event
            death_event.event_type = EventType.death
            death_event.arrival_time = event.end_time
            sched.append(death_event)
            
        # Add the event to the CPU queue if both servers are full
        elif (len(cpu) > 2):
            print('Both CPU servers are full, adding the event to the CPU queue...\n')
            cpu.append(event)
            
    # Put death event in a CPU server or CPU queue depending on what's available
    elif (event.event_type == EventType.death):
        
        if (len(cpu) == 0 or len(cpu) == 1): 
            print('A CPU server is free, serving event now...\n')
            cpu.append(event)         # Add event to the server
            
        # Add the event to the CPU queue if both servers are full
        elif (len(cpu) > 2):
            print('Both CPU servers are full, adding the event to the CPU queue...\n')
            cpu.append(event)
            
    # Generate a random new event with random arrival time
    # and service time uniformly distributed between 1 and 39 msec
    arrival_time = list(sched)[-1].arrival_time + exponential(40)
    serv_start = max(arrival_time, list(sched)[-1].end_time)
    serv_time = random.uniform(0.001, 0.0039)
    new_event = Event(arrival_time, serv_start, serv_time, EventType.birth, Resource.cpu)
    sched.append(new_event)  
    
    if (arrival_time > list(cpu)[0].arrival_time):     
        # Generate random probability to see where next CPU process should go
        prob = random.uniform(0, 1) 
        # Move first process of CPU to Disk with probability of 0.1
        if (prob <= 0.1):
            e = cpu.pop()
            e.res = Resource.disk
            clock += e.serv_time
            sim_disk(clock, e, arrival_time)
        # Move first process of CPU to Network with probability of 0.4
        elif (prob > 0.1 and prob < 0.5):
            e = cpu.pop()
            e.res = Resource.net
            e.serv_time = 0.025
            clock += e.serv_time
            sim_net(clock, e, arrival_time)
        # Process is finished with probability of 0.5
        else:
            cpu.pop()

# sim_disk() handles where an event passed to the Disk should go        
def sim_disk(clock, event, arrival_time):
    
    print('Disk queue peek: ')
    for event in list(disk): print(event.event_type, 'Arrival time: ', event.arrival_time, '\n')
    
    # Put birth event in the Disk server or queue depending on what's available
    if (event.event_type == EventType.birth): 
    
        if (len(disk) == 0): 
            print('Disk server is free, serving event now...\n')
            disk.append(event)         # Add event to the server
            
            # Schedule death event of event being served
            death_event = event
            death_event.event_type = EventType.death
            death_event.arrival_time = event.end_time
            sched.append(death_event)
            
        # Add the event to the Disk queue if its server is full
        elif (len(disk) > 1):
            print('Disk server is busy, adding the event to the Disk queue...\n')
            disk.append(event)
            
    # Put death event in the Disk server or queue depending on what's available
    elif (event.event_type == EventType.death):
        
        if (len(disk) == 0): 
            print('Disk server is free, serving event now...\n')
            disk.append(event)         # Add event to the server
            
        # Add the event to the Disk queue if its server is full
        elif (len(disk) > 1):
            print('Disk server is full, adding the event to the Disk queue...\n')
            disk.append(event)
    
    if (clock > list(disk)[0].arrival_time):  
        # Generate random probability to see next Disk process should go
        prob = random.uniform(0, 1) 
        # Move first process of Disk to CPU with probability of 0.5
        if (prob <= 0.5):
            e = disk.pop()
            e.res = Resource.cpu
            e.serv_time = 0.025
            clock += e.serv_time
            sim_cpu(clock, e, arrival_time)
        # Move first process of Disk to Network with probability of 0.5
        else:
            e = disk.pop()
            e.res = Resource.net
            e. serv_time = 0.025
            clock += e.serv_time
            sim_net(clock, e, arrival_time)

# sim_net() handles where an event passed to the Network should go        
def sim_net(clock, event, arrival_time):
    
    print('Network queue peek: ')
    for event in list(net): print(event.event_type, 'Arrival time: ', event.arrival_time, '\n')
    
    # Put birth event in the Network server or queue depending on what's available
    if (event.event_type == EventType.birth): 
    
        if (len(net) == 0): 
            print('Network server is free, serving event now...\n')
            net.append(event)         # Add event to the server
            
            # Schedule death event of event being served
            death_event = event
            death_event.event_type = EventType.death
            death_event.arrival_time = event.end_time
            sched.append(death_event)
            
        # Add the event to the Network queue if its server is full
        elif (len(net) > 1):
            print('Network server is busy, adding the event to the Network queue...\n')
            net.append(event)
            
    # Put death event in the Network server or queue depending on what's available
    elif (event.event_type == EventType.death):
        
        if (len(net) == 0): 
            print('Network server is free, serving event now...\n')
            net.append(event)         # Add event to the server
            
        # Add the event to the Network queue if its server is full
        elif (len(net) > 1):
            print('Network server are full, adding the event to the CPU queue...\n')
            net.append(event)
    
    if (clock > list(net)[0].arrival_time):  
        # Move first process of Network to the CPU with probability of 1.0
        e = net.pop()
        e.res = Resource.cpu
        clock += e.serv_time
        sim_cpu(clock, e, arrival_time)
    
# main() function simulates the processing of events throughout the system
def main():
    
    clock = 0     # Initialize the clock to 0
    
    # Generate the first event and put it in the schedule
    arrival_time = exponential(40)    
    serv_start = arrival_time
    serv_time = random.uniform(1, 39)
    e = Event(arrival_time, serv_start, serv_time, EventType.birth, Resource.cpu)
    sched.append(e)
    
    while (clock < 100):
        
        e1 = sched.pop()
        clock = e1.arrival_time
        
        if e1.res == Resource.cpu:
            sim_cpu(clock, e1, arrival_time)
            
        elif e1.res == Resource.disk:
            sim_disk(clock, e1, arrival_time)
            
        elif e1.res == Resource.net:
            sim_net(clock, e1, arrival_time)

sys.stdout = open('log_q3.txt', 'w')
main()
sys.stdout.flush()  
    