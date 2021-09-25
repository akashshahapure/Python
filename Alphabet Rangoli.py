n=5

width = n * 4 - 3
mystring = ''

for i in range(1, n + 1):
    for j in range(0, i):
        mystring += chr(96 + n - j)
        if len(mystring) < width:
            mystring += '-'
    for k in range(i-1, 0, -1):
        mystring += chr(97 + n - k)
        if len(mystring) < width:
            mystring += '-'
    print(mystring.center(width, '-'))
    mystring = ''

for i in range(n - 1, 0, -1):
    mystring = ''
    for j in range(0, i):
        mystring += chr(96 + n - j)
        if len(mystring) < width:
            mystring += '-'
    for k in range(i-1, 0, -1):
        mystring += chr(97 + n - k)
        if len(mystring) < width:
            mystring += '-'
    print(mystring.center(width, '-'))