# just regular string
str1 = "hello this is simple string"
print(str1)

# you can enclose quoted sentence as below.
str2 = "hello I am outer string, 'I am inner string quoted in single quotes'"
print(str2)


# MULTILINE STRING
# This is how you can write multiline string using single quotes thrice or double qutoes thirce at opening and closing.

multiLineStr = """ Hello this is multiline string 
in this string you can write essay, poem, love letter, formal letter
informal letter, abnormal letter, kaypan letter etc etc. Means you can write anything you want which is multiline string ok.
"""

print(multiLineStr)


# STRING INDEXING
# Index always start from 0
indexStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ind0 = indexStr[0]
print(ind0)  # it will print A

# print(
#     indexStr[26]
# )  # as index starts from zero we only have 25 indexes so it will thorw error as index out of range

spacingStr = "H E L L O"
# this string have 8 indexes beacause spaces also counted as index

print(spacingStr[1], "space counted")
