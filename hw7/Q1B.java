import java.util.concurrent.Semaphore;
import java.util.*;

public class Q1B extends Thread {
  
  private int id;
  private static int N = 4;
  private final Random rand = new Random();
  static volatile int[] ticket = new int[N];
  
  /*
   * Create a new process with given id
   */ 
  public Q1B(int id) {
    this.id = id;
  }
  
  /*
   * run() constitutes the main entry for thread execution
   * given by this problem (5 iterations for each thread)
   */ 
  public void run() {
    for (int k=0; k<=4; k++) {
      ticket[id] = 1;
      ticket[id] = max() + 1;
      for (int j=0; j<N; j++) {
        while(ticket[j]!=0 && (ticket[j] < ticket[id] || (ticket[j] == ticket[id] && j<id))) {};
      }
      
      delay(0, 20);
      System.out.println("Thread " + this.id + " is starting iteration " + k);
      delay(0, 20);
      System.out.println("We hold these truths to be self-evident, that all men are created equal,");
      delay(0, 20);
      System.out.println("that they are endowed by their Creator with certain unalienable Rights,");
      delay(0, 20);
      System.out.println("that among these are Life, Liberty and the pursuit of Happiness.");
      delay(0, 20);
      System.out.println("Thread " + this.id + " is done with iteration " + k + "\n");
      
      ticket[id] = 0;
    }
 
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
   * max() finds the maximum value in the ticket array
   */ 
  public int max() {
    int currentMax = ticket[0];
    for(int i=1; i<N; i++) {
      if(ticket[i] > currentMax) {
        currentMax = ticket[i];
      }
    }
    return currentMax;
  }
  
  /*
   * Spawns and runs four threads concurrently 
   */
  public static void main(String[] args) {
    final int N = 4;
    Q1B[] p = new Q1B[N];
    for (int i=0; i < N; i++) {
      p[i] = new Q1B(i);
      p[i].start();
    }
  }
  
}