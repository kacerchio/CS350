import java.util.concurrent.Semaphore;
import java.util.*;

public class Passenger extends Thread { 
  
  private final Random rand = new Random();
  private int id;  // ID for a passenger
  private int st;  // Start terminal for a passenger
  private int dt;  // Destination terminal for a passenger
  
  // Constructor for a passenger
  public Passenger(int id, int st, int dt) {
    this.id = id;
    this.st = st;
    this. dt = dt;
  }
  
  /*
   * run() constitutes the main entry for thread execution
   */ 
  public void run() {
    
    while(true) {
      
      wait(Controller.mutex);
      Controller.pickUpRequests[this.st]++;
      System.out.println("Passenger " + this.id + " is waiting for the shuttle at terminal " + this.st);
      signal(Controller.mutex); 
      
      wait(Controller.enterLock[this.st]);
      System.out.println("Passenger " + this.id + " is entering the shuttle at terminal " + this.st); 
      
      wait(Controller.mutex);
      Controller.dropOffRequests[this.dt]++; 
      System.out.println("Passenger " + this.id + " is on the shuttle en route to terminal " + this.dt);
      signal(Controller.mutex); 
      
      wait(Controller.exitLock[this.dt]); 
      System.out.println("Passenger " + this.id + " is exiting the shuttle at terminal " + this.dt); 
      dt = destTerminal(this.st); 
      
    }
  }
  
  /*
   * signal() is used by a process when it is finished with its Semaphore
   */ 
  public void signal(Semaphore s) {
    s.release();
  }
  
  /*
   * wait() is used by a passenger when it wishes to aquire a Semaphore
   */ 
  public void wait(Semaphore s) {
    try{
      s.acquire();
    }
    catch(InterruptedException e) { }
  }
  
  /*
   * delay() puts the process to sleep for some random time in interval given (i.e. 0-20)
   */ 
  public void delay(int min, int max) {
    try {
      int randomTime = rand.nextInt((max - min) + 1) + min;
      sleep(randomTime);
    } 
    catch (InterruptedException e) { }
  }
  
  /*
   * startTerminal() returns a random integer between 1 and 6
   * to select as a starting terminal for a passenger
   */ 
  public static int startTerminal() { 
    return (int)(Math.random() * 6); 
  }
  
  /*
   * destTerminal() returns a random integer between 1 and 6
   * to select as a destination terminal for a passenger
   */ 
  public static int destTerminal(int st) {
    int dt = (int)(Math.random() * 6);
    while (dt == st) {
      dt = (int)(Math.random() * 6);
    }
    return dt;
  }
  
}