from codeList14_7 import *

def main():
    pm = passManager({'bill':'$4Donuts','rich':'123ABC!'})
    
    maxTries = 3    #three tries allowed
    cnt = maxTries
    result = False
    while cnt>0 and not result:
        userStr = raw_input('User name :')
        try:
            result = pm.validate(userStr)
        except NameException:
            print 'Bad name!'
        except UserException:
            if raw_input('No such name ,add as new user(Y or y)?')in 'Yy':
                try:
                    pm.addUser(userStr)
                    #only get here if no excptions raised addUser
                    result = True
                except NameException:
                    print 'Bad name!'
                except UserException:
                    print 'User already exists!'
                except PasswordException:
                    print 'Bad password!'
        finally:
            cnt -=1
    if not result:
        print 'Session timed out.'    
    else:
        print 'Welcome user',userStr

if __name__ == '__main__':
    main()
    
                    