import math


class BaseCalculator:
    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def plus(*args: int | float) -> int:
        '''Returns summarized value of passed numbers'''
        return sum(args)

    @staticmethod
    def minus(first: int, second: int) -> int:
        '''Returns subtracted value'''
        if not isinstance(first, int):
            raise TypeError(f"unsupported operand type(s) for -: 'int' and '{first.__class__.__name__}'")
        if not isinstance(second, int):
            raise TypeError(f"unsupported operand type(s) for -: 'int' and '{second.__class__.__name__}'")
        return first - second

    @staticmethod
    def multiply(*args: int | float) -> int:
        '''Return the multiplied value of passed values'''
        result = 1
        for num in args:
            if not isinstance(num, int):
                raise TypeError(f"unsupported operand type(s) for *: 'int' and '{num.__class__.__name__}'")
            result *= num
        return result

    @staticmethod
    def power(number: int, power: int) -> int | float:
        '''Powers and returns the result'''
        if not isinstance(number, int):
            raise TypeError(f"unsupported operand type(s) for **: 'int' and '{number.__class__.__name__}'")
        if not isinstance(power, int):
            raise TypeError(f"unsupported operand type(s) for **: 'int' and '{power.__class__.__name__}'")
        return math.pow(number, power)

    @staticmethod
    def division(first: float | int, second: float | int) -> float:
        '''Divides and returns the result'''
        if not isinstance(first, int):
            raise TypeError(f"unsupported operand type(s) for /: 'int' and '{first.__class__.__name__}'")
        if not isinstance(second, int):
            raise TypeError(f"unsupported operand type(s) for /: 'int' and '{second.__class__.__name__}'")
        return first / second

    @staticmethod
    def whole_division(first: int, second: int) -> int:
        '''Divides, drops the decimal part and returns the result'''
        if not isinstance(first, int):
            raise TypeError(f"unsupported operand type(s) for //: 'int' and '{first.__class__.__name__}'")
        if not isinstance(second, int):
            raise TypeError(f"unsupported operand type(s) for //: 'int' and '{second.__class__.__name__}'")
        return first // second

    @staticmethod
    def find_remainder_division(first: int, second: int) -> int:
        '''Divides, and returns the remainder part from division'''
        if not isinstance(first, int):
            raise TypeError(f"unsupported operand type(s) for %: 'int' and '{first.__class__.__name__}'")
        if not isinstance(second, int):
            raise TypeError(f"unsupported operand type(s) for %: 'int' and '{second.__class__.__name__}'")
        return first % second

    def __str__(self) -> str:
        return self.name


if __name__ == '__main__':
    obj = BaseCalculator("My Calculator")
    print(obj.plus(5, 3))  # 8
    print(obj.minus(5, 3))  # 2
    print(obj.power(5, 3))  # 125.0
    print(obj.find_remainder_division(5, 3))  # 2
    print(obj.whole_division(5, 3))  # 1
    print(obj.multiply(5, 3))  # 15
    print(obj.division(5, 3))  # 1.6666666666666667





