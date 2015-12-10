'''
在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
但是，如果需要“混入”额外的功能，通过多重继承就可以实现，
比如，让Bird除了继承自Animal外，再同时继承FlyableMixIn。这种设计通常称之为MixIn。
就是java中的 类的继承和接口，但是Python中没有进行区分，而是写代码的时候要注意混淆用MxiIn这种命名设计方式区分开来
'''
class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

class Animal(object):
    def say(self):
        print('not a person....')

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal,FlyableMixIn):
    pass

# 各种动物:
class Dog(Mammal,RunnableMixIn):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

dog = Dog()
bird = Bird()
dog.run()
dog.say()
bird.fly()
bird.say()