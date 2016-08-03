string = "123asbs43abads02982"
digit = []
alphabet = []
def select(string):
    try:
        for item in string:
            if ord(item)>=48 and ord(item)<=57:
                digit.append(item)
            elif ord(item)>=97 and ord(item)<=122 or ord(item)>=65 and ord(item)<=90:
                alphabet.append(item)
            else:
                raise TypeError
    except TypeError:
        print 'The string must be consisted of integer or alphabet'
        
select(string)

print "All digit in string are :"+str(digit)
print "All alphabet in string are :"+str(alphabet)