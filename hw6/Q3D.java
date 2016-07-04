import java.util.concurrent.Semaphore;
import java.util.*;

public class Q3D extends Thread {
  
  private int id;
  private final Random rand = new Random();
  static volatile boolean [] flag = new boolean[2];
  static volatile int turn;
  
  /*
   * Create a new process with given id
   */ 
  public Q3D(int id) {
    this.id = id;
  }
  
  /*
   * run() constitutes the main entry for thread execution
   * given by this problem
   */ 
  public void run() {
    
    for(int k=0; k<=4; k++) {
      
      // Exit protocol for process i (Peterson's algorithm)
      flag[id] = true;
      turn = (id + 1) % 2; 
      while (flag[(id + 1) % 2] && turn == ((id + 1) % 2)) { };
      
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
      System.out.println("Thread " + this.id + " is done with iteration " + k + "\n");
      
      // Exit protocol for process i
      flag[id] = false;
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
   * Spawns and runs two threads concurrently 
   */
  public static void main(String[] args) {
    final int N = 2;
    Q3D[] p = new Q3D[N];
    for (int i = 0; i < N; i++) {
      p[i] = new Q3D(i);
      p[i].start();
    }
  }
  
}