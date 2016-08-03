def promptOpen(method):
    if method == "r":
        try:
            fileName = raw_input('Please input fileName:')
            f = open(fileName,'r')
        except Exception,e:
            print e
            promptOpen()
        else:
            for line in f.readlines():
                print line
                f.close()
    elif method == "w":
        try:
            fileName = raw_input('Please input fileName:')
            f = open(fileName,'a+')
        except Exception,e:
            print e
            promptOpen()
        else:
            paragraph = raw_input('Please input what you want to write into the file:')
            f.write(paragraph)
            f.close()
            print fileName+" has been changed"

promptOpen('w')
promptOpen('r')
