while True:
    try:
        valueStr = raw_input("Input Iteger:")
        valueInt = int(valueStr)    #convert to int (possible exception)
        break
    except ValueError:
        print 'Bad input.'
        