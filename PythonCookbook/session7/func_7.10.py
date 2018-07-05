
# 问题：代码中需要依赖到回调函数的使用（比如事件处理器、等待后台任务完成的回调），同时还需要让回调函数拥有额外的状态值，以便在它的内部使用


# 解决：

def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)

# 使用

def print_result(result):
    print('Got:', result)

def add(x, y):
    return x + y

apply_async(add, (2, 3), callback=print_result)
# 返回Got: 5

apply_async(add, ('hello', ' word'), callback=print_result)
# Got: hello word

# 问题：print_result只能接受一个参数，如果让回调函数访问其他变量或者特定环境的变量值就会遇到麻烦


# Versino1 解决：带额外状态的回调函数，使用类定义
class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))
r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, ('hello ', 'word'), callback=r.handler)

# Version2 解决：使用闭包方法

def make_handler():
    sequence = 0
    def handler(result):
        # 使用nonlocal定义sequence为自由变量，否则sequence将不可使用
        nonlocal  sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler

handler = make_handler()
apply_async(add, (2, 3), callback=handler)
apply_async(add, ('hello', 'word'), callback=handler)

# Version3 解决：使用协程
def make_handler():
    sequence = 0
    # while循环，是一个死循环
    while True:
        # yield出的值给result
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
# 重点：对于协程，需要使用它的send()方法作为回调函数
handler = make_handler()
# 使用enxt方法让handler协程运行一次，这时sequence的值为1
next(handler)
# 使用send方法调用协程的回调函数
apply_async(add, (2, 3), callback=handler.send)
apply_async(add, ('hello', 'word'), callback=handler.send)

# Version4 使用lambda
apply_async(add, (2, 3), callback=lambda r: handler(r, seq))