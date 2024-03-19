#include<stdio.h>
#include<stdlib.h>

# define S 5

int top=-1;
int stack[S];

void push();
void pop();
void display();

int main(void)
{
  int n;
  while (1)
  {
    
  
  printf("Stack operations");
  printf("\n1.PUSH\n2.POP\n3.DISPLAY\n4.EXIT\n");
  printf("Enter Choice:");
  scanf("%d",&n);

  switch (n)
  {
  case 1:
    push();
    break;
  case 2:
    pop();
    break;
  case 3:
    display();
    break;
  case 4:
    exit(0);
    break;  
  
  default:
    printf("Invalid Input.\n");
    break;
  }
  }
  return 0;
}
void push()
{
  if(top ==S-1)
  {
    printf("Stack Overflow\n");
  }
  else
  {
    int item;
    printf("Enter element into the stack:");
    scanf("%d",&item);
    stack[++top]=item;
    printf("Element added to stack is %d\n",item);
  }
}
void pop()
{
  if(top==-1)
  {
    printf("Stack Underflow.");
  }
  else
  {
    printf("Popped element is %d",stack[top--]);
  }
}
void display()
{
  if(top==-1)
  {
    printf("Stack Underflow.");
  }
  else
  {
    for(int i=top;i>=0;--i)
    printf("%d\n",stack[i]);
  }
}
