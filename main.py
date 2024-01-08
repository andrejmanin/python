def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

try:
    num = int(input("Введіть число: "))
    if num < 0:
        raise ValueError("Факторіал від'ємного числа не визначений")

    result = factorial(num)
    print(f"Факторіал {num} = {result}")

except ValueError as e:
    print(f"Помилка: {e}")