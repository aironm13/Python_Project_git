from jinja2 import Environment, PackageLoader, FileSystemLoader


# 包加载器
env = Environment(loader=PackageLoader('web_jinja', 'template'))

# 文件加载器
# env = Environment(loader=FileSystemLoader('web_jinja/template'))

# 搜索模块
template = env.get_template('index.html')

# 输出返回Template信息
print(template.render(title='Jinja2', url='www.Jinja2', username='TOM'))


# # 自动转义
# def guess_autoescape(template_name):
#     if template_name is None or '.' not in template_name:
#         return False
#     # 从右往左按照点切，只切一次返回一个列表，取这个列表索引为1的元素，也就是后缀
#     ext = template_name.rsplit('.', 1) [1]
#     return ext in ('html', 'htm', 'xml')
#
# env = Environment(autoescape=guess_autoescape,
#                   loader=PackageLoader('web_jinja'),
#                   extensions=['jinja2.ext.autoescape'])























