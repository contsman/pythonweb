#Class 中的__命名的属性，外部是访问不了的是private的
#不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self,name):
        self.__name = name

    def set_score(self,score):
        self.__score = score

    def getscore(self):
        print("student %s's score is %s" % (self.__name, self.__score))

    def tostring(self):
        return "{name:"+self.__name+", score:"+self.__score+"}"

    def __str__(self):
        return "{name:"+self.__name+", score:"+self.__score+"}"
    __repr__ = __str__

    def get_grade(self):
        if int(self.__score) >= 90:
            print("student %s's grade is %s" % (self.__name, 'A'))
        elif int(self.__score) >= 60:
            print("student %s's grade is %s" % (self.__name, 'B'))
        else:
            print("student %s's grade is %s" % (self.__name, 'C'))
'''
__iter__()

1.如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环。
2.要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
3.List对应的切片操作，对于Fib可能会报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
    但是没有对step参数作处理：

    Fib[:10:2]
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
'''

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

    def __getitem__(self, n):
        # a, b = 1, 1
        # for x in range(item):
        #     a, b = b, a+b
        # return a
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


student1 = Student("Jack", "59")
student2 = Student("Tomcat", "90")
student1.age = 18
print(student1._Student__name)
student1.getscore()
student1.get_grade()
print(student1.age)

student1.set_name("RenameName")
student1.set_score("90")
student1.getscore()
student1.get_grade()
print(student1.tostring())
print(student1.__repr__())

# fib, n = Fib(), 0
print(Fib()[5]) #不实现__getitem__方法会报错不能通过index获取值

print(Fib()[:10:2])#对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
for n in Fib():
    print(n)
# print(range(fib))
# while True:
#     # if n > 10: break
#     print(fib.__next__())
#     n += 1
