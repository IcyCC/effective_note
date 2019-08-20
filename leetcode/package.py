for (int i=1;i<=n;i++)
for (int c=0;c<=C;c++) {
       f[i][c]=f[i-1][c];
if (c>=w[i]) f[i][c] = max(f[i][c], f[i-1][c-w[i]] + v[i]); }

// 内层的for和外层的for可以互换。 for (int i=1;i<=n;i++)
for (int c=0;c<=C;c++) // 这里发生了变化——循环次序变了 if (c>=w[i]) f[c] = max(f[c], f[c-w[i]] + v[i]);