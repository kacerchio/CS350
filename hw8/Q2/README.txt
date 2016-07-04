Kristel Tan (ktan@bu.edu)
CAS CS350 Fundamentals of Computing Systems
Homework #8
Due: Thursday, April 7, 2016 at 3PM

README.txt

* This README file is for Problem(2) *

Running the Program:

	- This program was run using the DrJava development environment configured to JDK 6.0_65

All Files:

	Controller.java -- defines the Java Controller class for the shuttle system and runs the main function for the simulation of 50 passengers

	Passenger.java -- defines the Java Passenger class for an individual looking to board the shuttle from a starting terminal to a destination terminal 

	Shuttle.java -- defines the Java Shuttle class to hold Passengers and transport them to their destinations from their starting terminal

	Q2-Sample-Output -- a text file of some output from the console (protocol runs forever, so you will need to perform a keyboard interrupt to view the console's output when running the program live)

Functions:

	Controller.java 

		startTerminal(): returns a random integer between 1 and 6 to select as a starting terminal for a passenger
		destTerminal(): returns a random integer between 1 and 6 to select as a destination terminal for a passenger
		main(): spawns and runs 50 passengers concurrently with one shuttle in the system

	Passenger.java

		run(): constitutes the main entry for passenger thread execution
		signal(): used by a process when it is finished with its Semaphore
		wait(): used by a passenger when it wishes to aquire a Semaphore
		delay(): puts a process to sleep for some random time in interval given (i.e. 0-20)
		startTerminal(): returns a random integer between 1 and 6 to select as a starting terminal for a passenger
		destTerminal(): returns a random integer between 1 and 6 to select as a destination terminal for a passenger

	Shuttle.java

		run(): constitutes the main entry for shuttle thread execution
		signal(): used by a process when it is finished with its Semaphore
		wait(): used by a passenger when it wishes to aquire a Semaphore
		delay(): puts a process to sleep for some random time in interval given (i.e. 0-20)