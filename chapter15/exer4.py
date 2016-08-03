def multiFind(keyword,string):
    """
    >>> multiFind('I','Hello ,I am a student ,I am not a teacher ,I like learning coding .Since I can create some interesting things')
    4
    >>> multiFind('i','Hello ,I am a student ,I am not a teacher ,I like learning coding .Since I can create some interesting things')
    7
    >>> multiFind('z','Hello ,I am a student ,I am not a teacher ,I like learning coding .Since I can create some interesting things')
    0
    """
    
    list = string.split(keyword)
    count = len(list)-1
    return count
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)