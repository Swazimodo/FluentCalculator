from __future__ import annotations
from typing import Optional, Union
from enum import Enum
from math import floor

from calc.v1.classproperty import classproperty


class Operation(Enum):
    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIVIDED_BY = 4


class Calc:
    def __init__(self) -> None:
        self._accumulator: int = 0
        self._operation: Optional[Operation] = None

    @classproperty
    def new(self) -> Calc:
        return Calc()

    def __process_value(self, value: int) -> Union[Calc, int]:
        """
        Check for a pending operation.
        If one exists perform it against the current accumulator and the value property.
        The result is then saved back into the accumulator.
        """
        if self._operation is None:
            self._accumulator = value
            return self

        if self._operation is Operation.DIVIDED_BY:
            self._accumulator = floor(self._accumulator / value)
        elif self._operation is Operation.MINUS:
            self._accumulator = self._accumulator - value
        elif self._operation is Operation.PLUS:
            self._accumulator = self._accumulator + value
        elif self._operation is Operation.TIMES:
            self._accumulator = self._accumulator * value
        return self._accumulator

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
    def zero(self) -> Union[Calc, int]:
        return self.__process_value(0)

    @property
    def one(self) -> Union[Calc, int]:
        return self.__process_value(1)

    @property
    def two(self) -> Union[Calc, int]:
        return self.__process_value(2)

    @property
    def three(self) -> Union[Calc, int]:
        return self.__process_value(3)

    @property
    def four(self) -> Union[Calc, int]:
        return self.__process_value(4)

    @property
    def five(self) -> Union[Calc, int]:
        return self.__process_value(5)

    @property
    def six(self) -> Union[Calc, int]:
        return self.__process_value(6)

    @property
    def seven(self) -> Union[Calc, int]:
        return self.__process_value(7)

    @property
    def eight(self) -> Union[Calc, int]:
        return self.__process_value(8)

    @property
    def nine(self) -> Union[Calc, int]:
        return self.__process_value(9)
