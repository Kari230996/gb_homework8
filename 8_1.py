'''Первое задание'''

import re
import sys

RE_FULL_ADRESS = re.compile('^[A-Za-z0-9]+[.-_]*[A-Za-z0-9]+@[A-Za-z0-9-]+\.[a-z0-9]+[a-z]+') # re на полный адрес

def email_parse(email_adress):

    match = re.findall(RE_FULL_ADRESS, email_adress) # создадим переменную для вывода re полного адреса

    if '@' in email_adress:
        RE_SPLIT_EMAIL = re.split(r'@', email_adress) # делим адрес на две части
    else:
        raise ValueError(f'not an email-address: {email_adress}')

    inventory_dict = dict(username = RE_SPLIT_EMAIL[0], domen = RE_SPLIT_EMAIL[1]) # создадим словарь

    if not match:
        raise ValueError(f'strange email-address: {email_adress}')
    else:
        print(inventory_dict)

email_parse('claro.claire1996@gmail.com')

# email_parse(sys.argv[1]) # можно также выводить результат через терминал








