votes = ["pasta","pasta","pasta","paratha","paratha","paratha"]

win = {}

for food in votes:
    if food not in win:
        win[food] = 1
    else:
        win[food] += 1

print(win)

avg = len(votes) // 2

print(avg)

for key, val in win.items():
    if val > avg:
        print(key)
        break
    elif val <= avg:
        print('NOTA')
        break