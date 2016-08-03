while True:
    try:
        fileName = raw_input("Open file:")
        dataFile = open(fileName,"r")   #open a file (possible exception))
        break
    except IOError:
        print 'Bad file name.'
    