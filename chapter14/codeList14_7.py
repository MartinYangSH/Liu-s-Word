'''
Manage Key
'''
import string

#define our own exception
class NameException(Exception):
    '''For malformed names'''
    pass
class PasswordException(Exception):
    '''For bad password'''
    pass

class UserException(Exception):
    '''Raised for existing or missing user'''
    pass
def checkPass(passStr,targetStr):
    '''Return True,if password contains characters from target'''
    for char in passStr:
        if char in targetStr:
            return True
    return False
    
class passManager(object):
    '''A class to manage a dictionary ofpasswords with erro checking.'''
    def __init__(self,initDict=None):
        if initDict == None:
            self.passDict = {}
        else:
            self.passDict = initDict.copy()

    def dumpPasswords(self):
        return self.passDict.copy()
    def addUser(self,user):
        '''Add good user name and strong password to password dictionary.'''
        if not isinstance(user, str) or not user.isalnum():
            raise NameException
        if user in self.passDict:
            raise UserException
        passStr = raw_input("New password: ")
        #ensure strong password
        if not (checkPass(passStr, string.digits)) and checkPass(passStr, string.uppercase) and checkPass(passStr, string.punctuation):
            raise PasswordException
    def validate(self,user):
        '''Return True, if valid user and password.'''
        if not isinstance(user, str) or not user.isalnum():
            raise NameException
        if user not in self.passDict:
            raise UserException
        passWd = raw_input("PassWd:")
        return self.passDict[user] == passWd
    
            