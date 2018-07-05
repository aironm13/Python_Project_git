import pickle

obj = ['123', 'a', 'b', 'c']
print(obj)

# 序列化到文件
with open('a.txt', 'wb') as f:
    pickle.dump(obj, f)

# 从文件反序列化
with open('a.txt') as f:
    print(pickle.load(f))