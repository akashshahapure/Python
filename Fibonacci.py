n = 10

first = 0
second = 1
f = 0

if n > 0:
    for i in range(0, n):
        print(first)
        f = first+second
        first = second
        second = f

elif n == 0:
    print(0)

else:
    print('Please enter Positive integer')