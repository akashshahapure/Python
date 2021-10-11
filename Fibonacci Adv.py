n = int(input("Enter positive integer"))

fib = [0, 1]

if n == 0:
    print(fib[n])
elif n == 1:
    print(fib)
else:
    for i in range(2, n+1):
        fib.append(fib[i-2] + fib[i-1])
    print(fib)


