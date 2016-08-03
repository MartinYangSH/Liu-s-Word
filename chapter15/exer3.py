def is_Palindrome(num):
    """
    >>> is_Palindrome('asd')
    False
    >>> is_Palindrome('asddsa')
    True
    """
    num = str(num)
    numLen = len(num)
    p=''
    if numLen%2 == 0:
        pre = num[:numLen/2]
        post = num[numLen/2:]
    else:
        pre = num[:numLen/2]
        post = num[numLen/2+1:]
    for i in range(len(post)-1,-1,-1):
        p += post[i]
    if p == pre:
        return True
    else:
        return False
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
