Kristel Tan (ktan@bu.edu)
CAS CS350 Fundamentals of Computing Systems
Homework #3
Due: Tuesday, February 23, 2016 at 3PM

README.txt

Running the Program:

	- This program was run using Anaconda and the Spyder Python development environment. 
	- You will need the Python math, random, and enum libraries to run this file
	- Used Python 3.5

All Files:

	hw3.py -- Contains source code for problem 2 of this assignment

	log_2a.txt -- Contains the monitoring event and M/M/1 queue analysis log for a test simulation when Lambda = 60, Ts = 0.015, and simulation time = 100

	log_2b.txt -- Contains the monitoring event and M/M/1 queue analysis log for a test simulation when Lambda = 50, Ts = 0.015, and simulation time = 100
	
	log_2c.txt -- Contains the monitoring event and M/M/1 queue analysis log for a test simulation when Lambda = 65, Ts = 0.015, and simulation time = 100
	
	log_2d.txt -- Contains the monitoring event and M/M/1 queue analysis log for a test simulation when Lambda = 65, Ts = 0.020, and simulation time = 100

	*** 

	Please note that the first few times I ran my Python code, I had no issues generating the log txt files. However, at some point it unexplainably began generating empty text files or could not create the txt file if it was not already in the directory. 

	The open() and close() statements to generate these files have been commented out for now to avoid any errors in creating the logs.  Please use a Python console to view the logged events instead. 

	***

Classes: 

	- EventType: an enum class that defines the two event types (i.e. birth and death)

	- Event: an object that represents an event with the attributes of arrival time, service start time, service time, and end time

Functions: 

	- exponential(): returns a random value according to an exponential distribution using the built-in Python random function

	- monitor(): periodically prints statistical analysis based on the current state of the system including the number of events, mean, std deviation, w, and q

	- main(): handles both the controller and the simulator of the system; schedules births and their corresponding deaths based on the given lamda, service time, and simulation time; then prints statistical analysis of the end result including the number of events, average wait time, average service time, average time in the system, q, w, and utilization 

	* Please see comments in source code for how each individual function makes calculations and runs the simulation * 