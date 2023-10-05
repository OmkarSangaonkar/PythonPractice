import time

timeStamp = time.strftime("%H:%M:%S")

hr = int(time.strftime("%H"))
# print(type(hr))
# mi = int(time.strftime("%M"))
# sec = int(time.strftime("%S"))

if (hr >= 6) and (hr < 12):
    print("Good Morning")
elif hr >= 12 and hr < 17:
    print("Good Afternoon")
elif hr >= 17 and hr <= 20:
    print("Good Evening")
else:
    print("Good Night")
