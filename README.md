# Fluent Calculator
The Kata is inspired by the “Calculating with Functions Kata for JavaScript” on codewars.
The goal is to implement a simple calculator which uses fluent syntax:
```
Calc.new.one.plus.two (result: 3)
Calc.new.five.minus.six (result: -1)
Calc.new.seven.times.two (result: 14)
Calc.new.nine.divided_by.three (result: 3)
```

There are only four operations that are supported (plus, minus, times, divided_by) and 10 digits (zero, one, two, three, four, five, six, seven, eight, nine).
Each calculation consists of one operation only and will return an integer.
Note: This is not a string parsing problem. The calls above are a chain of methods. Some languages may require parenthesis in method
calls. That is OK, but consider a different language what would support the above syntax if possible.