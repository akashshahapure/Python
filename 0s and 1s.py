# Program to sort a list of 0s and 1s in one traversal of the list

# Given list of 0s and 1s
v = [0, 2, 0, 0, 1, 1, 2, 0, 1]
n = len(v)
# Initialise two variables 'i' and 'j' to 1, indicating that they are currently pointing at the
# first element in the list.
i = 0
j = 0

# Run a loop from 1 to the length of the list, with the variable 'i'
for i in range(n):

    # If you encounter a zero, swap the values between v[i] & v[j] and increment 'j' as well. 'i'
    # anyway gets incremented with every iteration of the loop. Think about it. This way, 'j' will
    # always point at the first '1' that hasn't been sorted. Swapping the value of v[i]
    # and v[j] will help replace the 1s with 0s that come after it. If v[j] is pointing at zero,
    # swapping won't matter anyway.
    if (v[i] == 0):
        temp = v[j]
        v[j] = v[i]
        v[i] = temp
        j = j + 1

# Print the sorted list
print(v)