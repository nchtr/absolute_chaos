#1
import re
with open('неприемлемые_слова.txt', 'r') as f:
    bad_words = f.read().splitlines()

with open('исходный_файл.txt', 'r') as f:
    source = f.read()

words = re.findall(r'\b\w+\b', source)

new_words = [word for word in words if word not in bad_words]

with open('новый_файл.txt', 'w') as f:
    f.write(' '.join(new_words))

#2
import transliterate
def translit_rus_to_eng(text):
    return transliterate.translit(text, reversed=True)

def translit_eng_to_rus(text):
    return transliterate.translit(text, reversed=False)

with open('input.txt', 'r') as file_input, open('output.txt', 'w') as file_output:
    print('1. Транслитерация с русского на английский')
    print('2. Транслитерация с английского на русский')
    choice = int(input('Выберите направление перевода: '))
    text = file_input.read()
    if choice == 1:
        result = translit_rus_to_eng(text)
    elif choice == 2:
        result = translit_eng_to_rus(text)
    else:
        print('Ошибка ввода')
    file_output.write(result)
#3
content = ""

while True:
    filename = input("Введите название файла или 'quit' для завершения: ")
    if filename == "quit":
        break
    try:
        with open(filename, "r") as f:
            content += f.read() 
    except FileNotFoundError:
        print("Файл не найден")

with open("result.txt", "w") as f:
    f.write(content)
#4
files = []
while True:
    filename = input("Введите название файла или 'quit' для завершения ввода: ")
    if filename == 'quit':
        break
    files.append(filename)

char_sets = []
for filename in files:
    with open(filename, 'r') as file:
        char_set = set(file.read())
        char_sets.append(char_set)

common_chars = set.intersection(*char_sets)

with open('result.txt', 'w') as file:
    file.write(''.join(common_chars))
