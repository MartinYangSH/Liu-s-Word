while True:
    valueStr = raw_input("Please input an Iteger:")
    try:
        if valueStr.isdigit():
            valueInt = int(valueStr)
            print 'The result is',valueInt
            continue
        else:
            raise ValueError,valueStr   #raise an exception here
    except ValueError:
        print 'Conversion to int Error:',valueStr
        continue
    
    