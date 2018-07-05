
# 将单方法的类转换为函数

# 有一个除__init__()方法外只定义了一个方法的类，将它转换成一个函数

# 解决思路：大多数情况下，可以使用闭包来将单个方法的类转换成函数

from urllib.request import urlopen

class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))

yahoo =  UrlTemplate('https://www.baidu.com/?s={names}&f={fields}')
for line in yahoo.open(names='IBM, APPL, FB', fields='sl1c1v'):
    print(line.decode('utf-8'))

# 把上面的类用函数来写

def urltemplate(template):
    # opener()函数记住了template参数的值，并在接下来的调用中使用它
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener

yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(name='IBM, APPL, FB', fields='sl1c1v'):
    print(line.decode('utf-8'))


# 总结：任何时候只要碰到需要给某个函数增加额外的状态信息问题，都可以考虑使用闭包。