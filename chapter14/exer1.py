password = '123456'
dictionary = {'id1':'Alice','id2':'Ben','id3':'Tom'}

def checkPass(passStr,password):
    if passStr == password:
        return True
    
class KeyError(Exception):
    '''catch the exception of wrong password'''
    pass

print 'If you want to see the Dictionary'

while True:
    passStr = raw_input('Please input the password:')
    try:
        if checkPass(passStr, password):
            for item in dictionary:
                 print 'id:'+item+' name:'+dictionary[item]
            break
        else:
            raise KeyError
    except KeyError:
        print 'You must have correct password or go away'
