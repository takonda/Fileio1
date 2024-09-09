from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import ttk
import requests
import pyperclip
import json
import os

history_file = 'upload_history.json'


def save_history(file_path, link):
    history = []
    if os.path. exists(history_file): # проверяе, что history_file существует в папке
        with open(history_file, 'r') as f:
            history = json.load(f)
    history.append({'file_path': os.path.basename(file_path), 'download_link': link})
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=4)

def upload():
    try:
        filepath = fd.askopenfilename() # открывает окно для выбора файла
        if filepath: # если переменная не пустая, т.е. файл найден
            with open(filepath, 'rb') as f:
                files = {'file': f} # открывает файл в режиме чтени побайтно
                response = requests.post('https://file.io', files=files)
                response.raise_for_status() # позволяет проверить не было ли ошибок
                link = response.json() ['link'] # в линк придет ссылка для скачивания
                entry.delete(0, END) # очищает поле ввода
                entry.insert(0, link) # вводит ссылку на сайт
                pyperclip.copy(link) # добавляет ссылку для скачивания в буфер обмена
                save_history(filepath, link)
                mb.showinfo('Ссылка скопирована', f'Ссылка {link} успешно скопирована в буфер обмена')
    except Exception as e:
        mb.showerror('Ошибка', 'Произошла ошибка: {e}')

window = Tk()
window.title('Сохранение файлов в облаке')
window.geometry('400x200')

button = ttk.Button(text='Загрузить файл', command=upload)
button.pack()

entry = ttk.Entry()
entry.pack()

window.mainloop()
