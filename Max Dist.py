list1 = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]

d1 = {}
for i in list1:
    if i not in d1:
        d1[i] = 1
    else:
        d1[i] = d1[i] + 1

print(d1)
d2 = dict(d1)
for key in d1.keys():
    if d1[key] > 1:
        for j in range(len(list1)):
            if key == list1[j]:
                d2[key] = j-1
print(d1)
print(d2)

cnt = max(d1.values())
print(cnt)

for key in d1:
    if d1[key] == cnt:
        print(d2[key])