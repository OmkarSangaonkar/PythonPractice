# default arguments: if we dont pass value it will take its default value as we passed this value in function argument


# def average(a=1, b=1):
#     avg = (a + b) / 2
#     print(avg)


# average(3, 50)
# average(3)  # here it take b's default value
# average()  # here it take both default value

# # keyword argument : we can give argument in any order by following way
# average(b=80, a=54)


""" Variable length argument: its same as rest paramters in JS but here it has two types, one is tuple which is denoted as (*args) and second is list which is denoted as (**args) <= which same in js. So basically we can pass as many arguments in function and make operations on them.
"""


# using tuples (*args)
# def sumOfNums(*args):
#     add = 0
#     for i in args:
#         add = add + i
#     print("addition of given", len(args), "numbers is", add)


# sumOfNums(10, 20, 30, 40)


# def averageOfNums(*nums):
#     sum = 0
#     for i in nums:
#         sum = sum + i

#     avg = sum / len(nums)
#     print("Average of given", len(nums), "numbers is", avg)


# averageOfNums(10, 20, 30, 40, 50)
