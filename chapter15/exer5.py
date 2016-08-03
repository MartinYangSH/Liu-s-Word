import string
def addWord(w,wcDict):
    '''
        Update the word frequency: word is the key , frequency is the value
    '''
    if w in wcDict:
        wcDict[w] += 1
    else:
        wcDict[w] = 1
        
def processLine(line,wcDict):
    '''
        Process the line to get lowercase words to add to the dictionary.
    '''
    line = line.strip()
    wordList = line.split()
    for word in wordList:
        #ignore the '--' that is in the file
        if word != '--':
            word = word.lower()
            word = word.strip()
            #get commas,periods and other punctuation out as well
            word = word.strip(string.punctuation)
            addWord(word, wcDict)
    
def prettyPrint(wcDict):
    '''Print nicely from highest to lowest frequency'''
    # create a list of tuples,(value,key)
    
    #valKeyList = [(value, key) for key,val in d.items()]
    
    valKeyList = []
    
    for key,val in wcDict.items():
        valKeyList.append((val,key))
    #sort method sorts on list's first element, here the frequency
    #Reverse to get biggest first
    valKeyList.sort(reverse = True)
    print '%-10s%10s'%('Word','Count')
    print '_'*21
    for val,key in valKeyList:
        print '%-12s    %3d'%(key,val)
        
def main(fName):
    '''
    >>>main('')
    File named not found
    >>>main('gettysburg.txt')
    Length of the dictionary: 43
    Word           Count
    _____________________
    to                4
    country           3
    a                 3
    the               2
    ...
    '''
    try:
        wcDict = {}
        fObj = open(fName,'r')
    except IOError:
        print 'File named %s not found'%fName
    else:
        for line in fObj:
            processLine(line, wcDict)
        print 'Length of the dictionary:',len(wcDict)
        prettyPrint(wcDict)
        fObj.close()
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
