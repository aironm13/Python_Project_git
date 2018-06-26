import queue

# 初始化一个大小为8的队列
q = queue.Queue(8)
# 下面两步线程是不安全的；线程切换会导致问题
if q.qsize() == 7:
    q.put(1)

if q.qsize() == 1:
    q.get()