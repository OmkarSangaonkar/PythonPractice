# age = int(input("enter age please: "))
# simple if else

# if age > 18:
#     print("you can vote and drive")
# else:
#     print("sorry! you can not vote and drive")


# using elseif

# if age > 21:
#     print("you can vote, drive and eligible to marry")
# elif age > 18:
#     print("you can vote and drive")
# else:
#     print("sorry! you are not eligible.")


# nested if else ladder

num = int(input("enter number: "))

if num < 0:
    print("it is negetive number ")
elif num > 0:
    if num <= 100:
        print("it is positive and under 100")
    elif num > 100 and num <= 1000:
        print("it is positive and lies between 100 to 1000")
    else:
        print("it is positive and larger than 1000")

else:
    print("it is zero")
