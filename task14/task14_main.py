"""
Написать функцию, которая будет принимать одно значение - строку или список.
Необходимо зашифровать строку. Первый элемент строки - код буквы в ascii (например 'a' = 97, a 'A' = 65).
Следующий элемент - закодированная с помощью таблицы разница между текущим и предыдущим символом, итд.
Если подается список - необходимо расшифровать его. Алгоритм такой же - первое число перекодируется в соответствием с таблицей ascii,
второй символ - сумма первого и второго числа перекодированная с помощью таблицы ascii.
"""
from typing import Union, List


def run(value: Union[List[int], str]) -> Union[List[int], str]:
    if isinstance(value, list):
        result = ''
        for i in range(1, len(value)):
            local_value = value[i] + value[i - 1]
            value[i] = local_value
        for item in value:
            result += chr(item)
        return result
    else:
        local_result, result = [], []
        for item in value:
            local_result.append(ord(item))
        result.append(local_result[0])
        for i in range(1, len(local_result)):
            result.append(local_result[i] - local_result[i - 1])
        return result


print(run([72, 29, 7, 0, 3, -78, 0, 0]))
print(run("Hello!!!"))
