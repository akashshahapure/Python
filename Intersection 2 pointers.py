L1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
L2 = [1, 1, 2, 2, 3, 3, 4, 4]
#print(sorted(list(set(L2).intersection(set(L1)))))


p1 = 0
p2 = 0

# we will use a similar approach as we used while merging two sorted list
# we will start poit pointers at zero
# keep incrementing the pointer pointing at smaller number
# if both are same, increment both pointers and add in intersection list
intersection = []

while (p1 < len(L1)) & (p2 < len(L2)):
    if L1[p1] == L2[p2]:
        intersection.append(L1[p1])
        p1 += 1
        p2 += 1

    elif L1[p1] > L2[p2]:
        p2 += 1

    elif L1[p1] < L2[p2]:
        p1 += 1

print(intersection)