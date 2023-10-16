# basic funcitons


def calculateGmean(a, b):
    Gmean = (a * b) / (a + b)
    print("Geomatric mean of ", a, "and", b, "is: ", Gmean)


calculateGmean(10, 20)
calculateGmean(40, 15)


# if we want to write a half function code or just defined function and planned to write it after some time then we should write "pass" inside funciton to avoid error


def planLaterFunc():
    pass


def calculateAvg(a, b):
    avg = (a + b) / 2
    print("average of ", a, "and", b, "is: ", avg)


calculateAvg(15, 25)
