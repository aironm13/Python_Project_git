# 层次结构
# getLogger()源代码
# def getLogger(name=None):
#     if name:
#         return Logger.manager.getLogger(name)
#     else:
#         return root

import logging

# 根logger
root = logging.getLogger()
print(root.name, type(root), root.parent, id(root))
# root <class 'logging.RootLogger'> None 1496087048264


# __name__为当前模块名
logger = logging.getLogger(__name__)
print(__name__)
print(logger.name, type(logger), id(logger.parent), id(logger))
# __main__ <class 'logging.Logger'> 1496087048264 1496086318776

# 模块名.child是子logger
loggerchild = logging.getLogger(__name__ + '.child')
print(loggerchild.name, type(loggerchild), id(loggerchild.parent.parent), id(loggerchild.parent), id(loggerchild))
# __main__.child <class 'logging.Logger'> 1496087048264 1496086318776 1496086318664
