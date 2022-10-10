


def duplicate_count(text):
    # Your code goes here
    duplicateChars = '' 
    loweredtext = text.lower()   
    for char in loweredtext:
        if(char not in duplicateChars) and (loweredtext.count(char) >1):
            duplicateChars +=char
    return len(duplicateChars)

duplicate_count("abcdeaB")