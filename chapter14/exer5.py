#coding=utf8
def safe_input(prompt='',ty_pe=str):
    if type(prompt) == str:
        print prompt
        a = input()             #raw_input(prompt)的返回值都是str，而input()则返回输入的类型
        print type(a)
        if type(a) == ty_pe:
            return a
        else:
            safe_input(prompt, ty_pe)

#ty_pe处可以选择任意数据类型
print safe_input("Please input :",str)
