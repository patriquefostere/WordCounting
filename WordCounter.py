from FileHandling import ReadFile, WriteResults
    
def PopulateDictionary(wordsArray):
    wordsDictionary = {}
    for word in wordsArray:
        if word in wordsDictionary:
            wordsDictionary[word] += 1
        else:
            wordsDictionary[word] = 1
    return wordsDictionary
        
def GetHighestWordCount(wordCountDictionary):
    result = 0
    for value in wordCountDictionary.values():
        if value >= result:
            result = value

    return result

def Run():
    wordsArray = ReadFile()
    wordsDictionary = PopulateDictionary(wordsArray)
    WriteResults(wordsDictionary)

Run()
