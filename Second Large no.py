input_list = [3, 1, 4, 4, 5, 5, 5, 0, 2, 2]

sor = sorted(input_list)

print(sor)

m = max(sor)

print(m)


for i in input_list:
    if i == m:
        sor.pop()

print(sor)

if len(sor)>0:
    print(sor[-1])
else:
    print('not present')