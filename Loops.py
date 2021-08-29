#This code will print ratings greater than 6
PlayListRatings = [[6,7,8],10, 9.5, 10,[8,5,10], 8, 7.5, 5, 10, 10]
int1=type(PlayListRatings[1])
flt=type(PlayListRatings[2])
list2=type(PlayListRatings[0])
i = 0
N=range(len(PlayListRatings))
for i in N:
    j = 0
    if (type(PlayListRatings[i]) != int1 and type(PlayListRatings[i]) != flt):
        while (j<len(PlayListRatings[i]) and PlayListRatings[i][j]>=6):
            print(PlayListRatings[i][j])
            j=j+1
    elif (type(PlayListRatings[i] != list2) and PlayListRatings[i]>=0):
        print(PlayListRatings[i])