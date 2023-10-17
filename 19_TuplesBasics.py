tup = (10, 20, 30, 40)
print(type(tup))

# if only one element in tuple then use , after that element
ex = (10,)  # like this
print(ex)

sl = tup[0:3]  # tuples are immutable means you cant change orignal tuple
print(sl)

# slicing

fruits = ("mangos", "apples", "bananas", "guavas", "watermelons", "oranges")
fr = fruits[0:4]
print(
    fr
)  # which is equivalant fruit[startindex : endindex-1]. which means it will count 0 to 3rd index

length = len(fruits)

# if we dont put start index then it will automatically take start index. same is applied for end index it will take end index automatically.
z = fruits[:5]
print(z)  # starts from 0

st = fruits[1:]
print(st)  # end index is len-1

steping = fruits[0:length:2]
print("2 steping: ", steping)  # (start:end:stepsize) it will skips 1 elements

# Negetive indexing
len1 = len(fruits)
# neg = fruits[1:-2]  # equivalant to fruit[1:len-2]
# print(neg)
print(fruits[1 : len1 - 2])  # look it is printing same result
print(fruits)  # see after slicing and all we get same orignal tuple


"""
NOTE: YOU CAN CHANGE TUPLE BY CHANGING IT INTO LIST.
AND THEN YOU CAN PERFORM ALL OPERATIONS OF LIST. 
"""
tx1 = (10, 20, 30, 40)
li = list(tx1)
print(type(li))
li.sort(reverse=True)
print(li)
print(tuple(li))  # again reversed to tuple

tx2 = (45, 54, 25, 30, 12, 78, 25, 92, 31, 24, 12, 24)
tx3 = tx1 + tx2  # concat tuples and store it into new tuple
print(tx3)

# finding index of number
print(tx2.index(25))
idx = tx2.index(25, 3, 8)  # index(number, startIndex, endIndex)
print(idx)
