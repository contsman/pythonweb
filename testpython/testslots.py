'''
只允许对Student实例动态添加已经在类中绑定好的属性。
为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
'''


class SlotClass:
    __slots__ = ('name', 'age')

slot1 = SlotClass()
slot1.name = 'wangtiecai'
slot1.age = '26'
slot1.tel = '123412312'

