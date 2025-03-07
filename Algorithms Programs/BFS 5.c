#include<stdio.h>

void bfs(int a[20][20], int n, int start) {
    int q[20], visited[20] = {0}, st = 0, ed = 0;

    q[ed++] = start - 1;
    visited[start - 1] = 1;

    printf("Nodes reachable from %d: %d ", start, start);

    while (st < ed) {
        int node = q[st++];
        for (int i = 0; i < n; i++) {
            if (a[node][i] == 1 && !visited[i]) {
                q[ed++] = i;
                visited[i] = 1;
                printf("%d ", i + 1);
            }
        }
    }

    if (ed != n)
        printf("\nNot all nodes are reachable from %d", start);
}

int main() {
    int a[20][20], n, start;

    printf("Enter the number of nodes: ");
    scanf("%d", &n);

    printf("Enter the adjacency matrix:\n");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &a[i][j]);

    printf("Enter the start node: ");
    scanf("%d", &start);

    bfs(a, n, start);

    return 0;
}
