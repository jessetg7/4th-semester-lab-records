#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int a[20000],ele,pos;

int lin() {
    if(pos<0) return pos+1;
    if(a[pos]==ele) return pos+1;
    pos--;
    return lin();
}

void main() {
    int n,temp,i;
    clock_t start,end;

    printf("\nEnter the number of elements: ");
    scanf("%d",&n);

    printf("\nEnter the search element: ");
    scanf("%d",&ele);

    for(i=0;i<n;i++) {
        a[i]=rand();
    }

    pos=n-1;
    start=clock();
    temp=lin();
    end=clock();

    printf("\nElement found at position = %d and time taken = %lf",temp,((double)(end-start))/CLOCKS_PER_SEC);
}
