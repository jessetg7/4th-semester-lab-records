#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void main() {
    int a[1000],n,i,j,item;
    clock_t start,end;

    printf("Enter the size of the array: ");
    scanf("%d",&n);

    printf("\nRandomly generated array elements are:\n");
    for(i=0;i<n;i++) {
        a[i]=rand()%100;
        printf("%d ",a[i]);
    }

    start=clock();

    for(i=1;i<n;i++) {
        item=a[i];
        j=i-1;
        while(j>=0 && a[j]>item) {
            a[j+1]=a[j];
            j--;
        }
        a[j+1]=item;
    }

    end=clock();

    printf("\nSorted list is:\n");
    for(i=0;i<n;i++) {
        printf("%d\t",a[i]);
    }

    printf("\nTime taken = %f",(double)(end-start)/CLOCKS_PER_SEC);
}
