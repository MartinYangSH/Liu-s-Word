def factorial(n):
    '''Recursive Factorial with print to show operation.'''
    indent = 4*(6-n)*' '    #more indent on deeper  recursion , so the most important thing is the amount of indent 
    print indent+'Enter factorial n = ',n
    if n == 1:
        print indent +'Base case.'
        return 1
    else:
        print indent+'Before recursive call f('+str(n-1)+')'
        #seperate recursive call allows print after Call
        rest = factorial(n-1)
        print indent+'After recursive call f('+str(n-1)+') = ',rest
        return n*rest
factorial(4)