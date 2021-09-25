sides = [5, 4, 2, 1, 4, 5]


blocks = sorted(sides)

poss = []
for i in range(0, len(sides)):
    if blocks[i-len(sides)] >= blocks[i]:
        poss.append(1)
    else:
        poss.append(0)

print('Possible' if sum(poss) == len(sides) else 'Impossible')