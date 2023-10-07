# it is basically switch statement in other languages

i = int(input("enter value :"))

match i:
    case 1:
        print("you are number 1")
    case 2:
        print("you are number 2")
    case 3:
        print("you are number 3")
    case 4:
        print("you are number 4")
    case _:
        print("you are unknown number")
