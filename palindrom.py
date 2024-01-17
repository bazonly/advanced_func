# вариант 1

my_list = ['radar', 'level', 'racecar', 'deified', 'бабайка', 'серега']
palindrome_list = list(filter(lambda x: (str(x).lower() == str(x[::-1]).lower()) , my_list))
print(palindrome_list)

# вариант 2

def palinrdome(check_list: list):
    new_list = []
    for item in check_list:
        is_palindrome = lambda x: str(x).lower() == str(x[::-1]).lower()
        if is_palindrome(item):
            new_list.append(item)
    return new_list

my_list = ['radar', 'level', 'racecar', 'deified', 'бабайка', 'серега']

new_list = palinrdome(my_list)
print(new_list)