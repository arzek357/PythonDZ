# coding=utf-8
"""
Создайте функцию для выполнения основных арифметических операций, которая применяет сложение,
вычитание, умножение и деление к строковому значению (например, "12 + 24" или "23-21" или "12 // 12" или "12 * 21").
Здесь у нас есть 1 число, за которым следует пробел, затем оператор, за которым следует другой пробел, и 2 число.
Возвращаемое значение должно быть числом.
Применение функции eval() не допускается.
В случае деления, всякий раз, когда второе число равно "0", возвращайте -1.
"""


def test_function(operation: str):
    args = operation.split()
    number1 = float(args[0])
    number2 = float(args[2])

    if args[1] == '+':
        return number1 + number2
    if args[1] == '-':
        return number1 - number2
    if args[1] == '*':
        return number1 * number2
    if args[1] == '//':
        if number2 == 0:
            return -1
        return number1 / number2


print(test_function("32 + 3"))
print(test_function("31 - 3"))
print(test_function("31 * 3"))
print(test_function("33 // 3"))
print(test_function("33 // 0"))
