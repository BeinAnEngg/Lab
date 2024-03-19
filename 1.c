#include <stdio.h>
#include <stdlib.h>

struct day {
    char *dname;
    int date;
    char *activity;
};

struct day *cal;

void create();
void read();
void display();

int main() {
    create();
    read();
    display();
    return 0;
}

void create() {
    int i;
    cal = (struct day *)malloc(7 * sizeof(struct day));
    for (i = 0; i < 7; i++) {
        cal[i].dname = (char *)malloc(20 * sizeof(char));
        cal[i].activity = (char *)malloc(70 * sizeof(char));
    }
}

void read() {
    int i;
    printf("Enter the weekly calendar details:\n");
    for (i = 0; i < 7; i++) {
        printf("Enter Day Name: ");
        scanf(" %[^\n]", cal[i].dname);
        printf("Enter Date: ");
        scanf("%d", &cal[i].date);
        printf("Enter Activity: ");
        scanf(" %[^\n]", cal[i].activity);
    }
}

void display() {
    int i;
    printf("The details of the weekly calendar are:\n");
    printf("\n DayName\t\t Date\t\t Activity\n");
    for (i = 0; i < 7; i++) {
        printf("%-15s\t %d\t\t %s\n", cal[i].dname, cal[i].date, cal[i].activity);
    }
}
