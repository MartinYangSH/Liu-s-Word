myDict = {'bile':100,'zach':'hi mom','laurie':'bye mom'}

try:
    result = ''
    theKey = raw_input("Give me a key:")
    val = myDict[theKey]
    result = result+val
except KeyError:
    result = 'hi mom'
except TypeError:
    result = '100'
else:
    result = result+' '+'all done'
finally:
    if result.isdigit():
        result = int(result)+10

print result