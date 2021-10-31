def digit(number):
    numberAsString = str(number)
    firstLetter = numberAsString[0]
    lastLetter = numberAsString[-1]
    print(int(firstLetter) + int(lastLetter))

digit(1234567)