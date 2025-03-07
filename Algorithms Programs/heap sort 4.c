#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void heapify(int a[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && a[left] > a[largest])
        largest = left;
    if (right < n && a[right] > a[largest])
        largest = right;

    if (largest != i) {
        int temp = a[i];
        a[i] = a[largest];
        a[largest] = temp;
        heapify(a, n, largest);
    }
}

void heapSort(int a[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(a, n, i);

    for (int i = n - 1; i > 0; i--) {
        int temp = a[0];
        a[0] = a[i];
        a[i] = temp;
        heapify(a, i, 0);
    }
}

int main() {
    int n, i;
    clock_t start, end;

    printf("Enter the value of n: ");
    scanf("%d", &n);
    int a[n];

    for (i = 0; i < n; i++)
        a[i] = n - i;

    start = clock();
    heapSort(a, n);
    end = clock();

    printf("\nSorted array:\n");
    for (i = 0; i < n; i++)
        printf("%d ", a[i]);

    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("\nTime taken: %lf seconds\n", time_taken);

    return 0;
}
