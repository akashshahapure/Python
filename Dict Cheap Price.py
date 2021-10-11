dict1 = {'mobile1':10000, 'mobile2':11000, 'mobile3':13000, 'mobile4':9000, 'mobile5':15000, 'mobile6':16000, 'mobile7':17000, 'mobile8':18000, 'mobile9':19000}

cheap = min(dict1.values())

for key, val in dict1.items():
    if val == cheap:
        print(key+':',val)