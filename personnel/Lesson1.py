print("Hello World")
"""
'''
使用变量保存数据并进行算术运算
# Version 1.0
# quentinwey
# date 2020.01.10
'''

a=321
b=123
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

'''
使用type()检查变量的类型
# version 1.0
# quentinwey
# date 2020.01.10
'''
a = 100
b = 12.345
c = 1+5j
d = 'hello world'
e = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

'''
使用input()函数获取键盘输入（字符串）
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串
# version 1.0
# quentinwey
# date 2020.01.10
'''
a = int(input("a = "))
b = int(input("b = "))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

'''
赋值运算符和复合赋值运算符
# version 1.0
# quentinwey
# date 2020.01.10
'''
a = 10
b = 3
a += b
a *=a + 2
print(a)
'''
比较，逻辑和算身份运算符的使用
# version 1.0
# quentinwey
# date 2020.01.10
'''
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print("flag0 =",flag0)
print("flag1 =",flag1)
print("flag2 =",flag2)
print("flag3 =",flag3)
print("flag4 =",flag4)
print("flag5 =",flag5)
print(flag1 is True)
print(flag2 is not false)
"""
"""
'''
将华氏温度转换成摄氏温度
version 1.0
quentinwey
date 2020 01.10
'''
f = float(input('请输入华氏温度\n F='))
c = (f - 32 )/1.8
print('%.1f华氏度 = %.1f摄氏度' %(f, c))


'''
输入半径，计算圆的周长与面积
version 1.0
quentinwey
date 2020 01.13
'''
import math

radius = float(input('请输入圆的半径:'))
perimeter =2* radius * radius
area = math.pi*radius * radius
print('周长：%.2f' % perimeter)
print('面积：%.2f'% area)

'''
输入年份判断是不是闰年
version 1.0
quentinwey
date 2020 01.14
'''
year = int(input('请输入年份'))
is_leap = (year % 4 == 0 and year % 100 != 0  or  year % 400 == 0)
print(is_leap)
"""
"""
'''
用户身份验证
version 1.0
quentinwey
date 2020 01.14
'''
username = input('请输入用户名')
password = input('请输入密码')
if username == 'admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')

'''
分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
version 1.0
quentinwey
date 2020 01.14
'''
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x,y))


'''
英制单位英寸和公制单位厘米互换
version 1.0
quentinwey
date 2020 01.14
'''
value = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸' or unit == '寸' or unit == 'cun':
    print('%.2f英寸 = %.2f厘米' % (value,value*2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.2f厘米 = %.2f英寸' % (value,value/2.54))
else:
    print('请输入有效的单位')

'''
百分制成绩转换为等级制成绩
version 1.0
quentinwey
date 2020 01.14
'''
score = float(input('请输入成绩：'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('您的成绩级别是:',grade)


'''
判断输入的边长能否构成三角形，如果可以，则计算出三角形的周长与面积
version 1.0
quentinwey
date 2020 01.15
'''
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长： %f' % (a + b +c ))
    p = (a + b + c) / 2
    area = (p*(p-a)*(p-b)*(p-c)**0.5)
    print('面积：%f' %(area))
else:
    print('不能构成三角形')

'''
用for循环实现1-100求和
 version 1.0
 quentinwey
 date 2020 02.11
'''
sum = 0
for x in range(101):
    sum += x
print(sum)

"""