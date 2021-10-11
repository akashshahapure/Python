input_dict = {'Fruit': 1, 'Vegetable': {'Cabbage': 2, 'Cauliflower': 3}, 'Spices': 4}


def flatten_dict(dd, separator ='_', prefix =''):
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dd.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dd, dict) else { prefix : dd }


out1=list(flatten_dict(input_dict).keys())
out2=list(flatten_dict(input_dict).values())
out1.sort()
out2.sort()
print(out1)
print(out2)