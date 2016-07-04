import java.util.concurrent.Semaphore;
import java.util.*;

public class Q3C extends Thread {
  
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
  static volatile int counter = 0;
  static volatile int[] numAccess = new int[N];
  
  /*
   * Create a new process with given id
   */ 
  public Q3C(int id) {
    this.id = id;
  }
  
  /*
   * run() constitutes the main entry for thread execution
   */ 
  public void run() {
    for(int j = 1; j <= 10; j++) {
      newWait(this.id);
      // Critical section
      System.out.println("P" + this.id + " is entering CS on iteration " + j);
      numAccess[this.id]++;
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
    counter--; 
    if(counter > 0) {
      System.out.println("P" + i + " is exiting the CS");
      int min = min();
      signal(B[min]); 
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
      wait(B[i]);  
    } 
  } 
  
  /*
   * min() finds Semaphore with the minimum number of accesses numAccess[]
   */ 
  public int min() {
    int min = numAccess[0];
    for(int i=1; i<N; i++) {
      if(numAccess[i] < min) {
        min = R[i];
      }
    }
    return min;
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
    Q3C[] p = new Q3C[N];
    for (int i=0; i < N; i++) {
      p[i] = new Q3C(i);
      p[i].start();
    }
  }

}