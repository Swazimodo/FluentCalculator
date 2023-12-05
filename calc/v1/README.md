This first approach is probably the simplest solution that accomplishes the spec but comes at the cost of type safety.
This is due to the fact that the number properties have two possible result types.
The first option is a `Calc` instance which will allow chaining, and the second is a int result.
This causes mypy to give a bunch of errors which would need to be ignored opening yourself up for real errors that should have been caught.

```
running mypy
tests\v1\test_calc.py:88: error: Item "int" of "Calc | int" has no attribute "divided_by"  [union-attr]
tests\v1\test_calc.py:96: error: Item "int" of "Calc | int" has no attribute "divided_by"  [union-attr]
tests\v1\test_calc.py:105: error: Item "int" of "Calc | int" has no attribute "divided_by"  [union-attr]
tests\v1\test_calc.py:110: error: Item "int" of "Calc | int" has no attribute "minus"  [union-attr]
tests\v1\test_calc.py:118: error: Item "int" of "Calc | int" has no attribute "minus"  [union-attr]
tests\v1\test_calc.py:126: error: Item "int" of "Calc | int" has no attribute "plus"  [union-attr]
tests\v1\test_calc.py:134: error: Item "int" of "Calc | int" has no attribute "times"  [union-attr]
```

The other issue I encountered was that when you use this chain vscode get's tripped up on the types and stops giving you proper intellisense. It looks like it knows that `new` is defined as `(property) new: (self: Self@Calc) -> Calc` but it treats it as returning `Any`. This causes it to not validate properly in the IDE or by calling mypy directly. You can type out `Calc.new.nine.asdf.three` and it will only error out at runtime.