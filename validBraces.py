def validBraces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            # we create a stack for each char we test, 
            # openers are easy.
            # closers we match against the last char in the stack.
            # if it is the correct closer then we remove both and continue testing 
            # if it does not match we return false immedialty.
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0



validBraces("([{]}])")

# usedString = {
#     "[":0,
#     "{":0,
#     "(":0
#     }



# def valid_braces(string):

    
    
#     stringBegins = ['[', '{','(']
#     stringEnds = [']', '}',')']
#     closingString = ""
#     openingString = ""
    
#     result = True
#     openingcounter = 0
#     closingCounter = 0
#     splitString = []
    
#     splitString.extend(string)
#     for i in range (len(splitString)):
#     # for i in splitString:
#         testing = splitString[i]
#         if splitString[0] in stringEnds:
#             # result = False
#             break
#         elif splitString[i] in stringBegins:
            
#             openingString = stringBegins.index(splitString[i])
#             closingString = stringEnds[openingString]

            

#             if (closingString in splitString) and ((splitString.index(closingString, i) - i) % 2 != 0):
#                 openingcounter +=1
#                 usedString.update({stringBegins[openingString]: openingcounter})

#             else:
#                 break

#         elif splitString[i] in stringEnds:
#             openingString = stringEnds.index(splitString[i])
#             openIndex = usedString.get(stringBegins[openingString]) 

#             if openIndex <1:
#                 # result = False
#                 break
                
#                 # i = len(splitString) -1
#             else:
#                 closingCounter +=1
#     if (closingCounter == openingcounter) and (closingCounter != 0):
#          result = True
    

#     print(str(result))
#     return result
            

# valid_braces("([}{])")
# # valid_braces("(({{[[]]}}))")