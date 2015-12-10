#Python 多线程
import threading,time
def loop():
    print("Thread %s is running...." %(threading.current_thread().name))
    n = 0
    while n<5:
        n += 1
        print('Thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)

    print('Thread %s is ended.' % (threading.current_thread().name))

print('Thread %s is running ....'%(threading.current_thread().name))
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()#如果想实现异步执行子线程，注释掉join()就可以了
print('Thread %s is done.' % (threading.current_thread().name))

#以下多线程中足够多的运行次数，一定会出现balance 全局变量不等于0情况，这是线程之间执行次序乱了，导致balance不能正常等于0
# balance = 0
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
# def run_thread(n):
#     for i in range(1000000):
#         change_it(n)
# t1 = threading.Thread(target=run_thread,name="Thread 1",args=(3,))
# t2 = threading.Thread(target=run_thread,name="Thread 2",args=(5,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

#多线程之间同步锁，实现变量同步，保证同一时间，变量或者方法只能被一个线程调用
balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        #首先获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            #用完锁后进行释放锁，供给其他线程使用。
            #获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程
            lock.release()
t1 = threading.Thread(target=run_thread,name="Thread 1",args=(3,))
t2 = threading.Thread(target=run_thread,name="Thread 2",args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


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
#1.ThreadLocal消除了对象在每层函数中的传递问题，避免调用线程的时候去给线程传递当前线程要操作的对象。
#2.ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，
# HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
local_school = threading.local()
def process_student():
    student = local_school.student
    print("Thread %s is running...student = %s" % (threading.current_thread().name,student))

def process_thread(name,score):
    local_school.student = Student(name,score)
    process_student()
t1 = threading.Thread(target=process_thread,name="Thread 1",args=('Wangtc1','80'))
t2 = threading.Thread(target=process_thread,name="Thread 2",args=('Wangtc2','90'))
t1.start()
t2.start()
t1.join()
t2.join()
print('Thread all done.')