
# 通过format()函数和字符串方法使一个对象支持自定义的格式化


_formats = {
    'ymd':'{d.year}-{d.month}-{d.day}',
    'mdy':'{d.month}-/{d.day}/{d.year}',
    'dmy':'{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

# __format__()方法给Python的字符串格式化功能提供了一个钩子

from datetime import date
d = date(2012, 12, 21)
format(d)