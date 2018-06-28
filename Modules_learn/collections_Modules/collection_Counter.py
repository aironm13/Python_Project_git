from collections import Counter


words = [1, 2, 3, 4, 5, 12, 1, 2, 3, 4]
word_counts = Counter(words)
print(word_counts)
# Counter({1: 2, 2: 2, 3: 2, 4: 2, 5: 1, 12: 1})

# most_common返回序列中次数最多的前几项
# 返回一个列表包含的多项元组
print(word_counts.most_common(3))
# [(1, 2), (2, 2), (3, 2)]


