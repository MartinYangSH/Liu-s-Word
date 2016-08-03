def processFile(dataFile):
    """Print each line of a file with its line number."""
    count = 1
    for line in dataFile:
        print 'Line '+str(count)+':'+line.strip()
        count = count+1
while True:
    fileName = raw_input("Input a file to open: ")
    try:
        dataFile = open(fileName)
    except IOError:
        print 'Bad file name;Try again'
    else:
        #no exception so let's process the file
        print 'Procession file ',fileName
        processFile(dataFile)
        break   #exit "while" loop(but do "finally" block first)
    finally:
        try:
            dataFile.close()
        except NameError:
            print 'Going around again'

print 'Line after the try-except group'

