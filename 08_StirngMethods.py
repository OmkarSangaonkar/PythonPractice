s1 = "!!!!Stringify!! !!Stringify"

# prints length
print(len(s1))

# uppercase conversion
print(s1.upper())

# lowercase conversion
print(s1.lower())

# removing mentioned charators if it is present at start of sentence
print(s1.strip("!"))

# removing mentioned charactors if it is present at end of sentence
print(s1.rstrip("!"))

# replacing word
print(s1.replace("Stringify", "Verify"))

# spliting words into list which have spaces if we put str.split(" ")
print(s1.split(" "))

# if we put any charactor then it will split that word with that charactor
print(s1.split("!"))  # it will split with !

# Capitalize first charactor of sentense and make other charactors lower case
demoStr = """this is demo Sentnce in which t at start will get uppercase.
 and S of sentence get lower case if there is any other charactor which is uppercase in sentence that also converted to lower case"""
print(demoStr.capitalize())

# centering the sentences

str2 = "this need to go center by 50"
print(len(str2))
print(str2.center(50))
print(len(str2.center(50)))

# counting word or chactor. And it is case sensetive
print(s1.count("!"))
print(s1.count("tr"))

# endswith ==> it will return true or false if given char present at end or not

print(s1.endswith("fy"))

print(
    s1.endswith("!!", 0, 15)
)  # it will slice string from zero to 15 and check at 15 it is ended with double exclamation mark

# find method
# it will return index of first occurance of word and if not found then return -1
print(demoStr.find("to"))

# iselnum to find wheather string has a to z, A to Z, or numbers present
x = "str123"
print(x.isalnum())

# isAlpha to find only it has charactors
y = "isAlpha1231"
print(y.isalpha())


# NOTE :: THERE ARE MANY MORE BUILT IN METHODS. TO SEE IT WATCH HARRYS 13TH VIDEO OF 100 DAYS OF CODE
