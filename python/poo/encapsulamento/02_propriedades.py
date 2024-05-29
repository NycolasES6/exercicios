class Foo:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        _x = self._x
        _value = value
        self._x = _x + _value

    @x.deleter
    def x(self):
        self._x = -1


foo = Foo(20)
print(foo.x)
foo.x = 40
print(foo.x)
del foo.x
print(foo.x)
