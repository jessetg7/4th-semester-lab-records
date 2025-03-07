#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int a[20000],n,low,high,ele;

void sort(int a[], int n) {
    int i,j,temp;
    for(i=0;i<n-1;i++) {
        for(j=i+1;j<n;j++) {
            if(a[i]>a[j]) {
                temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
    }
}

int bin() {
    int mid;
    while(low<=high) {
        mid=(low+high)/2;
        if(a[mid]==ele) return mid+1;
        if(a[mid]>ele) high=mid-1;
        else low=mid+1;
    }
    return 0;
}

void main() {
    int i,temp;
    clock_t start,end;

    printf("\nEnter the number of elements: ");
    scanf("%d",&n);

    printf("\nEnter the search element: ");
    scanf("%d",&ele);

    for(i=0;i<n;i++) {
        a[i]=rand();
    }

    low=0;
    high=n-1;

    sort(a,n);

    start=clock();
    temp=bin();
    end=clock();

    if(temp) printf("\nElement found at position = %d",temp);
    else printf("\nElement not found");

    printf(" and time taken = %lf",((double)(end-start))/CLOCKS_PER_SEC);
}
