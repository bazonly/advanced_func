# вариант 1
def the_Collatz_sequence(start_number=1):
    num = start_number
    while True:
        if num == 1:
            yield num
        elif num % 2 == 0:
            yield num
            num = num/2
        else:
            yield num
            num = 3 * num + 1



collatz = the_Collatz_sequence(100)
while True:
    result = next(collatz)
    print(result)
    if result == 1:
        break

# вариант 2

def the_Collatz_sequence_v2(start_number):
    num = start_number

    def inner_func():
        nonlocal num
        if num == 1:
            pass
        elif num % 2 == 0:
            num = num/2
        else:
            num = 3 * num + 1
        return num
    return inner_func


# Вызов внешней функции
print()
start = 100
print(start)
collatz = the_Collatz_sequence_v2(start_number=start)

while True:
    result = collatz()
    print(result)
    if result == 1:
        break