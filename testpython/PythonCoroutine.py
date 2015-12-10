#协程
#子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。
#协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。
# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
# c = consumer()
# produce(c)
'''
注意到consumer函数是一个generator，把一个consumer传入produce后：
    1.首先调用c.send(None)启动生成器；
    2.然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
    3.consumer通过yield拿到消息，处理，又通过yield把结果传回；
    4.produce拿到consumer处理的结果，继续生产下一条消息；
    5.produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
'''

#***********************asyncio************Python 3.4以上版本自带模块进行异步IO处理
# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# import threading
# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread().name)
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread().name)
#
# loop1 = asyncio.get_event_loop()
# tasks = [hello(), hello(), hello()]
# loop1.run_until_complete(asyncio.wait(tasks))
# loop1.close()

#我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：
import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()