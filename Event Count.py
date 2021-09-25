

events = [[23, 29], [12,22], [22, 22], [1, 12], [29,31], [12,18]]
wedding = 22
eve_cnt = 0

for i in events:
    if i[0] <= wedding and i[1] >= wedding:
        eve_cnt += 1

#eve_cnt = sum(list(1 for i in range(0, len(events)) if min(events[i]) >= wedding and wedding <= max(events[i])))

print(eve_cnt)
print(min(events[1]), max(events[1]))