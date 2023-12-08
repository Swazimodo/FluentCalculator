Here I iterated on my initial design to improve type safety.
First I fixed the ClassProperty decorator using the new generic syntax in python 3.12.
Before you would have had to use `TypeVar` and `Generic` to do this but now it's much simpler.
The result of this is that it is able to see the types past `new` in the chain.

The second change I also modified the spec slightly and moves in the direction of the builder pattern with the addition of `result`.
Calling the value properties will always return `self` for easy chaining which provides a couple advantages.
First off you have type safety in the chain and no longer see errors from the union return type.
This would keep users from needing to add type ignores in their code helping move more errors to be caught at build time.
The second advantage is that the calculation is not completed when the second number is entered allowing for more complex equations.
```
Calc.new.three.plus.two.minus.one.result (result: 4)
```

While this does unlock new functionality the design would then need to clarify how order of operations will be handled. Currently it will execute left to right as you would expect in a simple calculator.
Scientific calculators on the other hand, would evaluate the entire equation at once but that would bring additional complexity.
```
# the equation is executed left to right causing the addition to happen before multiplication
# (3 + 2) * 2 == 10  # right to left
# 3 + (2 * 2) == 7   # order of operations
Calc.new.three.plus.two.times.two.result (result: 10)
```

I tried seeing if you could take this farther to unlock any integer instead of 0-9
`Calc.new.3.plus.2.result (result: 5)`
but that experiment failed.
```
class DynamicAttributes:
    def __init__(self) -> None:
        # Cannot have attribute names starting with a number
        # self.1 = 1

        # I tried forcing a number attribute into the class's internal dict
        # but this is not accessible unless you also access it this way
        # because it runs into the same limitation that attribute names can't
        # start with a number
        self.__dict__["1"] = 1

    def __getattr__(self, attr):
        # If it was possible to access number named attributes
        # you could do something like this to dynamically parse them into numbers.
        # However, even if this did work it would not allow you to have type safety
        # as this is a runtime hack
        return int(attr)
```
