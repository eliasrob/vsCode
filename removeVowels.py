


from posixpath import split

userInput = input("type a string here:")

# Elias Method
def disemvowel(string_):
    vowles = ['a', 'e', 'o', 'u', 'i', 'A', 'E', 'O', 'U', 'I']
    newString = ""
    splitStrings = string_.split(' ')
    for i in range (len(splitStrings)):
        for char in splitStrings[i]:
            if char not in vowles:
                # splitString.replace(char, "")
                newString+=char
            splitStrings[i] = newString
        newString = ''
        
    result = ' '.join(map(str, splitStrings))
    print(result)
    return splitStrings

# Best Practice
def disemvowel(s):
    # make a string of all vowles for testing
    # loop through each char in the vowels string
    for i in "aeiouAEIOU":
        # if any char in the vowels string, replace its match in the original string with ''
        s = s.replace(i,'')
    return s

# Best Practice 2
def disemvowel(string):
    #  remove any char resembling 'aeiouAEIOU' from the original string using translate
    return string.translate(None, 'aeiouAEIOU')


# Call Method
userOutput =  disemvowel(userInput) 