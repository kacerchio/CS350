Kristel Tan (ktan@bu.edu)
CAS CS350 Fundamentals of Computing Systems
Homework #7
Due: Tuesday, March 29, 2016 at 3PM

README.txt

* This README file is for Problem(1) and Problem (3) source code of this assignment *

Running the Program:

	- This program was run using the DrJava development environment configured to JDK 6.0_65

All Files:

	Q1B.java -- an implementation of the of the an alternative Bakery algorithm defined in this problem

	Q3A.java -- a generalized implementation of priority semaphore, which initializes data structures necessary for the newWait() and newSignal functions defined in this problem  

	Q3B.java -- an implementation of priority semaphore, running 5 processes that each request the critical section 10 times and are allowed to enter based on max priority

	Q3C.java -- an implementation of priority semaphore, favoring the process that has used the critical section for the least number of times in its lifetime

Functions: 

	- run(): constitutes the main entry for thread execution given by this problem

	- signal(): used by a process when it is done with its Semaphore

	- newSignal(): used by a process when it wishes to signal the "priority Semaphore"

	- wait(): used by a process when it wishes to aquire a Semaphore

	- newWait(): used by a process when it wishes to wait on the "priority Semaphore"

	- max(): finds Semaphore with the highest priority in R[] (i.e. the "priority Semaphore")

	- min(): finds Semaphore with the minimum number of accesses numAccess[]

	- delay(): puts a process to sleep for some random time in interval given (i.e. 0-20)

	- main(): spawns and runs two threads concurrently 