import java.util.concurrent.Semaphore;
import java.util.*;

public class Shuttle extends Thread { 
  
  static volatile int curTerminal; 
  static volatile int nextTerminal; 
  private final Random rand = new Random();
  static volatile Semaphore N = new Semaphore(10, false); //maximum 10 permits for 10 passengers 
  private int id;
  
  // Constructor for a shuttle
  public Shuttle(int id) { 
    this.id = id;
  } 
  
  /*
   * run() constitutes the main entry for shuttle thread execution
   */ 
  public void run() {
    while(true) {
      for (int nextTerminal = curTerminal; nextTerminal < 6; nextTerminal++) {
        if (Controller.dropOffRequests[nextTerminal] > 0 || (Controller.shuttleCap <= 10 && Controller.pickUpRequests[nextTerminal] > 0)) {
          delay(0, 20);
          this.curTerminal = nextTerminal;
          wait(Controller.shuttle);
          System.out.println("Shuttle " + this.id + " arrived at Terminal " + this.curTerminal);
          
          while(Controller.dropOffRequests[this.curTerminal] > 0) { 
            wait(Controller.mutex); 
            Controller.dropOffRequests[this.curTerminal]--;
            signal(Controller.mutex); 
            signal(Controller.exitLock[this.curTerminal]); 
            wait(Controller.scMutex); 
            Controller.shuttleCap++; 
            signal(Controller.scMutex); 
          }
          
          System.out.println("Shuttle " + this.id + " is leaving Terminal " + this.curTerminal);
          
          while(Controller.shuttleCap <= 10 && Controller.pickUpRequests[this.curTerminal] > 0) {
            wait(Controller.mutex);
            Controller.pickUpRequests[this.curTerminal]--;
            signal(Controller.mutex);
            signal(Controller.enterLock[this.curTerminal]); 
            wait(Controller.scMutex); 
            Controller.shuttleCap--; 
            signal(Controller.scMutex);
          }
          signal(Controller.shuttle);
        } 
      }
      this.curTerminal = 0; 
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

}