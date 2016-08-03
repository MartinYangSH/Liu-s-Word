try:
    print 'Enterint the try suite'
    dividend = float(raw_input("Provide a dividend to divide:"))
    divisor = float(raw_input("Provide a divisor to divide by:"))
    result = dividend/divisor
    print '%2.2f divided by %2.2f yields %2.2f'%(dividend,divisor,result)
except ZeroDivisionError:
    print "Divide by 0 error"
except ValueError:
    print "Value error, couldn't convert to a float"
print 'Continuing ton with the rest of the program'

