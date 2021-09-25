from math import factorial

n = 6
Pr = []

for i in range(n):
    if i == n-1:
        for j in range(i + 1):
            Pr.append(factorial(i) // (factorial(i - j) * factorial(j)))



print(Pr)

