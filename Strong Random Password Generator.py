import random
digits = [c for c in '0123456789']
lowercase_letters = [chr(c) for c in range(ord('a'), ord('z') + 1)]
uppercase_letters = [c.upper() for c in lowercase_letters];
punctuation = [c for c in '!#$%&*+-=?@^_']

print('Добро пожаловать в Генератор паролей!')
number_of_passwords = int(input('Укажите количество паролей для генерации: '))
length = int(input('Укажите длину одного пароля: '))
need_digits = input('Пароль должен содержать цифры? Введите "+" (да) или "-" (нет): ')
need_uppercase = input('Пароль должен содержать заглавные буквы? Введите "+" (да) или "-" (нет): ')
need_lowercase = input('Пароль должен содержать строчные буквы? Введите "+" (да) или "-" (нет): ')
need_punctuation = input('Пароль должен содержать символы !#$%&*+-=?@^_? Введите "+" (да) или "-" (нет): ')
need_symbols = input('Пароль должен содержать неоднозначные символы il1Lo0O? Введите "+" (да) или "-" (нет): ')

if need_symbols != '+':
    digits = digits[2:]
    del lowercase_letters[lowercase_letters.index('i')], lowercase_letters[lowercase_letters.index('l')], lowercase_letters[lowercase_letters.index('o')], uppercase_letters[uppercase_letters.index('L')], uppercase_letters[uppercase_letters.index('O')]

        
def generate_password(length, digits, need_digits, lowercase_letters, need_lowercase, uppercase_letters, need_uppercase, punctuation, need_punctuation):
    x = length // 4
    password = random.sample(digits, x) * (need_digits == '+') + random.sample(lowercase_letters, (x + length % 4)) * (need_lowercase == '+') + random.sample(uppercase_letters, x) * (need_uppercase == '+') + random.sample(punctuation, x) * (need_punctuation == '+')
    random.shuffle(password)
    return ''.join(password)

for _ in range(number_of_passwords):
    print(generate_password(length, digits, need_digits, lowercase_letters, need_lowercase, uppercase_letters, need_uppercase, punctuation, need_punctuation))