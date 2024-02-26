class MyThread extends Thread 
{
  public MyThread(String threadName) 
  {
      // Call the base class constructor
      super(threadName);
      // Start the thread
      start();
  }
  
  @Override
  public void run() 
  {
      try {
          for (int i = 1; i <= 5; i++) 
          {
              System.out.println(Thread.currentThread().getName() + ": Count - " + i);
              // Sleep for 500 milliseconds
              Thread.sleep(500);
          }
      } 
      catch (InterruptedException e) 
      {
          System.out.println(Thread.currentThread().getName() + " thread interrupted.");
      }
      
      System.out.println(Thread.currentThread().getName() + " thread exiting.");
  }
}

public class ThreadExample 
{
  public static void main(String[] args) 
  {
      // Create an instance of MyThread
      MyThread myThread = new MyThread("Child Thread");
      
      // Main thread
      try {
          for (int i = 1; i <= 5; i++) 
          {
              System.out.println(Thread.currentThread().getName() + ": Count - " + i);
              // Sleep for 500 milliseconds
              Thread.sleep(500);
          }
      } 
      catch (InterruptedException e) 
      {
          System.out.println(Thread.currentThread().getName() + " thread interrupted.");
      }
      
      System.out.println(Thread.currentThread().getName() + " thread exiting.");
  }
}
