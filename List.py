List1 = [1,2,'Akash',68.25]
print(List1)


List1.extend(['Family', 5,4,6])
List1.append(['Family', 5,4,6])
List1.extend('Dave Batista'.split())
List1.extend(('Roman Reigns'))
List1.append(['John Cena'])
List1.append([('Ash')])
List1.append(('No'))
Tuple1=('Tuple')
List1.append(Tuple1)
del(List1[12])
List2=List1
List1[8][3]=7

print(List2)