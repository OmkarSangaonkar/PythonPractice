s1 = "mangos"

l = len(s1)

print(s1, "is", l, "charactors word")

# slicing

fruit = "strawberry"
print(
    fruit[0:4]
)  # which is equivalant fruit[startindex : endindex-1]. which means it will count 0 to 3rd index

# if we dont put start index then it will automatically take start index. same is applied for end index it will take end index automatically.

print(fruit[:5])  # starts from 0
print(fruit[1:])  # end index is len-1

# Negetive indexing
len1 = len(fruit)
print(fruit[1:-2])  # equivalant to fruit[1:len-2]
print(fruit[1 : len1 - 2])  # look it is printing same result
