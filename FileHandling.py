import os
import re

def remove_non_alpha(input_string):
    """
    Remove all non-alphabetical characters from a string using regex.
    
    Args:
        input_string (str): The input string to process
        
    Returns:
        str: A new string with only alphabetical characters (a-z, A-Z)
    """
    # Use regex to keep only alphabetical characters

    return re.sub(r'[^a-zA-Z\-\']', '', input_string).lower()

def ReadFile():
    file = os.path.join(os.getcwd(), "test.txt")
    with open(file, 'r') as file:
        # first split document into lines - otherwise we get problems arising from removing non-alphabetical characters
        
        lines = file.readlines()

        # remove blank lines
        nonBlankLines = []
        for line in lines:
            if len(line.strip()) != 0:
                nonBlankLines.append(line)

        # split on spaces and dashes
        # â€” is how python reads a certain kind of dash
        split = []
        for line in nonBlankLines:
            split += line.split(" ")

        dashesRemoved = RemoveDashes(split)

        resultWordArray = []
        for word in dashesRemoved:
            if len(word) >= 3:
                resultWordArray.append(remove_non_alpha(word))

        return resultWordArray
    
def RemoveDashes(wordArray):
    result = []
    dashString = r"â€”"
    for word in wordArray:
        if dashString in word:
            split = word.split(dashString)
            result += split
        else:
            result.append(word)

    return result
    
def WriteResults(wordCountDictionary):
    lines = []
    for i in range(1, 4):# only care about words occuring up to 3 times
        wordsOccurringITimes = []
        for key in wordCountDictionary:
            if wordCountDictionary[key] == i:
                wordsOccurringITimes.append(key)
        
        lines.append(f"\nHere's all the words in the text that occur {i} times:\n")
        for word in wordsOccurringITimes:
            lines.append(word+"\n")

    path = os.path.join(os.getcwd(), "result.txt")
    with open(path, 'w') as file:
        file.writelines(lines)