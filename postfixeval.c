//  EVALUATION OF POSTFIX EXPRESSION
#include<stdio.h> 
#include<ctype.h>
#include<math.h>

#define MAX 20

void push(int e); 
int pop();

int a[MAX], top = -1;

int main(void)
{
    char post[MAX], ch;
    int i, op1, op2, result;

    printf("Program to evaluate postfix expression\n");
    printf("Enter the postfix expression: ");
    scanf("%s", post);
    
    for (i = 0; post[i] != '\0'; i++)
    {
        ch = post[i]; 
        if (isdigit(ch)) 
            push(ch - '0');
        else
        {
           
            op2 = pop();
            op1 = pop();
            switch (ch) 
            {
              case '+':result = op1 + op2;
                  break;
              case '-':result = op1 - op2;
                  break;
              case '*':result = op1 * op2;
                  break;
              case '/':result = op1 / op2;
                  break;
              case '^':result = pow(op1, op2);
                  break;
              case '%':result = op1 % op2;
                  break;
              default:
                  printf("Invalid character\n");
            }
            push(result);
        }
    }
    printf("Result of the above expression is %d\n", pop());
}

void push(int e)
{
    ++top;
    a[top] = e;
}

int pop()
{
    int ele;
    ele = a[top];
    --top;
    return (ele);
}
