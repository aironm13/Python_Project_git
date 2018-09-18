class A:
    # 定义类的__new__方法
    """
    1,使用__new__魔术方法在构造类的实例，添加一个属性_instance
    缺点：不能构造第二个类，否则抛出异常
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            setattr(cls, '_instance', super().__new__(cls))
            setattr(cls, '_count', 0)
        return cls._instance

    def __init__(self, url, debug):
        if self._count == 0:
            self.url = url
            self.debug = debug
            self.__class__._count = 1
        else:
            raise Exception('Just One Instance')

    def __repr__(self):
        return F"<B {self.url} {self.debug}>"


if __name__ == '__main__':
    # 测试
    s1 = A(url='http://www.baidu.com', debug=True)
    s2 = A(url='http://www.qq.com', debug=False)
    print(s1)
    print(s2)