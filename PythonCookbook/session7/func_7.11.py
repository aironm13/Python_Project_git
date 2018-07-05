
# 当使用回调函数的时候，担心很多小函数的扩展可能会弄乱程序控制流，通过某个方法来让代码看上去更像一个普通的执行序列


# 解决： 使用生成器和协程可以使回调函数内联在某个函数中


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)

# Version1
from queue import Queue
from functools import wraps

class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args

def inlined_async(func):
    @wraps(func) #  装饰器
    def wrapper(*args):
        f = func(*args) # 调用函数得出结果
        result_queue = Queue() # 定义一个LIFI的队列，先进先出
        result_queue.put(None) # 向这个队列中put一个None元素
        while True: # 进入循环
            result = result_queue.get() # 取出队列中的一个元素
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wraps

# 上面两个代码片段允许使用yield语句内联回调

def add(x, y):
    return x + y

@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'word'))
    print(r)

    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Goodbye')

test()