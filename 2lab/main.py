string = input('Введите строку, состоящую из латинских букв: ')
def clear(string):
    dictionary = {}
    for letter in string:
        if letter.isalpha():
            lower_letter = letter.lower()
            if lower_letter not in dictionary:
                dictionary[lower_letter] = {'lower': 0, 'upper': 0}
            if lower_letter == letter:
                dictionary[lower_letter]['lower'] += 1
            else:
                dictionary[lower_letter]['upper'] += 1
    result = []
    for letter in string:
        if not letter.isalpha():
            result.append(letter)
            continue
        lower_letter = letter.lower()
        if dictionary[lower_letter]['lower'] <= dictionary[lower_letter]['upper']:
            result.append(letter)
    return ''.join(result)
print(clear(string))
