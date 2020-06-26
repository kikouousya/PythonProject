import re


str1= input()
result_list = []

for char in str1:
    if char.islower():
        res = ord('z')-ord(char)+ord('a')
        res = chr(res)
    elif char.isupper():
        res = ord('Z')-ord(char)+ord('A')
        res = chr(res)
    else:
        res = char
    print( char,ord(char), res, ord(res) )
    result_list.append(res)

result = "".join(result_list)
print(result)


# def fama(text):
#     result=[]
#     for eachChar in text:
#         if eachChar.islower():
#             n=chr(ord('z')-(ord(eachChar)-ord('a')))
#         elif eachChar.isupper():
#             n=chr(ord('Z')-(ord(eachChar)))
#         else:n=eachChar
#         result.append(eachChar)
#
#     return ''.join(result)
#
# str = "Hello"
# print(fama(str))


# n = int(input())
# print_str = ""
# space_count = n // 2 + 1
# for i in range(1, n + 1, 2):
#     space_count -= 1
#     print_str += " " * space_count + "*" * i + " " * space_count + "\n"
# print(print_str)

#
# def decordKaisa(matched):
#     char = matched.groups()[0]
#     n = ord(char)
#     n += 3
#     if n >122 or 65>n>89:
#         n -= 26
#     res = chr(n)
#     # print(char,ord(char), res, ord(res))
#     return res
# str1 = input()
# # str1 = "%python%IS*(GOOD)"
# str1 = re.sub("([a-z]|[A-Z])", decordKaisa, str1)
#
# print(str1)
