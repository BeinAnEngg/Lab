#include<stdio.h>
#include<stdlib.h>
#define SIZE 6

int front=0,rear=-1,count=0;
char cqueue[SIZE];

void insert();
void delete();
void display();

int main(void)
{
  int n;
  
  
  printf("CIRCULAR QUEUE\n");
  printf("1.Insert\n2.Delete\n3.Display\n4.Exit\n");
  printf("Enter choice:");
  scanf("%d",&n);

  switch (n)
  {
  case 1:insert();
    break;
  case 2:delete();
    break;
  case 3:display();
    break;
  case 4:exit(0);

  default:
  printf("Invalid Input.");
    break;
  }
  
}
void insert()
{
  char item;
  if(count>=SIZE)
  {
    printf("Queue overflow.\n");
  }
  else
  {
    printf("Enter the element to Be inserted: ");
    scanf(" %c",&item);
    rear=(rear+1)%SIZE;
    cqueue[rear]=item;
    count++;
  }
  main();
}
void delete()
{
  char d;
  if(count<=0)
  {
    printf("Queue underflow");
  }
  else
  {
    d=cqueue[front];
    front=(front+1)%SIZE;
    printf("Deleted element %c",d);
    count--; 
  }
}
void display()
{
  printf("The elements in the queue are:");
  for(int i=0;i<=count;i++)
  {
    printf(" %c",cqueue[(front+i)%SIZE]);
  }
}
