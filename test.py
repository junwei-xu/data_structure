#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/7/5 15:18
# description
# def NumberOf1(n):
#     count = 0
#     while n&0xffffffff != 0:
#         count += 1
#         n = n & (n-1)
#     return count
# print(NumberOf1(-5))

# def count(n):
#     coun = 0
#     if n >= 0:
#         while n:
#             coun += n & 1
#             n >>= 1  # 无符号右移一位
#         return coun
#     else:  # n为负数 Python中bin一个负数，输出的是它的原码的二进制表示加上个负号
#         n = bin(n & 0xffffffff)
#         n = str(n)
#         return n.count('1')
#
# print(count(-5))
# class Solution:
#     def oct_to_binary(self, input_int):
#         # write code here
#         coun = 0
#         if input_int >= 0:
#             while input_int:
#                 coun += input_int & 1
#                 input_int >>= 1  # 无符号右移一位
#             return coun
#         else:
#             n = bin(input_int & 0xffffffff)
#             n = str(n)
#             return n.count('1')
#
#
# n = int(input())
# print(Solution().oct_to_binary(n))

# def convert(one_string,space_character):#one_string:输入的字符串；space_character:字符串的间隔符，以其做为分隔标志
#     string_list = str(one_string).split(space_character)#将字符串转化为list
#     first = string_list[0].lower()
#     others = string_list[1:]
#     others_capital =[word.capitalize()for word in others]#str.capitalize():将字符串的首字母转化为大写
#     others_capital[0:0]=[first]
#     hump_string =''.join(others_capital)#将list组合成为字符串，中间无连接符。
#     return hump_string
# if __name__=='__main__':
# print"the string is:ab-cd-ef"
# print"convert to hump:"
# print convert("ab-cd-ef","-")

# def camelCase(newString):
#     # write code here
#     # 先全部小写
#     newString = newString.lower()
#     newString = list(newString)
#     # 记录间隔的索引
#     res = []
#     for i, v in enumerate(newString):
#         if not (49 <= ord(v) <= 57 or 65 <= ord(v) <= 90 or 97 <= ord(v) <= 122):  # 数字 大写 小写
#             res.append(i)
#     print(res)
#     for i in res:
#         if i + 1 < len(newString) - 1:
#             newString[i + 1] = newString[i + 1].upper()
#
#     newString = ''.join(newString)
#     for i in res:
#         newString = newString.replace(newString[i], '-')
#
#     newString = newString.replace('-', '')
#
#     if newString is None:
#         return "shopee"
#
#     newString = list(newString)
#     if 65 <= ord(newString[0]) <= 90:
#         newString[0] = newString[0].lower()
#
#     return ''.join(newString)
#
#
# print(camelCase("This is a Demo!"))
