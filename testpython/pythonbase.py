a = 100
if a >= 0:
    print(a)
else:
    print(-a)


print("I'm \"OK!\"")
print("\t")
print("hh")
#在字符串前面添加r：表示后面的字符串不进行转义后输出
print(r'\'\\\t\\')
print(r'''\\line1
... \\line2
... \\line3''')
age = 18
if age >= 18:
    print('adult')
else:
    print('teenager')

x = 10
x = x+2
print(x)

a = "ABC"
b = a
a = "XYZ"
b = "DHJ"
print(a+" "+b)

#PI = 3.14159265359
#print(PI)
#PI = 3
#print(PI)
i = 11
j = 3
print(i/j)#精确除法
print(i//j)#地板除法，得到的是整数部分，小数部分不是四舍五入，不管你是否大于0.5都抹去
#exercise
print("*******************练习部分**********************")
n = 123
print("1,",n)
f = 456.789
print("2,",f)
s1 = '\'Hello, world\''
print("s1 =",s1)
s1 = r'Hello, \'Adam\''
print("s1 =",s1)
s1 = 'r\'Hello, "Bart"\''
print("s1 =",s1)
s1 = 'r\'\'\'Hello,'
print("s1 =",s1)
s1 = 'Lisa!\'\'\''
print(s1)

print("""小明的成绩从去年的72分提升到了今年的85分，
请计算小明成绩提升的百分点，
并用字符串格式化显示出'xx.x%'，
只保留小数点后1位：""")
s1 = 72
s2 = 85
r = "asdf"
print('''小明的成绩从去年的%d分提升到了今年的%d分，
请计算小明成绩提升的百分点，
并用字符串格式化显示出'%.1f'，只保留小数点后1位''' % (s1,s2,s1/s2))
#list 集合
classmates = ['a','b','c','c','d','e','f','g','h']
print(len(classmates),classmates[-8])
classmates.append("i")
print(len(classmates),classmates)
classmates.pop(2)
classmates.insert(1, 'Jack')
test = [1,'test']
classmates.insert(3,test)
print(len(classmates),classmates)

#tuple(元组) 一旦初始化就不能被修改
tupletest = ('Michael', 'Bob', 'Tracy')
print(tupletest)
#tupletest[0] = "aaa" 不能进行更改tuple本身元素
#print(tupletest)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
## 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

#birth = input('birth: ')
#if int(birth) < 2000:
#    print('00前')
#else:
#    print('00后')
for elem in tupletest:
    print(elem)
    
#和list比较，dict有以下几个特点：

#查找和插入的速度极快，不会随着key的增加而增加；
#需要占用大量的内存，内存浪费多。
#而list相反：

#查找和插入的时间随着元素的增加而增加；
#占用空间小，浪费内存很少。
#所以，dict是用空间来换取时间的一种方法。
d={'a':1,'b':2,'c':3,'d':4}
key = 'b'
print(d.get('e'))
if key in d:
    print(d[key])
    print(d.get(key))
else:
    print(key+' dos\'t in d')

s=set([1,2,3,1])
print(s)
#由于set集合为无序不重复的，所以可以做交集，并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
#setList  =[1,2]
#set的原理和dict一样，所以，同样不可以放入可变对象，
#因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
#s1.add(setList)
testTuple = (1,2,3)
testTuple1 = (1,2,[1,2])
s1.add(testTuple)
#s1.add(testTuple1)
print(s1&s2)#交集
print(s1|s2)#并集

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-1))


#默认参数函数建立
def enroll(name,gender,age = 6,city='beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('wangtiecai','M')
enroll('wangtiecai','M',7)
enroll('wangtiecai','M','Tianjin')
enroll(age=10,city='Tianjin',name='Wangtc',gender='F')

#命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)

# person('Wangtc',10,'Peking','Enginer')# 会报错
#必须这样调用
person('Wangtc',10,city='Peking',job='Enginer')
#关键字参数函数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        print('city in kw')
        pass
    if 'job' in kw:
        # 有job参数
        print('job in kw')
        pass
    print('name:', name, 'age:', age, 'other:', kw)

extra={'job':'Enginer','city':'Peking'}
person('Wangtc',10,**extra)
#递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

def fact1(n):
    return fact_iter(n, 1)

def fact_iter(num, product=1):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

#print(fact(100))
print(fact1(5))
print(fact_iter(5))
#汉诺塔的移动可以用递归函数非常简单地实现。

#请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
#然后打印出把所有盘子从A借助B移动到C的方法，例如：


def move(n,a,b,c): 
    if n==0:
        return None
    elif n==1:
        print("%s-->%s" % (a,c))
    else:
        move(n-1,a,c,b)#首先将n-1个盘子从A柱子上移动到B上
        move(1,a,b,c)#将最后一个盘子放到C柱子上
        move(n-1,b,a,c)#将n-1个盘子从B柱子上移到C上

move(3,'a','b','c')

#切片取集合中部分片段元素slice
slice=list(range(100))#slice=[0, 1, 2, 3, ..., 99]
print(slice[0:3])
#如果其实索引为0可以默认写为arr[:n]方式去到的元素不包含索引n的元素
print(slice[:3])
#取list中倒数的元素
print(slice[-3:-1])
#前10个数，每两个取一个：
print(slice[:10:2])
#所有数，每5个取一个：
print(slice[::5])
#甚至什么都不写，只写[:]就可以原样复制一个list：
print(slice[:])
#tuple也是一种list，唯一区别是tuple不可变。
#因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print((0,1,2,3,4,5)[:3])
#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。
#因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

#列表生成式 实现全排列
print([m + n for m in 'ABC' for n in 'XYZ'])
#列表生成式 获取当前目录下的所有文件
import os
print([d for d in os.listdir('.')])
#列表生成式 大小写转换
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
print([s.upper() for s in L])

#*******************exercise*****************
L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s,str)])

#生成器计算斐波那契数列算法
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return "done"

fib(6)

#reduce
from functools import reduce
def fn(x, y):
    return x * 10 + y
def char2num(s):
     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print(reduce(fn, [1, 3, 5, 7, 9]))
print(reduce(fn, map(char2num, '13579')))

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print(str2int('20'))

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def normalize(name):
    return name[:1].upper()+name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
#编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod1(L):
    return reduce(common,L)
def prod2(L):
    return reduce(lambda x,y:x*y,L)
def common(x,y):
    return x*y

print('3 * 5 * 7 * 9 =', prod1([3, 5, 7, 9]))
print('3 * 5 * 7 * 9 =', prod2([3, 5, 7, 9]))
#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
#想整体变为整数，之后除以小数点位数
def str2float(s):
    return reduce(lambda x,y:x*10+y,map(int,s.replace(".","")))/(10 ** (len(s) - s.find(".") - 1))

print('str2float(\'123.456\') =', str2float('123.456'))

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
def is_palindrome(n):
    return str(n)[::-1]==str(n)

# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))

#请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    for key in t:
        return key
L2 = sorted(L, key=by_name)
print(L2)
#再按成绩从高到低排序：
def by_score(t):
    return t[1]*-1

L2 = sorted(L, key=by_score)
print(L2)

#lambda 更方便
NAME,SCORE=0,1
def sortBy(t):
    return lambda x:x[t]
print(sorted(L, key=sortBy(NAME)))
print(sorted(L, key=sortBy(SCORE),reverse=True))

#decorator 装饰器动态增加功能。装饰器特点，接受一个函数参数，返回一个函数参数
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
'''@log
def testLog():
    print('testLog.....')
testLog()
print(testLog.__name__)'''

#带有参数的decorator
def log1(text):
    def decorator(func):
        #因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
        #否则，有些依赖函数签名的代码执行就会出错。
        @functools.wraps(func)#将function.__name__属性的值修改为调用log1装饰器的__name__
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log1('testDecorator')
def testDecorator():
    print('testDecorator function print')
#testDecorator()
#print(testDecorator.__name__)

#decorator exercise****************************
#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
#编写共同拥有带有参数和不带有参数功能
def testLog(text):
    def decorator(func):
        @functools.wraps(func)
        def logger(*args,**kw):
            if not callable(text): print(text)
            print("start call %s %s():" % (text,func.__name__))
            func(*args,**kw)
            print("end call %s %s" % (text,func.__name__))
            return logger
        return logger
    return  decorator(text) if callable(text) else (lambda fn : decorator(fn))
@testLog
def testExerciseDeco(msg):
    print('testExerciseDeco'+msg)
testExerciseDeco('1111')
