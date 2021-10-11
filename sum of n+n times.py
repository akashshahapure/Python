n = '10'

l1 = []
for i in range(1, int(n)+1):
    l1.append(n*i)

print(l1)

l2 = []

for i in l1:
    l2.append(int(i))

print(l2)

print(sum(l2))