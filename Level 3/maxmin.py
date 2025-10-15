def minmax(s):
    min_max = []
    curr_min = s[0]
    curr_max = s[0]
    for i in s:
        if curr_min > i:
            curr_min = i
    min_max.append(curr_min)

    for i in s:
        if curr_max < i:
            curr_max = i
    min_max.append(curr_max)

    return min_max


# s = [2, 4, 1, 0, 2, -1]
# s = [20, 50, 12, 6, 14, 8]
s = [100, -100]
print(minmax(s))
