 #include <stdio.h>

void main()
{
   FILE *fp;
fp = fopen("data.txt","r");
/* ASSUME THE FILE NOT EXIST */
printf("\n %d",fp);
}
