#Python 常用内置模块，类库，无需安装

#datetime是Python处理日期和时间的标准库。
from datetime import datetime
now = datetime.now()
print(now)
print(type(now))
dt = datetime(2015,12,8,13,14,59)
print(dt)
#datetime to timestamp
print(dt.timestamp())#注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
# timestamp to datetime
print(datetime.fromtimestamp(1449551699.))
#timestamp也可以直接被转换到UTC标准时区的时间：北京时间与UTC时间相差8小时即 UTF+8:00
print(datetime.utcfromtimestamp(1449551699.0))
#str转换为datetime
print(datetime.strptime("2015-12-08 13:14:59","%Y-%m-%d %H:%M:%S"))
#datetime 转换为str
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%H:%M:%S"))
#对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
from datetime import timedelta
#day +/- 1
print(dt + timedelta(days=1))
print(dt - timedelta(days=1))
#hour +/- 1
print(dt + timedelta(hours=1))
print(dt - timedelta(hours=1))
#本地时间转换为UTC时间
#本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
#一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))#获取本地时区,即:UTC+8:00
print(tz_utc_8)
dt = now.replace(tzinfo=tz_utc_8)
print('Now UTC is %s' %(datetime.utcnow()))
print(dt)

#collections是Python内建的一个集合模块，提供了许多有用的集合类。
#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
from collections import namedtuple
Student = namedtuple("Student",['name','age','score'])
student = Student('Wangtc','20',90)
print(student.name,student.age,student.score)
print(isinstance(student,Student))
print(isinstance(student,tuple))

#使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque
q = deque(['a','b','c'])
q.append('d')
q.appendleft('e')
q.pop()
q.popleft()
print(q)

#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict
dd = defaultdict(lambda :'N/A')
dd['key1']='abc'
print(dd)
print(dd['key1'])
print(dd['key2'])
#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#如果要保持Key的顺序，可以用OrderedDict：

from collections import OrderedDict
d =  dict([('a',1),('b',2),('c',3)])
print(d)
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)

#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdateOrderedDict(OrderedDict):
    def __init__(self,capatity):
        super(LastUpdateOrderedDict,self).__init__()
        self._capatity = capatity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

od = LastUpdateOrderedDict(10)
print(od)

#计数器 Counter
from collections import Counter
c = Counter()
for ch in "programming":
    c[ch] = c[ch]+1
print(c)
