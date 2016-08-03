#coding=utf8
# #循环解法
# def matchBracket(string):
#     left = 0
#     for i in string:
#         if i == '(':
#             left+=1
#         elif i == ')':
#             left -=1
#         else:
#             print 'String is invalid'
#     if left == 0:
#         print 'valid'
#     else:
#         print 'invalid'
# 
# matchBracket(')')

#递归解法   
def matchBrackets(string,position,left):
    if string == None:
        return True
    elif position == len(string) and left == 0:
        print position,'asd'
        return True
    elif position<len(string):
        if string[position] == '(':
            left +=1 
            return matchBrackets(string, position+1,left)
        elif string[position] == ')':
            left -=1
            return matchBrackets(string, position+1,left)
    else:
        return False
            
if matchBrackets('(((()))',0,0):
    print 'Valid'
else:
    print 'Invalid'
