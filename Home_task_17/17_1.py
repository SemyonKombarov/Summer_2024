def replace_doubles(some_string):
    import re
    pattern = r'(\w+)(\s+\1)+'
    return print(re.sub(pattern, r'\1', some_string))
replace_doubles("Напишите программу программу, которая устраняет повторение повторение слов, т.е. результат результат должен быть следующим")