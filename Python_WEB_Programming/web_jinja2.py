from jinja2 import Environment, PackageLoader, FileSystemLoader


# 包加载器
# env = Environment(loader=PackageLoader('webarch', 'templates'))

# 文件加载器
env = Environment(loader=FileSystemLoader('webarch/templates'))

# 搜索模块
template = env.get_template('index.html')

userlist = [
    (3, 'tom', 20),
    (5, 'jerry', 16),
    (6, 'sam', 23),
    (8, 'kevin', 18)
]

d = {'userlist':userlist, 'usercount':len(userlist)}
print(template.render(**d)) # 解构
