For this final version I wanted to create a solution that exactly solved the assignment without any compromises from a linting or type checking perspective.
It removed the generics because support was not yet fully there from both pylint and mypy. This is an ok compromise because the generic function was only ever used once.
We are not causing any additional code duplication here from making it more tailored to the task at hand.
The classes were also split up because the first time you set a number it needs to return a chainable class value the last time you do so it has to return an int.
By splitting up the classes we can have different implementations of those two calls.