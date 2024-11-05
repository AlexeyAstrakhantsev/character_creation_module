from math import sqrt

message = """Добро пожаловать в самую лучшую программу
          для вычисления квадратного корня из заданного числа"""
print(message)


def CalculateSquareRoot(number: float) -> float:
    """ Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number):
    if your_number <= 0:
        return
    squareroot = CalculateSquareRoot(your_number)
    print(f"Мы вычислили квадратный корень из введённого вами числа. "
          f"Это будет: {squareroot}")


print(message)
calc(25.5)
