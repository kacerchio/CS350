import java.util.concurrent.Semaphore;
import java.util.*;

public class Q4 extends Thread {
  
  private int id;
  private static int N = 5;
  private final Random rand = new Random();
  static volatile Semaphore [] B = new Semaphore [N];
  static {
    for(int i = 0; i < N; i++) {
      B[i] = new Semaphore(0, false);
    }   
  }
  static volatile int[] R = new int[N];
  static volatile LinkedList<Integer> queue = new LinkedList<Integer>();
  static volatile int counter = 0;
  static volatile int bound = 0;
  
  /*
   * Create a new process with given id
   */ 
  public Q4(int id) {
    this.id = id;
  }
  
  /*
   * run() constitutes the main entry for thread execution in which there is a 
   * fixed upper bound of "N" on the out-of-order use of the priority semaphore
   */ 
  public void run() {
    for (int j = 1; j < 10; j++) {
      // P0 requests the critical section at a slower rate
      if (this.id == 0) {
        delay(0, 20);
      }
      newWait(this.id);
      // Critical section
      System.out.println("P" + this.id + " is entering CS on iteration " + j);
      delay(0, 20);
      newSignal(this.id);
    }
  }
  
  /*
   * signal() is used by a process when it is done with its Semaphore
   */ 
  public void signal(Semaphore B) {
    B.release();
  }
  
  /*
   * newSignal() is used by a process when it wishes to signal 
   * the "priority Semaphore"
   */
  public void newSignal(int i) { 
    // Decrease the bound P0 has just requested the CS
    if (i == 0) {
      bound--;
    }
    R[i] = 0;
    counter--; 
    if(counter > 0) {
      System.out.println("P" + i + " is exiting the CS");
      int max = max();
      Integer head = queue.poll();
      if(head.intValue() == 0 && max != 0) { 
        bound++; 
      } 
      // If upper N-bound has been reached, signal B[0] and decrease the bound variable
      if(bound == 2) { 
        signal(B[0]); 
        bound--;
      } 
      // Signal next process in the queue if upper N-bound has not been reached
      else { 
        signal(B[head]); 
      } 
    } 
  } 
  
  /*
   * wait() is used by a process when it wishes to aquire a Semaphore
   */ 
  public void wait(Semaphore B){
    try {
      B.acquire();
    }
    catch(InterruptedException e) {
    }
  }
  
  /*
   * newWait() is used by a process when it wishes to wait on 
   * the "priority Semaphore"
   */
  public void newWait(int i) {
    System.out.println("P" + i + " is requesting CS");
    R[i] = i;  
    counter++; 
    if (counter > 1){ 
      queue.add(new Integer(i));
      wait(B[i]);  
    } 
  } 
  
  /*
   * max() finds Semaphore with the highest priority in R[]
   * (i.e. the "priority Semaphore")
   */ 
  public int max() {
    int maxPriority = R[0];
    for(int i=1; i<N; i++) {
      if(R[i] > maxPriority) {
        maxPriority = R[i];
      }
    }
    return maxPriority;
  }
  
  /*
   * delay() puts the process to sleep for some
   * random time in interval given (i.e. 0-20)
   */ 
  public void delay(int min, int max) {
    try {
      int randomTime = rand.nextInt((max - min) + 1) + min;
      sleep(randomTime);
    } 
    catch (InterruptedException e) { }
  }
  
  /*
   * Spawns and runs N threads concurrently 
   */
  public static void main(String[] args) {
    final int N = 5;
    Q4[] p = new Q4[N];
    for (int i = 0; i < N; i++) {
      p[i] = new Q4(i);
      p[i].start();
    }
  }

}