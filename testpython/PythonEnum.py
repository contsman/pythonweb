from enum import Enum,unique


MonthEnum = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# print(MonthEnum.Jan)
# for name, member in MonthEnum.__members__.items():
#     print(name, '=>', member, ',', member.value)
#@unique装饰器可以帮助我们检查保证没有重复值。
@unique
class WeekDay(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

for t in WeekDay:
    print(t.value)
print(WeekDay.Mon.value)
print(type(Enum), type(MonthEnum), isinstance(MonthEnum.Jan, MonthEnum), isinstance(MonthEnum.Jan, Enum), type(MonthEnum)==type(WeekDay))