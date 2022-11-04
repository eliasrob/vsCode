from ast import Or
from inspect import stack

# my idiot solution
# def anagrams(word, words):
#     #your code here
#     wordchars = list(word)
#     wordsList = words
#     stack = []
#     isAnagram = True
    
#     for item in wordsList:
#         for char in word:
#             charCount = word.count(char)
#             itemCharcount = item.count(char)
#             if(charCount != itemCharcount) or (len(word) != len(item)):
#                 isAnagram = False
#                 break
#             else:
#                 isAnagram = True
#         if(isAnagram == True):
#             stack.append(item)

#     print(str(stack))
        

# Kata Pro solution
def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]




# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']),
# anagrams('abba', ['dada', 'bbaa'])