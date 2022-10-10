



from operator import truediv
from unittest import result


# Elias method
def comparestrings(str1, str2):
    result= True
    lenStr1 = len(str1)
    lenstr2 = len(str2)
    compare = str1[-lenstr2:]
    if(str2 == compare) or (str2 == ""):
        result = True
    else:
        result = False
    

    return result

# Best Practice
def comparestirngsKata(str1, str2):
    return (str1.endswith(str2))


comparestirngsKata('abcde', 'cde')