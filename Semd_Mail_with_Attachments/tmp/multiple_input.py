# coding:utf-8
# 演示：多行输入
from time import sleep as wait

lines = []

print("Enter some lines of text, \e for end line ===> ")
while True:
    try:
        s = input()
        if s != '\\e':
            lines.append(s)
        else:
            break
    except:
        break

txt = '\n'.join(lines)

print('- ' * 16)
print('You have entered a text of multiple lines, it is:')
print(txt)

wait(3)
