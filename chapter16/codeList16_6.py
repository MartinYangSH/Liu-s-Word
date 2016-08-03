#Reverse a string using a recursive Function
def reverser(aStr):
    '''recursive function to reverse a string '''
    print 'Got as an argument:',aStr
    #base case 
    if len(aStr) == 1:
        print 'Base case!'
        return aStr
    #recursive step
    else:
        newStr == reverser(aStr[1:])+aStr[0]
        print 'Reassembling %s and %s into %s'%(aStr[1:],aStr[0],newStr)
        return newStr

theStr = raw_input('What string :')
print 
resultStr = reverser(theStr)
print '\nThe reverse of %s is %s\n'%(theStr,resultStr)