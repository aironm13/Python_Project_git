
# join方法
# import threading
#
# def add(x, y):
#     ret = x + y
#     print(ret)
#     return ret
#
# # 定义一个damon线程
# t1 = threading.Thread(target=add, args=(3, 4), daemon=True)
# # 启动一个damon线程
# t1.start()
# # join，必须等t1线程执行完，主线程才会执行然后退出
# t1.join()
# print('Master Stop')



# threading.local类
import threading
import time

# 创建一个local类实例
global_data = threading.local()

def worker():
    # 为每个线程都维护一个global_data.x的属性
    global_data.x = 100
    for i in range(100):
        time.sleep(0.01)
        global_data.x += 1
    # 输出当前线程对象和x的值
    print(threading.current_thread(), global_data.x)

for i in range(10):
    threading.Thread(target=worker).start()

