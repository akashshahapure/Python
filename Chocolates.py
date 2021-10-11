#Sanjay has m rupees, each chocolate costs c rupees, shopkeeper will give away k chocolates for w wrappers.
#Can you find now how many chocolates Sanjay will be able to eat?

m = 15
c = 2
w = 3
k = 2


choc = m // c
wr = m // c

while wr // w != 0:
    choc = choc + (wr // w * k)
    wr = (wr // w * k) + wr % w

print(choc)