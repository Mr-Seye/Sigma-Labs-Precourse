def digitize(n):
    rev_nums = [] # initialise list
    n = str(n)[::-1] # reassign n as reversed string of input
    for i in n: # iterate through n
        rev_nums.append(int(i)) # add it to empty list and convert it back to int
    return rev_nums
