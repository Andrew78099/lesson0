import io

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    s = 0
    for items in info:
        a = file.tell()
        s += 1
        file.write(items + '\n')
        print(f'({s},{a}),{items}')
    file.close()

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)