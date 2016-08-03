D = {'1':1,'2':2}
class KeyError(Exception):
    #used to raise an error when key not in D
    pass
key = raw_input('Please input a key:') 

try:
    if key not in D:
        raise KeyError
    else:
        D[key] += 1
except KeyError:
    D[key] = 1

print D