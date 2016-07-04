import java.util.concurrent.Semaphore;
import java.util.*;
import java.io.PrintWriter;
import java.io.IOException;

public class Q4 extends Thread {
  
  private int id;
  private final Random rand = new Random();
  static volatile boolean [] flag = new boolean[2];
  static volatile int turn;
  static volatile int counter = 0;
  static volatile int [] counterRec = new int[2];
  static volatile PrintWriter printWriter;
  
  /*
   * Create a new process with given id
   */ 
  public Q4(int id) {
    this.id = id;
  }
  
  /*
   * run() constitutes the main entry for thread execution
   * given by this problem
   */ 
  public void run() {
    
    for (int j=0; j<10; j++) {
      for(int k=0; k<=4; k++) {
        
        // Exit protocol for process i (Peterson's algorithm)
        flag[id]=true;
        turn = (id + 1) % 2; 
        while (flag[(id+1) % 2] && turn == ((id+1) % 2)) { 
          // Increment counter to keep track of busy-waiting
          counter++;
        }
        
        if(id == 0) {
          delay(0, 1000);
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
        System.out.println("Thread " + this.id + " is done with iteration " + k);
        
        System.out.println("Counter of Thread " + this.id + ": " + counter + "\n");
        
        // Update counter record totals for each process 
        if (id == 0) {
          counterRec[0] += counter;
        }
        if (id == 1) {
          counterRec[1] += counter;
        }
        // Reset counter
        counter = 0;
        
        // Exit protocol for process i
        flag[id] = false;
      }
      
      // Write the counter records of the two processes to a file
      if (counterRec[0] != 0) {
        double avgThread0 = counterRec[0] / 5.0;
        double avgThread1 = counterRec[1] / 5.0;
        printWriter.println("Experiment " + j);
        printWriter.println("Thread 0: " + avgThread0 + " | Thread 1: " + avgThread1 + "\n"); 
        counterRec[0] = 0;
        counterRec[1] = 0;
      }
    }
    printWriter.close();

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
   * Spawns and runs two threads concurrently 
   */
  public static void main(String[] args) throws IOException {
    printWriter = new PrintWriter("Q4-log.txt");
    final int N = 2;
    Q4[] p = new Q4[N];
    for (int i = 0; i < N; i++) {
      p[i] = new Q4(i);
      p[i].start();
    }
    
  }
}