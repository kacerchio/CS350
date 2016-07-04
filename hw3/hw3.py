'''

Kristel Tan (ktan@bu.edu)
CAS CS350 Spring 2016 - Professor Bestavros
hw3 - hw3.py

'''

import random 
import math
from enum import Enum  

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
# state of the system including mean, std deviation, w, and q
def monitor(s, lamda):
    
    print("\n--------------------------------")
    print("         Monitoring Event         ")
    print("--------------------------------\n")
    
    num_events = len(s)
    print("# Events = ", num_events)    
    
    serv_times = [event.serv_time for event in s]
    avg_serv_time = sum(serv_times) / len(serv_times)
    mean = 1 / avg_serv_time
    print("Mean = ", mean)
    
    var = sum([(event.serv_time - mean)**2 for event in s])
    std_dev = math.sqrt(var)
    print("Std Deviation = ", std_dev)
    
    wait_times = [event.wait_time for event in s]
    avg_wait_time = sum(wait_times) / len(wait_times)
    w = lamda * avg_wait_time
    print("w = ", w)  
    
    total_times = [event.wait_time + event.serv_time for event in s]
    avg_time_in_system = sum(total_times) / len(total_times)
    q = lamda * avg_time_in_system
    print("q = ", q)
    
# The main function handles both the controller and the simulator
# of the system. It schedules births and their corresponding deaths
# based on the given lamda, service time, and simulation time
def main(lamda, serv_time, sim_time):
    
    clock = 0           # Initialize the clock to 0
    schedule = []       # Create an empty schedule list to hold events
    
    # Initialize schedule
    arrival_time = exponential(lamda)
    serv_start = arrival_time
    schedule.append(Event(arrival_time, serv_start, serv_time, EventType.birth))
    
    
    # Begin simulation
    while(clock < sim_time):

        current_event = schedule[0]     # Store 1st item in schedule as the current event
        
        # If the current event is a death, remove it from the schedule
        if (current_event.event_type == EventType.death):
            schedule.remove(current_event)
        
        # Generate a random arrival time for next event
        arrival_time += exponential(lamda)
        # If the arrival time is before the end time of the last event, 
        # change the service start time to the end time of the last event
        serv_start = max(arrival_time, schedule[-1].end_time)
        # Create a new birth event with the updated attributes
        new_event = Event(arrival_time, serv_start, serv_time, EventType.birth)
        # Place the new event at the end of the schedule
        schedule.append(new_event)
    
        # Schedule and initialize the death of the current event
        death_event = current_event
        death_event.event_type = EventType.death
        death_event.serv_start = current_event.end_time
        # Place the death right after the current event's arrival
        schedule.insert(1, death_event)
        
        # Do a monitor check on the system
        monitor_check = random.choice([0, 1])
        if (monitor_check == 1):
            monitor(schedule, lamda)
        
        clock = arrival_time         # Increment clock
            
    # Generate statistical analysis for M/M/1 queue
            
    num_events = len(schedule)
    
    wait_times = [event.wait_time for event in schedule]
    avg_wait_time = sum(wait_times) / len(wait_times)
    w = lamda * avg_wait_time
    
    serv_times = [event.serv_time for event in schedule]
    avg_serv_time = sum(serv_times) / len(serv_times)
    
    total_times = [event.wait_time + event.serv_time for event in schedule]
    avg_time_in_system = sum(total_times) / len(total_times)
    q = lamda * avg_time_in_system
 
    util = sum(serv_times) / clock

    print("\n--------------------------------")
    print("      M/M/1 Queue Analysis        ")
    print("--------------------------------\n")
    print("Total # events = ", num_events, "\n")
    print("Avg Tw = ", avg_wait_time)
    print("Avg Ts = ", avg_serv_time)
    print("Avg Tq = ", avg_time_in_system, "\n")
    print("q = ", q)
    print("w = ", w)
    print("p = ", util)

# Write to four different log files for parts a - d of this problem 

#f1 = open('log_2a.txt', 'w') 
main(60, 0.015, 100)
p1 = 60 * 0.015
q1 = p1 / (1 - p1)
tw1 = (q1 / 60) - 0.015
w1 = tw1 * 60
print("\n--------------------------------")
print(" M/M/1 Queue Analytical Analysis  ")
print("--------------------------------\n")
print("Avg Tw = ", tw1)
print("Avg Ts = ", 0.015)
print("Avg Tq = ", q1 / 60, "\n")
print("q = ", q1)
print("w = ", w1)
print("p = ", p1)
#f1.close()

#f2 = open('log_2b.txt') 
main(50, 0.015, 100)
p2 = 50 * 0.015
q2 = p2 / (1 - p2)
tw2 = (q2 / 50) - 0.015
w2 = tw2 * 50
print("\n--------------------------------")
print(" M/M/1 Queue Analytical Analysis  ")
print("--------------------------------\n")
print("Avg Tw = ", tw2)
print("Avg Ts = ", 0.015)
print("Avg Tq = ", q2 / 50, "\n")
print("q = ", q2)
print("w = ", w2)
print("p = ", p2)
#f2.close()

#f3 = open('log_2c.txt') 
main(65, 0.015, 100)
p3 = 65 * 0.015
q3 = p3 / (1 - p3)
tw3 = (q3 / 65) - 0.015
w3 = tw3 * 65
print("\n--------------------------------")
print(" M/M/1 Queue Analytical Analysis  ")
print("--------------------------------\n")
print("Avg Tw = ", tw3)
print("Avg Ts = ", 0.015)
print("Avg Tq = ", q3 / 65, "\n")
print("q = ", q3)
print("w = ", w3)
print("p = ", p3)
#f3.close()

#f4 = open('log_2d.txt') 
main(65, 0.020, 100)
p4 = 65 * 0.020
q4 = p4 / (1 - p4)
tw4 = (q4 / 65) - 0.020
w4 = tw4 * 65
print("\n--------------------------------")
print(" M/M/1 Queue Analytical Analysis  ")
print("--------------------------------\n")
print("Avg Tw = ", tw4)
print("Avg Ts = ", 0.020)
print("Avg Tq = ", q4 / 65, "\n")
print("q = ", q4)
print("w = ", w4)
print("p = ", p4)
#f4.close()