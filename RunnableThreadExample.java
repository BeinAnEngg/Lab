class MyRunnable implements Runnable 
{
  private String threadName;
  
  public MyRunnable(String name) 
  {
      this.threadName = name;
  }
  
  @Override
  public void run() 
  {
      try 
      {
          for (int i = 1; i <= 5; i++) 
          {
              System.out.println(threadName + ": Count - " + i);
              Thread.sleep(500);
          }
      } 
      catch (InterruptedException e) 
      {
          System.out.println(threadName + " thread interrupted.");
      }
      System.out.println(threadName + " thread exiting.");
  }
}

public class RunnableThreadExample 
{
  public static void main(String[] args) 
  {
      MyRunnable runnable1 = new MyRunnable("Thread 1");
      MyRunnable runnable2 = new MyRunnable("Thread 2");
      
      Thread thread1 = new Thread(runnable1);
      Thread thread2 = new Thread(runnable2);
      
      thread1.start();
      thread2.start();
      
      for (int i = 1; i <= 5; i++) 
      {
          System.out.println("Main Thread: Count - " + i);
          try 
          {
              Thread.sleep(500);
          } 
          catch (InterruptedException e) 
          {
              System.out.println("Main thread interrupted.");
          }
      }
      System.out.println("Main thread exiting.");
  }
}
