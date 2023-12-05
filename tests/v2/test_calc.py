import pytest

from calc.v2 import Calc
from calc.v2.calc import Operation


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
        assert Calc.new._accumulator == 0

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

    def test_number_setNumber_shouldReturnSelf(self) -> None:
        assert isinstance(Calc.new.one, Calc)


class Test_SetOperation:
    def test_operation_defaultOperation_shouldBeNone(self) -> None:
        assert Calc.new._operation is None

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
        assert isinstance(Calc.new.divided_by, Calc)


class Test_ExecuteOperation:
    def test_divideBy_twoNumbersWithIntegerResult_shouldReturnIntResult(self) -> None:
        result = Calc.new.two.divided_by.two.result

        assert result == 1
        assert isinstance(result, int)

    def test_divideBy_twoNumbersWithRationalNumberResult_shouldReturnIntResult(
        self,
    ) -> None:
        result = Calc.new.five.divided_by.three.result

        assert result == 1
        assert isinstance(result, int)

    def test_divideBy_divideByZero_shouldRaiseException(self) -> None:
        with pytest.raises(ZeroDivisionError):
            Calc.new.five.divided_by.zero.result

    def test_minus_subtractTwoNumbers_shouldReturnIntResult(self) -> None:
        result = Calc.new.five.minus.one.result

        assert result == 4
        assert isinstance(result, int)

    def test_minus_subtractTwoNumbersWithNegativeResult_shouldReturnIntResult(
        self,
    ) -> None:
        result = Calc.new.one.minus.five.result

        assert result == -4
        assert isinstance(result, int)

    def test_plus_addTwoNumbers_shouldReturnIntResult(self) -> None:
        result = Calc.new.one.plus.one.result

        assert result == 2
        assert isinstance(result, int)

    def test_times_multiplyTwoNumbers_shouldReturnIntResult(self) -> None:
        instance: Calc = Calc.new

        result = instance.five.times.three.result

        assert result == 15
        assert isinstance(result, int)


def test_SampleTestCasesInSpec() -> None:
    assert Calc.new.one.plus.two.result == 3
    assert Calc.new.five.minus.six.result == -1
    assert Calc.new.seven.times.two.result == 14
    assert Calc.new.nine.divided_by.three.result == 3


def test_multipleOperations_inconsequentialOrdering_returnsResult() -> None:
    assert Calc.new.three.plus.two.minus.one.result == 4


def test_multipleOperations_consequentialOrdering_returnsResultFromRightToLeftExecution() -> (
    None
):
    # the equation is executed left to right causing the addition to happen before multiplication
    # (3 + 2) * 2 == 10  # right to left
    # 3 + (2 * 2) == 7   # order of operations
    assert Calc.new.three.plus.two.times.two.result == 10
