m = 4
n = 5

final = [0]*n

final2 = [final[:] for i in range(m)]
for i in final2:
    print(i)

print("\n")

for i in range(m):
    for j in range(n):
        if i==0 or j==0 or i==m-1 or j==n-1:
            final2[i][j] = 1

for i in final2:
    print(i)
