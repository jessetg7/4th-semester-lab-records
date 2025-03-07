#include<stdio.h>

void main() {
    int a[20][20], n, i, j, st[20], top = -1, r[20] = {0}, tot = 1;
    printf("Enter the number of nodes: ");
    scanf("%d", &n);
    printf("Enter the adjacency matrix:\n");
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            scanf("%d", &a[i][j]);
    st[++top] = 0;
    r[0] = 1;
    while (top != -1) {
        for (j = 0; j < n; j++) {
            if (r[j] == 0 && a[st[top]][j] == 1) {
                st[++top] = j;
                r[j] = 1;
                tot++;
                break;
            }
        }
        if (j == n) top--;
    }
    if (tot == n) printf("All nodes are reachable!");
    else printf("Not all nodes are reachable!");
}
