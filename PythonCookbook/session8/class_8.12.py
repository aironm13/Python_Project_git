

# 定义一个接口或抽象类，通过执行类型检查来确保子类实现某些特定的方法

# 解决：使用abc模块

from abc import ABCMeta, abstractmethod

# 元编程;通过代码生成代码
class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass
# 抽象类的一个特点是它不能直接被实例化

# 抽象类的目的就是让别的类继承它并实现特定的抽象方法：
class SockeStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass

def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    pass


