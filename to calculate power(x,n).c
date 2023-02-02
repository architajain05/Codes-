#include<stdio.h>
int main(){
	int i,n,num,result=1;
	printf("Enter any number:");
	scanf("%d",&num);
	printf("\n Till which power to calculate:");      
	scanf("%d",&n);
	for(i=1;i<=n;i++)
{
	result=result*num;
}
  printf("\n pow(%d, %d)=%d",num,n, result);
	return 0;
}
