from __future__ import annotations
from typing import Optional
from enum import Enum
from math import floor


class Operation(Enum):
    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIVIDED_BY = 4


class CalculatorFactory:
    def __init__(self) -> None:
        self.fget = lambda: CalculatorStart()

    def __get__(self, instance: None, cls: object) -> CalculatorStart:
        return self.fget()


class Calc:
    new = CalculatorFactory()


class CalculatorStart:
    """
    Responsible for collecting the first value and an operation to perform on that value
    """

    def __init__(self) -> None:
        self._accumulator: Optional[int] = None
        self._operation: Optional[Operation] = None

    def _set_value(self, value: int) -> None:
        if self._accumulator is not None:
            raise AttributeError("The value cannot be changed once defined")
        self._accumulator = value

    def _set_operation(self, operation: Operation) -> None:
        if self._accumulator is None:
            raise ReferenceError("A value needs to be set before defining an operation")
        self._operation = operation

    def _get_calc_final(self) -> CalculatorFinal:
        if self._accumulator is not None and self._operation is not None:
            return CalculatorFinal(self._accumulator, self._operation)
        raise ValueError("undefined accumulator or operation")

    # operations calculator can perform
    @property
    def plus(self) -> CalculatorFinal:
        self._set_operation(Operation.PLUS)
        return self._get_calc_final()

    @property
    def minus(self) -> CalculatorFinal:
        self._set_operation(Operation.MINUS)
        return self._get_calc_final()

    @property
    def times(self) -> CalculatorFinal:
        self._set_operation(Operation.TIMES)
        return self._get_calc_final()

    @property
    def divided_by(self) -> CalculatorFinal:
        self._set_operation(Operation.DIVIDED_BY)
        return self._get_calc_final()

    # values
    @property
    def zero(self) -> CalculatorStart:
        self._set_value(0)
        return self

    @property
    def one(self) -> CalculatorStart:
        self._set_value(1)
        return self

    @property
    def two(self) -> CalculatorStart:
        self._set_value(2)
        return self

    @property
    def three(self) -> CalculatorStart:
        self._set_value(3)
        return self

    @property
    def four(self) -> CalculatorStart:
        self._set_value(4)
        return self

    @property
    def five(self) -> CalculatorStart:
        self._set_value(5)
        return self

    @property
    def six(self) -> CalculatorStart:
        self._set_value(6)
        return self

    @property
    def seven(self) -> CalculatorStart:
        self._set_value(7)
        return self

    @property
    def eight(self) -> CalculatorStart:
        self._set_value(8)
        return self

    @property
    def nine(self) -> CalculatorStart:
        self._set_value(9)
        return self


class CalculatorFinal:
    """
    Collects the final value in the equation and calculates the result
    """

    def __init__(self, accumulator: int, operation: Operation) -> None:
        self._accumulator: int = accumulator
        self._operation: Operation = operation

    def __process_value(self, value: int) -> int:
        """
        Perform the set operation against the current accumulator and the new property value
        """
        if self._operation is Operation.DIVIDED_BY:
            # this package is expected to deal with only integers but division will return a float
            # we are going to use integer division and drop and decimals with the `floor` function
            return floor(self._accumulator / value)
        elif self._operation is Operation.MINUS:
            return self._accumulator - value
        elif self._operation is Operation.PLUS:
            return self._accumulator + value
        elif self._operation is Operation.TIMES:
            return self._accumulator * value
        raise AttributeError("An invalid operation type has been specified")

    # values
    @property
    def zero(self) -> int:
        return self.__process_value(0)

    @property
    def one(self) -> int:
        return self.__process_value(1)

    @property
    def two(self) -> int:
        return self.__process_value(2)

    @property
    def three(self) -> int:
        return self.__process_value(3)

    @property
    def four(self) -> int:
        return self.__process_value(4)

    @property
    def five(self) -> int:
        return self.__process_value(5)

    @property
    def six(self) -> int:
        return self.__process_value(6)

    @property
    def seven(self) -> int:
        return self.__process_value(7)

    @property
    def eight(self) -> int:
        return self.__process_value(8)

    @property
    def nine(self) -> int:
        return self.__process_value(9)
