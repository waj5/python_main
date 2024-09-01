import  re

# re.match(r'^\d{3}-\d{3,8}$', '010-12345')
#pattern 正则表达式
#string 要匹配的字符串

# res =re.match("冰","冰冰永元元十八")
# print(res.group())

#.匹配任意字符，\n除外
res =re.match(".","冰冰永元元十八")
print(res.group())


#[]匹配中括号中列举的字符
res = re.match("[a-z].*","abc")
print(res.group())

res = re.match("[0-9]","54321")
print(res.group())

res=re.match("[a-zA-Z]","ssxbb")
print(res.group())


#\d匹配数字，\w匹配字母数字，\s匹配空白字符
res = re.match("\d","010-12345")
print(res.group())


#\D匹配非数字，\W匹配非字母数字，\S匹配非空白字符
res = re.match("\D","冰冰永元元十八")
print(res.group())



res = re.match("\w.*","abc_网-AAAA000")
print(res.group())
