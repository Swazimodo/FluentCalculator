import pytest

from calc.v1 import Calc
from calc.v1.calc import Operation


class Test_ClassPropertyFactory:
    def test_new_callingStaticPropertyFactory_shouldReturnCalcInstance(self) -> None:
        instance: Calc = Calc.new

        assert instance is not None
        assert isinstance(instance, Calc)

    def test_new_calledTwice_shouldReturnDifferentInstances(self) -> None:
        first_instance: Calc = Calc.new
        second_instance: Calc = Calc.new
        assert first_instance is not second_instance


class Test_SetNumber:
    def test_new_defaultAccumulatorValue_shouldBeZero(self) -> None:
        instance: Calc = Calc.new

        assert instance._accumulator == 0

    def test_number_setNumberWithoutOperation_shouldOverwriteAccumulator(self) -> None:
        instance: Calc = Calc.new

        instance.one
        assert instance._accumulator == 1
        instance.two
        assert instance._accumulator == 2
        instance.three
        assert instance._accumulator == 3
        instance.four
        assert instance._accumulator == 4
        instance.five
        assert instance._accumulator == 5
        instance.six
        assert instance._accumulator == 6
        instance.seven
        assert instance._accumulator == 7
        instance.eight
        assert instance._accumulator == 8
        instance.nine
        assert instance._accumulator == 9
        instance.zero
        assert instance._accumulator == 0

    def test_number_setNumberWithoutOperation_shouldReturnSelf(self) -> None:
        instance: Calc = Calc.new

        getter = instance.one

        assert isinstance(getter, Calc)


class Test_SetOperation:
    def test_operation_defaultOperation_shouldBeNone(self) -> None:
        instance: Calc = Calc.new

        assert instance._operation is None

    def test_operation_setMultipleOperations_shouldOverwriteOperation(self) -> None:
        instance: Calc = Calc.new

        instance.divided_by
        assert instance._operation is Operation.DIVIDED_BY
        instance.minus
        assert instance._operation is Operation.MINUS
        instance.plus
        assert instance._operation is Operation.PLUS
        instance.times
        assert instance._operation is Operation.TIMES

    def test_operation_setOperation_shouldReturnSelf(self) -> None:
        instance: Calc = Calc.new

        getter = instance.divided_by

        assert isinstance(getter, Calc)


class Test_ExecuteOperation:
    def test_divideBy_twoNumbersWithIntegerResult_shouldReturnIntResult(self) -> None:
        instance: Calc = Calc.new

        result = instance.two.divided_by.two  # type: ignore

        assert result == 1
        assert isinstance(result, int)

    def test_divideBy_twoNumbersWithRationalNumberResult_shouldReturnIntResult(
        self,
    ) -> None:
        instance: Calc = Calc.new

        result = instance.five.divided_by.three  # type: ignore

        assert result == 1
        assert isinstance(result, int)

    def test_divideBy_divideByZero_shouldRaiseException(self) -> None:
        instance: Calc = Calc.new

        with pytest.raises(ZeroDivisionError):
            instance.five.divided_by.zero  # type: ignore

    def test_minus_subtractTwoNumbers_shouldReturnIntResult(self) -> None:
        instance: Calc = Calc.new

        result = instance.five.minus.one  # type: ignore

        assert result == 4
        assert isinstance(result, int)

    def test_minus_subtractTwoNumbersWithNegativeResult_shouldReturnIntResult(
        self,
    ) -> None:
        instance: Calc = Calc.new

        result = instance.one.minus.five  # type: ignore

        assert result == -4
        assert isinstance(result, int)

    def test_plus_addTwoNumbers_shouldReturnIntResult(self) -> None:
        instance: Calc = Calc.new

        result = instance.one.plus.one  # type: ignore

        assert result == 2
        assert isinstance(result, int)

    def test_times_multiplyTwoNumbers_shouldReturnIntResult(self) -> None:
        instance: Calc = Calc.new

        result = instance.five.times.three  # type: ignore

        assert result == 15
        assert isinstance(result, int)


def test_SampleTestCasesInSpec() -> None:
    assert Calc.new.one.plus.two == 3
    assert Calc.new.five.minus.six == -1
    assert Calc.new.seven.times.two == 14
    assert Calc.new.nine.divided_by.three == 3

    # this should fail from a type check but it doesn't
    # assert Calc.new.nine.asdf.three == 0
