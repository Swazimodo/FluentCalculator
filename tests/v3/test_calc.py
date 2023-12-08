import pytest

from calc.v3 import Calc
from calc.v3.calc import CalculatorStart, CalculatorFinal, Operation


class Test_ClassPropertyFactory:
    def test_new_callingStaticPropertyFactory_shouldReturnCalculatorStartInstance(
        self,
    ) -> None:
        instance: CalculatorStart = Calc.new

        assert isinstance(instance, CalculatorStart)

    def test_new_calledTwice_shouldReturnDifferentInstances(self) -> None:
        first_instance: CalculatorStart = Calc.new
        second_instance: CalculatorStart = Calc.new
        assert first_instance is not second_instance


class Test_SetNumber:
    def test_number_defaultFirstValue_shouldBeNone(self) -> None:
        assert Calc.new._accumulator is None

    def test_number_setNumber_shouldSetAccumulator(self) -> None:
        assert Calc.new.one._accumulator == 1
        assert Calc.new.two._accumulator == 2
        assert Calc.new.three._accumulator == 3
        assert Calc.new.four._accumulator == 4
        assert Calc.new.five._accumulator == 5
        assert Calc.new.six._accumulator == 6
        assert Calc.new.seven._accumulator == 7
        assert Calc.new.eight._accumulator == 8
        assert Calc.new.nine._accumulator == 9
        assert Calc.new.zero._accumulator == 0

    def test_number_setNumberTwice_shouldRaiseError(self) -> None:
        with pytest.raises(AttributeError):
            Calc.new.one.one

    def test_number_setNumber_shouldReturnSelf(self) -> None:
        assert isinstance(Calc.new.one, CalculatorStart)


class Test_SetOperation:
    def test_operation_defaultOperation_shouldBeNone(self) -> None:
        assert Calc.new._operation is None

    def test_operation_setOperationBeforeValue_shouldRaiseError(self) -> None:
        with pytest.raises(ReferenceError):
            Calc.new.plus

    def test_operation_setMultipleOperations_shouldOverwriteOperation(self) -> None:
        assert Calc.new.one.divided_by._operation is Operation.DIVIDED_BY
        assert Calc.new.one.minus._operation is Operation.MINUS
        assert Calc.new.one.plus._operation is Operation.PLUS
        assert Calc.new.one.times._operation is Operation.TIMES

    def test_operation_setOperation_shouldReturnCalculatorFinal(self) -> None:
        assert isinstance(Calc.new.one.plus, CalculatorFinal)


class Test_ExecuteOperation:
    def test_divideBy_twoNumbersWithIntegerResult_shouldReturnIntResult(self) -> None:
        result = Calc.new.two.divided_by.two

        assert result == 1
        assert isinstance(result, int)

    def test_divideBy_twoNumbersWithRationalNumberResult_shouldReturnIntResult(
        self,
    ) -> None:
        result = Calc.new.five.divided_by.three

        assert result == 1
        assert isinstance(result, int)

    def test_divideBy_divideByZero_shouldRaiseException(self) -> None:
        with pytest.raises(ZeroDivisionError):
            Calc.new.five.divided_by.zero

    def test_minus_subtractTwoNumbers_shouldReturnIntResult(self) -> None:
        result = Calc.new.five.minus.one

        assert result == 4
        assert isinstance(result, int)

    def test_minus_subtractTwoNumbersWithNegativeResult_shouldReturnIntResult(
        self,
    ) -> None:
        result = Calc.new.one.minus.five

        assert result == -4
        assert isinstance(result, int)

    def test_plus_addTwoNumbers_shouldReturnIntResult(self) -> None:
        result = Calc.new.one.plus.one

        assert result == 2
        assert isinstance(result, int)

    def test_times_multiplyTwoNumbers_shouldReturnIntResult(self) -> None:
        result = Calc.new.five.times.three

        assert result == 15
        assert isinstance(result, int)


def test_SampleTestCasesInSpec() -> None:
    assert Calc.new.one.plus.two == 3
    assert Calc.new.five.minus.six == -1
    assert Calc.new.seven.times.two == 14
    assert Calc.new.nine.divided_by.three == 3
