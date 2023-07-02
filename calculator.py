num_1 = input("Введите первое число: ")
num_2 = input("Введите второе число: ")
math = input("Введите математическую функцию: ")

try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    if math == "+":
        result = int(num_1+num_2)
    else:
        if math == "-":
            result = int(num_1 - num_2)
        else:
            if math == "*":
                result = int(num_1 * num_2)
            else:
                if math == "/":
                    result = int(num_1 / num_2)
                else:
                    print("Такой функции нет")
except ZeroDivisionError:
    result = 0
    print("На 0 делить нельзя")
except ValueError:
    print("Введено не число")
    exit()

print("Результат: " + str(result))