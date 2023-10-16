nums = [50, 24, 57, 5, 32, 35, 98, 45, 15, 5, 5]
print(nums)
nums.sort()
print(nums)

# reverse sort
nums.sort(reverse=True)
print(nums)

# reverse list
nums.reverse()
print(nums)

# find index of given number
i = nums.index(98)  # will find first occurance numbers index in case of duplicates
print(i)

# count the number in list
cnt = nums.count(5)
print("given number is occured", cnt, "times in list")

""" copy list: if we assign list to new variable and change the value of that
 list then same changes occurs in orignal list. to avoid this there is method 
 in python called copy """

numsCopy = nums.copy()
# before change
print("ORG", nums)
print("COPY", numsCopy, "\n")

numsCopy[0] = 10

# after change
print("ORG", nums)
print("COPY", numsCopy)


# insert: it will insert new value at particular index insert(index, newValue)

nums.insert(1, 500)
print(nums)

# extend: it will simply joint two list one list append to other
# ex list1.extend(list2).. here list2 append at list1
li = [4520, 877, 356, 988]
nums.extend(li)
print(nums)
