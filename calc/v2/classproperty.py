from typing import Callable, Type


class ClassProperty[ClassT, PropertyT]:
    """
    Decorator that converts a method with a single cls argument into a property
    that can be accessed directly from the class.
    """

    def __init__(self, method: Callable[[], PropertyT]):
        self.fget: Callable[[Type[ClassT]], PropertyT] = method

    def __get__(self, instance: None, cls: Type[ClassT]) -> PropertyT:
        return self.fget(cls)
