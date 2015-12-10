'''
由于对属性的复制限制比较麻烦所有有了@property装饰器
通过@Property装饰器指定属性的getter方法，并且会生成另一个属性名.setter(@xxx.setter)的装饰器来对属性进行赋值操作
'''


class StudentProperty(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    #otherscore为只读属性,因为没有setter方法,age的值是通过属性_score计算出来的
    @property
    def otherscore(self):
        return 2015 - self._score
