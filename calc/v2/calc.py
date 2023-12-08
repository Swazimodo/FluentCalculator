from __future__ import annotations
from typing import Optional
from enum import Enum
from math import floor

from calc.v2.classproperty import ClassProperty


class Operation(Enum):
    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIVIDED_BY = 4


class Calc:
    def __init__(self) -> None:
        self._accumulator: int = 0
        self._operation: Optional[Operation] = None

    @ClassProperty
    # @ClassProperty makes this a static property so there is not a `self`
    def new() -> Calc:  # type: ignore [misc]
        return Calc()

    @property
    def result(self) -> int:
        self._operation = None
        return self._accumulator

    def __process_value(self, value: int) -> None:
        """
        Check for a pending operation.
        If one exists perform it against the current accumulator and the value property.
        The result is then saved back into the accumulator.
        """
        if self._operation is None:
            self._accumulator = value
            return

        if self._operation is Operation.DIVIDED_BY:
            # this package is expected to deal with only integers but division will return a float
            # we are going to use integer division and drop and decimals with the `floor` function
            self._accumulator = floor(self._accumulator / value)
        elif self._operation is Operation.MINUS:
            self._accumulator = self._accumulator - value
        elif self._operation is Operation.PLUS:
            self._accumulator = self._accumulator + value
        elif self._operation is Operation.TIMES:
            self._accumulator = self._accumulator * value

        # a calculation has completed and the operation is reset
        self._operation = None

    # operations calculator can perform
    @property
    def plus(self) -> Calc:
        self._operation = Operation.PLUS
        return self

    @property
    def minus(self) -> Calc:
        self._operation = Operation.MINUS
        return self

    @property
    def times(self) -> Calc:
        self._operation = Operation.TIMES
        return self

    @property
    def divided_by(self) -> Calc:
        self._operation = Operation.DIVIDED_BY
        return self

    # values
    @property
    def zero(self) -> Calc:
        self.__process_value(0)
        return self

    @property
    def one(self) -> Calc:
        self.__process_value(1)
        return self

    @property
    def two(self) -> Calc:
        self.__process_value(2)
        return self

    @property
    def three(self) -> Calc:
        self.__process_value(3)
        return self

    @property
    def four(self) -> Calc:
        self.__process_value(4)
        return self

    @property
    def five(self) -> Calc:
        self.__process_value(5)
        return self

    @property
    def six(self) -> Calc:
        self.__process_value(6)
        return self

    @property
    def seven(self) -> Calc:
        self.__process_value(7)
        return self

    @property
    def eight(self) -> Calc:
        self.__process_value(8)
        return self

    @property
    def nine(self) -> Calc:
        self.__process_value(9)
        return self
