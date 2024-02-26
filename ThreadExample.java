class MyThread extends Thread 
{
  public MyThread(String threadName) 
  {
      super(threadName);
      start();
  }
  
  @Override
  public void run() 
  {
      try {
          for (int i = 1; i <= 5; i++) 
          {
              System.out.println(Thread.currentThread().getName() + ": Count - " + i);
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
      MyThread myThread = new MyThread("Child Thread");
      
      try {
          for (int i = 1; i <= 5; i++) 
          {
              System.out.println(Thread.currentThread().getName() + ": Count - " + i);
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
