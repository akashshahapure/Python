l1 = [1, 3, 5, 7, 9, 10]
l2 = [2, 3, 4, 5, 6, 8, 11, 12, 13]
l3 = []


i = 0
j = 0
while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        l3.append(l1[i])
        i += 1
    else:
        l3.append(l2[j])
        j += 1

l3 = l3 + l1[i:] + l2[j:]

print(l3)