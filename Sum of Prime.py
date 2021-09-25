n = 10

if n == 0:
    print(0)

elif n == 1:
    print(1)

elif n > 1:
    for i in range(2, n+1):
        for j in range(2, n):
            if i % j == 0:
                prime = i + j
    print(prime)

else:
    print("Enter positive integer")