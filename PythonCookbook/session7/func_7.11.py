from queue import Queue
from functools import wraps
# 当使用回调函数的时候，担心很多小函数的扩展可能会弄乱程序控制流，通过某个方法来让代码看上去更像一个普通的执行序列


# 解决： 使用生成器和协程可以使回调函数内联在某个函数中


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)

# Version1


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args

def init_async(func):
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
    return wrapper

# 上面两个代码片段允许使用yield语句内联回调

def add(x, y):
    return x + y

@init_async
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

# 总结：将复杂的控制流隐藏到生成器函数背后在第三方库和包中都能看到，
# 如contextlib中的@contextmanager装饰器；通过一个yield语句将进入和离开上下文管理器粘合在一起