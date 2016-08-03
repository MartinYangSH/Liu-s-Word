def memoFab(n,fab = {}):
    if fab.has_key(n):
        return fab[n]
    else:
        if n == 1:
            fab[1] = 1
            return fab[1]
        elif n == 2:
            fab[2] = 1 
            return fab[2]
        else:
            fab[n] = memoFab(n-1,fab)+memoFab(n-2,fab)
            return fab[n]
decide = True
while (decide):
    n = int(raw_input('Please input an int:'))
    print 'The fibonacci is ',memoFab(n)
    decide = raw_input('Do you want to continue?(Y/N)')
    if decide=='Y' or decide == 'y':
        decide = True
    else:
        decide = False
    