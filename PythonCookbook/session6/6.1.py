
# 读写一个CSV格式的文件

# 解决：使用csv库

from collections import namedtuple
import csv
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    Row = namedtuple('Row', 'headings')
    for r in f_csv:
        row = Row(*r)