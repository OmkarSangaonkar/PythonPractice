li = [10, 30, 40, 50]

l = len(li)

print("given list has ", l, "number of elements")

# slicing

fruits = ["mangos", "apples", "bananas", "guavas", "watermelons", "oranges"]
print(
    fruits[0:4]
)  # which is equivalant fruit[startindex : endindex-1]. which means it will count 0 to 3rd index

length = len(fruits)

# if we dont put start index then it will automatically take start index. same is applied for end index it will take end index automatically.

print(fruits[:5])  # starts from 0
print(fruits[1:])  # end index is len-1
print(
    "2 steping: ", fruits[0:length:2]
)  # (start:end:stepsize) it will skips 1 elements

# Negetive indexing
len1 = len(fruits)
print(fruits[1:-2])  # equivalant to fruit[1:len-2]
print(fruits[1 : len1 - 2])  # look it is printing same result

# List Comprehenssion : making list from iterable elements..  for details watch cwh 100 days of python lect 22 end 5 mins

lst = [i for i in range(10)]
print(lst)  # will genrate list of 0 to 10 elements
lst = [i for i in range(10) if i % 2 == 0]
print(lst)  # will print even numbers from 0 to 10
