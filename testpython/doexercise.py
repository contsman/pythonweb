#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen:

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('width must be an integer!')
        elif value<0 or value >1920:
            raise ValueError('width must between 0 ~ 1920!')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError('height must be an integer!')
        elif value<0 or value >1080:
            raise ValueError('height must between 0 ~ 1080!')
        self._height = value

    @property
    def resolution(self):
        return self._width*self._height


#type 动态创建类，为类动态绑定方法

def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)
Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h))


#红包算法推断测试

import random

def weixin_divide_hongbao(money, n):
    divide_table = [random.randint(1, 10000) for x in range(0, n)]
    print(divide_table)
    sum_ = sum(divide_table)
    print(sum_)
    return [x*money/sum_ for x in divide_table]

print(weixin_divide_hongbao(100,10))