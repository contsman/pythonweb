class Animal(object):
    __animalname__="Animal"
    def run(self):
        print("Animal can run....")


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class OtherAnimal(object):
    def run(self):
        print('OtherAnimal is running...')

dog = Dog()
dog.run()
print(isinstance(dog,Animal))


def run_twice(instance):
    instance.run()
    instance.run()
#Python是动态语言，java是静态语言。
# Python多态和Java不同之处是，对于Python这样的动态语言来说，
# 则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：因为class都是object的子类，都继承了object（此处有点像JavaScript原生链。。）
run_twice(dog)
run_twice(Animal())
run_twice(OtherAnimal())

#通过type(obj)函数获取对象信息，数据类型，对象类型等。。
print(type(run_twice))


#判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types
print(type(run_twice)==types.FunctionType)
print(type(run_twice)==types.LambdaType)
print(type(run_twice)==types.MethodType)
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir(Animal))


#hasattr 获取是否有属性 或者方法
def testhasattr():
    if hasattr(dog,'egg'):
        dog.run()
    else:
        print("Class Dog has no egg function")

testhasattr()