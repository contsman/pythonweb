#from module名字 import 类名方式可以引入其他文件中的类
from testpython.Student import Student
from testpython.PropertyDecorator import StudentProperty
from testpython.doexercise import Screen
from PIL import Image
# import logging


# logger = logging.getLogger(__name__)
#获取图片缩略图
def getthumbnail():
    im = Image.open('E:\\pythonworkspace\\artist.jpg')
    print(im.format, im.size, im.mode)
    im.thumbnail((160, 90))
    im.save('E:\\pythonworkspace\\thumb.jpg', 'JPEG')

getthumbnail()


from types import MethodType

student1 = Student('Wangtc','90')


def set_tel(self, tel):
    self.tel = tel
student1.set_tel = MethodType(set_tel, student1)
student1.set_tel('13426057895')
# logging.warning('This is warning message')
print(student1.tel)
#给一个实例动态绑定的方法，其他实例是不起作用的
'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'set_age'''''
# stu2 = Student('Wangtc2','89')
# stu2.set_tel('32123132')

#为了给所有实例都绑定方法，可以给class绑定方法：
def set_tel(self, tel):
    self.tel = tel

Student.set_tel = MethodType(set_tel, Student)

stu3 = Student("Wangtc3","69")
stu3.set_tel("123456789")
print(stu3.tostring())

propstu =StudentProperty()
propstu.score =100

print(propstu.score)
#propstu.otherscore = 200 会报错AttributeError: can't set attribute
print(propstu.otherscore)

screen = Screen()
screen.width = 1920
screen.height = 1080
print(screen.resolution)