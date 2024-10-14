import os

# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
directory = '.'
for i in os.walk(directory):
    print(i)

# Примените os.path.join для формирования полного пути к файлам.
with os.scandir(directory) as files:
    for file in files:
        if file.is_file():
            print(os.path.join(directory, file.name))

# Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
filename = "ter.txt"
m_time = os.path.getmtime(filename)
print(m_time)

# Используйте os.path.getsize для получения размера файла

filename = "ter.txt"
r_file = os.path.getsize(filename)
print(r_file)

# Используйте os.path.dirname для получения родительской директории файла.

mypath = "/Users/user/PycharmProjects/pythonProject4/.venv/bin/python /Users/user/PycharmProjects/pythonProject4/direct.py"
parent = os.path.abspath(os.path.join(mypath, '..'))
print(parent)

print(f'Обнаружен файл: {file}, Путь: {i}, Размер: {r_file} байт, Время изменения: {m_time}, Родительская директория: {parent}')

