from contextlib import contextmanager

# 1，异常之后exit不执行
# @contextmanager
# def foo():
#     print('enter')
#     yield 5
#     print('exit')
#
# if __name__ == '__main__':
#     with foo() as f:
#         print(f)

# 2，
@contextmanager
def foo():
    print('enter')
    try:
        # 2,把yield之前的当做 __enter__ 方法执行
        yield 5
    # 4,把yield之后的当做 __exit__ 方法执行；
    finally:
        print('exit')

if __name__ == '__main__':
    # 1，把yield的值作为 __enter__ 的返回值
    with foo() as f: # 3，with首先进入__enter__也就是第1步；执行到yield 5把返回值给f；
        # 4，抛出一个异常；直接执行__exit__也就是第4步，执行完成之后，抛出异常结束
        raise Exception()
        # print被异常打断不执行
        print(f)