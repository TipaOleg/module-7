

def custom_write(file_name, strings):
    strings_position = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for line_num, string in enumerate(strings, start=1):
            position = file.tell()
            file.write(string + '\n')
            strings_position[(line_num, position)] = string

    return strings_position

info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

    ]



result = custom_write('test.txt', info)

for elem in result.items():

  print(elem)