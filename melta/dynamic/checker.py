callable = lambda x: hasattr(x, "__call__")
anything = lambda x: True
nothing = lambda x: x is None
iterable = lambda x: hasattr(x,"__iter__")

class TypeCheckError(Exception): pass
class TypeCheckSpecificationError(Exception): pass
class InputParameterError(TypeCheckError): pass
class ReturnValueError(TypeCheckError): pass


class Checker(object):

    def __call__(self, value):
        return self.check(value)