age=int(input("Enter your age:"))
List1=["You can enter!","Go see pink floyd!","You can not enter!","Move on..."]
if (age>18):
    print(List1[0])
elif (age==18):
    print(List1[1])
else:
    print(List1[2])
print(List1[3])