


# 通过改变实例创建方法来实现单例、缓存或其他类似的特性


class Spam:
    def __init__(self, name):
        self.name = name

a = Spam('tom')
b = Spam('jerry')


class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError('Cant instantiate directly')

class Spam(metaclass=NoInstance):
    @staticmethod
    def grok(x):
        print('Spam.grok')


# 实现单例模式即只能创建唯一实例的类

class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')