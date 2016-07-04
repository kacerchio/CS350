Kristel Tan (ktan@bu.edu)
CAS CS350 Fundamentals of Computing Systems
Homework #4
Due: Tuesday, March 1, 2016 at 3PM

README.txt

* This README file is for Problem (2) source code of this assignment *

Running the Program:

	- This program was run using Anaconda and the Spyder Python development environment. 
	- You will need the Python math, random, statistics, sys, collections, and enum libraries to run this file
	- Used Python 3.5

All Files:

	hw4_q2.py -- Contains source code for problem 2 of this assignment

	log_2ab.txt -- Contains the monitoring event and M/M/1/K queue analysis log for a test simulation when Lambda = 50, Ts = 0.020, and simulation time = 100 and when Lambda = 50, Ts = 0.015, and simulation time = 100

	log_2c.txt -- Contains the monitoring event and M/M/1/K queue analysis log for a test simulation when Lambda = 65, Ts = 0.015, and simulation time = 100
	
	log_2d.txt -- Contains the monitoring event and M/M/1/K queue analysis log for a test simulation when Lambda = 50, Ts = 0.015, and simulation time = 100
	
	log_2e.txt -- Contains the monitoring event and M/M/1 queue analysis log for a test simulation when Lambda = 65, Ts = 0.015, and simulation time = 100

Classes: 

	- EventType: an enum class that defines the two event types (i.e. birth and death)

	- Event: an object that represents an event with the attributes of arrival time, service start time, service time, and end time

Functions: 

	- clear_trackers(): resets monitoring queue statistical trackers 

	- exponential(): returns a random value according to an exponential distribution using the built-in Python random function

	- monitor(): periodically prints statistical analysis based on the current state of the system including the mean service time, std deviation, w, and q

	- mm1k(): function handles both the controller and the simulator of an M/M/1/K system. It services births and their corresponding deaths based on the given k (queue size), lambda, and simulation time

	- md1(): handles both the controller and the simulator of an M/D/1 system. It schedules births and their corresponding deaths based on the given k (queue size), lambda, service time, and simulation time

	* Please see comments in source code for how each individual function makes calculations and runs the simulation * 