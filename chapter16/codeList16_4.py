#recursive function to reverse a string 
def reverser(aStr):
    #base Case
    #recursive step
        #divide into parts
        #conquer/reassemble
    n = len(aStr)
    if n == 1:
        return aStr[0]
    else:
        return reverser(aStr[n-1])+reverser(aStr[0:n-1])
theStr = raw_input('Reverse what string:')
result = reverser(theStr)
print 'The reverse of %s is %s.'%(theStr,result)