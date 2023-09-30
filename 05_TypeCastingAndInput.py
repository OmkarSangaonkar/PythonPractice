# m = int(input("enter number: "))
# print("m is type of : ", type(m))

m = "1547"
n = "224"
"""
this is explicit typecasting because here we are converting string to number
note that if give string is only converted when it is having only integer value

"""
x = int(m)
y = int(n)
z = x + y
print("addtion after conversion from number is: ", z)

"""
below is implicit typecasting beacause it automatically convert a number to float after addtion because it is having on float value in oprand

"""
p = 22.5
q = 587
r = p + q
print("addtion will get float value: ", r)


# inputs

intInput = int(input("eneter first input: "))
print(intInput)

floatInput = float(input("enter float input: "))
print(floatInput)

mixAdd = intInput + floatInput
print(mixAdd)

trialInput = 454
print("type: ", type(trialInput))
