#include<stdio.h>
#include<stdlib.h>

void FCFS();

int n, i, *bt, *wt, *tat, terminaltime=0;
float avgwt = 0, avgtat = 0;

int main() 
{
    int choice;
    for(;;) 
    {
        printf("\n Enter the number of processes : ");
        scanf("%d", &n);
        free(bt);
        free(wt);
        free(tat);
        bt = (int*)malloc(n*sizeof(int));
        wt = (int*)malloc(n*sizeof(int));
        tat = (int*)malloc(n*sizeof(int));
        
        printf("\n Enter the burst time for each process \n");
        for(i=0; i<n; i++){
            printf(" Burst time for P%d : ", i);
            scanf("%d", &bt[i]);
            terminaltime += bt[i];
        }
        
        FCFS();
    }
}

void FCFS() 
{
    avgwt = 0, avgtat = 0;
    wt[0] = 0;
    tat[0] = bt[0];
    for(i=1; i<n; i++) 
    {
        wt[i] = wt[i-1] + bt[i-1];
        tat[i] = wt[i] + bt[i]; 
    }
    for(i=0; i<n; i++) 
    {
        avgwt += wt[i];
        avgtat += tat[i];
    }
    avgwt = avgwt/n;
    avgtat = avgtat/n;
    printf("\n PROCESS \t BURST TIME \t WAITING TIME \t TURNAROUND TIME \n");
    printf("--------------------------------------------------------------\n");
    for(i=0; i<n; i++) 
    {
        printf(" P%d \t\t %d \t\t %d \t\t %d \n", i, bt[i], wt[i], tat[i]);
    }
    printf("\n Average Waiting Time = %f \n Average Turnaround Time = %f \n", avgwt, avgtat);
    printf("\n GAANT CHART \n");
    printf("---------------\n");
    for(i=0; i<n; i++) {
        printf(" %d\t|| P%d ||\t%d\n", wt[i], i, tat[i]);
    }
}
