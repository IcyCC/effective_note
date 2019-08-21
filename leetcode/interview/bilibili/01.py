N = int(input())
C = int(input())
W = [int(i) for i in input().split()]
V = [int(i) for i in input().split()]

f = [[ 0 for c in range(C+1)] for i in range(N+1)]

for c in range(1, C + 1):
    for i in range(1, N+1):
        if c >= W[i-1]:
            f[i][c] = max(f[i-1][c], f[i-1][c-W[i-1]] + V[i-1])
print(f[N][C])
