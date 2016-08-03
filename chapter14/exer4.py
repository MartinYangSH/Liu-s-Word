a = raw_input('Please input the first int:')
b = raw_input('Please input the second int:')
c = raw_input('Please input the third int:')

try:
    if a.isdigit() and b.isdigit() and c.isdigit():
        a = float(a)
        b = float(b)
        c = float(c)
        if a == 0 or b == 0 or c == 0:
            raise ZeroDivisionError
        else:
            print a/b+c
    else:
        raise IOError
except IOError:
    print 'Please input digit!'
except ZeroDivisionError:
    print 'Don\'t input a zero!'
except ValueError:
    print 'Can\'t parse to float!'
        