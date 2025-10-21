

import re
from collections import Counter
string_s = input('Введите предложение: ')
d1 = string_s.split()
def preobr_char():
    string_1 = string_s.lower()
    d = [x for x in string_1 if x.isalpha()]
    return d
chars = preobr_char()
def fdch():
    counter_1 = Counter(chars)
    popular_chars = counter_1.most_common(5)
    print('5 самых популярных букв:\nБуква 1, количество раз:', popular_chars[0],'\nБуква 2, количество раз:', popular_chars[1],'\nБуква 3, количество раз:', popular_chars[2],'\nБуква 4, количество раз:', popular_chars[3], '\nБуква 5, количество раз:', popular_chars[4])

def preobr_word():
    d1 = re.findall(r'\b\w+\b', string_s.lower())
    return d1
words = preobr_word()
def fdwd():
    counter_2 = Counter(words)
    popular_words = counter_2.most_common(5)
    print('5 самых популярных слов:\nСлово 1, количество раз:',
          popular_words[0],'\nСлово 2, количество раз:', popular_words[1],
          '\nСлово 3, количество раз:', popular_words[2],'\nСлово 4, количество раз:',
          popular_words[3],
          '\nСлово 5, количество раз:', popular_words[4])
    


fdch()
fdwd()
