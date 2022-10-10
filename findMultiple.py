

number = int(input("enter the number here"))



def findmultiple(number):
    count = 0
    for i in range(number):
        if (i % 3 == 0) or (i % 5 == 0):
            count +=i

    print(str(count))
    return count


findmultiple(number)