#include<stdio.h>
#include<string.h>

int main()
{
    char STR[100],PAT[100],REP[100],ans[200];
    int i,j,m,c,k,flag=0;

    printf("Enter MAIN String\n");
    fgets(STR,sizeof(STR),stdin);
    STR[strcspn(STR, "\n")]='\0';

    printf("Enter PATTERN String\n");
    fgets(PAT,sizeof(PAT),stdin);
    PAT[strcspn(PAT, "\n")]='\0';

    printf("Enter REPLACEMENT String\n");
    fgets(REP,sizeof(REP),stdin);
    REP[strcspn(REP, "\n")]='\0';

    i=j=c=m=0;

    while (STR[c] != '\0')
    {
        if (STR[m] == PAT[i])
        {
            m++;
            i++;
            flag=1;
            if(PAT[i] == '\0')
            {
                for (k = 0; REP[k] !='\0'; k++,j++)
                    ans[j]=REP[k];

                i=0;
                c=m;
            }
        }
        else
        {
            ans[j]=STR[c];
            j++;
            c++;
            m=c;
            i=0;
        }
    }
    if(flag == 0)
    {
        printf("Pattern not found.\n");
    }
    else
    {
        ans[j] = '\0';
        printf("The Resultant String is\n%s",ans);
    }
}
