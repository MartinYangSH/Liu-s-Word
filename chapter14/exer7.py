import re

def readCDR(f):
    '''
        read CDR file and print err result ,if there is something invalid ,the program will be broke down
    '''
    lists = []
    for line in f.readlines():
        list = line.strip('\n').replace(' ',',').split(',')
        if list[0] == '':
            raise ValueError
        a = re.findall('\d{3}-\d{3}-\d{4}', list[1], re.S)
        b = re.findall('\d{3}-\d{3}-\d{4}', list[2], re.S)
        if a == [] or b == []:
            print 'Error CDR :',list
        else:
            lists.append(list)
    return lists

def findLongestCall(lists):
    '''
        find the longest time of the call 
    '''
    for i in range(len(lists)-1):
        if lists[i][3]>lists[i+1][3]:
            long = lists[i]
        else:
            long = lists[i+1]
    return long 

def findLocation(file,list):
    '''
        used to find the location of the call's from and to 
    '''
    f = open(file)
    fm = ''
    to = ''
    for line in f.readlines():
        item = line.split('|')
        if item[0] == re.findall('^\d{3}', list[1], re.S)[0]:
            fm = item[3]
        elif item[0] == re.findall('^\d{3}', list[2], re.S)[0]:
            to = item[3]
        else:
            continue
    f.close()
    return [fm,to]

def countCallAbroad(lists):
    '''
        used to count the number that somebody call abroad 
    '''
    count = 0 
    for list in lists:
        ft = findLocation('EuropeAreaCode.txt', list)
        if ft[0] == '' or ft[1] == '':
            count += 1 
    return count

def countCallAtDate(date,lists):
    '''
        used to count the number of call called at specified date 
    '''
    count = 0
    for list in lists:
        d = list[0].split('-')
        d = d[0]+'.'+d[1]+'.'+d[2]
        if d == date:
            count += 1
    return count

def countCallAtHour(hour,lists):
    '''
        used to count the number of call called at specified hour
    '''
    count = 0
    for list in lists:
        d = list[0].split('-')
        t = d[4].split(':')
        h = t[0]
        if h == hour:
            count += 1
    return count

#use those functions 
try:
    f = open('CDR.txt')     
    lists = []
    lists = readCDR(f)
except ValueError:
    print 'There is a record which does not have a date.'
else:
    print lists
    print len(lists)
    longest = findLongestCall(lists)                                    #find longest call 
    print 'The longest call is :',longest           
    ft = findLocation('EuropeAreaCode.txt', longest)                    #find location
    print 'From:',ft[0].strip('\n'),'--> To:',ft[1].strip('\n')         
    print 'There are ',countCallAbroad(lists),'Call abroad'             #find abroad call
    print '2016.3.5 has ',countCallAtDate('2016.3.5', lists),' Call.'   #find dated call
    print '2 am has ',countCallAtHour('2', lists),' Call.'              #find houred call
finally:
    f.close()
    