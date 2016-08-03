'''This is the password which is used to check 
if you have the previlege to visit the Dictionary'''
password = '123456'
def checkPass(passStr,password):
    if passStr == password:
        return True

class PassError(Exception):
    '''catch the exception of wrong password'''
    pass
print 'If you want to see the Dictionary'
while True:
    passStr = raw_input('Please input the password:')
    try:
        if checkPass(passStr, password):
            f = open('Dictionary.txt')
            for line in f.readlines():
                print line,
            break
        else:
            raise PassError
    except PassError:
        print 'You must have correct password,or go away'
        goAway = raw_input(':Y(yes)/N(no):')
        if goAway=='Y':
            break
        else:
            continue
    finally:
        try:
            f.close()
        except Exception:
            if goAway != 'Y':
                print 'Please Try Again!'
            else:
                print 'Bye!'