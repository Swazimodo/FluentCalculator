# pylint: disable-next=too-few-public-methods
class ClassProperty:
    """
    Decorator that converts a method into a property that can be accessed directly from the class.
    """

    def __init__(self, method=None):
        self.fget = method

    def __get__(self, instance: None, cls=None):
        return self.fget()
