n = 12
k = 5


# Function
def pattern(n):
    # Write your recursive function here
    if n == 0:
        print(0, end='')
    elif n < 0:
        print(n, end='')
    else:
        print(n, end=', ')
        pattern(n - k)
        print(',',n, end='')


pattern(n)
