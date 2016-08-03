def convert(n,string = ''):
    if n == 1:
        return '1'+string
    else:
        if n%2 == 0:
            string = '0'+string
            return convert(n/2, string)
        else:
            string = '1'+string
            return convert(n/2, string)

print convert(18)