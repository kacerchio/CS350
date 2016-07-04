Kristel Tan (ktan@bu.edu)
CAS CS350 Fundamentals of Computing Systems
Homework #7
Due: Tuesday, March 29, 2016 at 3PM

README.txt

LATE SUBMISSION

* This README file is for Problem (3d) and Problem() source code of this assignment *

Running the Program:

	- This program was run using the DrJava development environment configured to JDK 6.0_65

All Files: 

	Q3D.java -- an implementation of priority semaphore, allowing a set of processes to grab the semaphore in strict FIFO order

	Q4.java -- an implementation of priority semaphore, in which there is a fixed upper bound of "N" on the out-of-order use of the priority semaphore

Functions: 

	- run(): constitutes the main entry for thread execution given by each problem

	- signal(): used by a process when it is done with its Semaphore

	- newSignal(): used by a process when it wishes to signal the "priority Semaphore"

	- wait(): used by a process when it wishes to aquire a Semaphore

	- newWait(): used by a process when it wishes to wait on the "priority Semaphore"

	- max(): finds Semaphore with the highest priority in R[] (i.e. the "priority Semaphore")

	- min(): finds Semaphore with the minimum number of accesses numAccess[]

	- delay(): puts a process to sleep for some random time in interval given (i.e. 0-20)

	- main(): spawns and runs two threads concurrently 