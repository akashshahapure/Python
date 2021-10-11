l1 = [1, 3, 5, 6, 10]
c = 15


l = 0
r = -1

while l>r:
    if l1[l]+l1[r] == c:
        print(l1[l], l1[r])
        break
    elif l1[l]+l1[r] < c:
        l += 1
    else:
        r -= 1