# pylint: skip-file
# PEP 695 generics are not yet supported by mypy or pylint
from typing import Callable, Type


# looks like a known issue that this can't be ignored https://github.com/python/mypy/issues/15238#issuecomment-1794797432
class ClassProperty[ClassT, PropertyT]:  # type: ignore [valid-type]
    """
    Decorator that converts a method into a property that can be accessed directly from the class.
    """

    def __init__(self, method: Callable[[], PropertyT]):  # type: ignore [name-defined]
        self.fget: Callable[[], PropertyT] = method  # type: ignore [name-defined]

    def __get__(self, instance: None, cls: Type[ClassT]) -> PropertyT:  # type: ignore [name-defined]
        return self.fget()
