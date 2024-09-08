from http.client import responses
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import requests


def upload():
    filepath = fd.askopenfilename() # открывает окно для выбора файла
    if filepath: # если переменная не пустая, т.е. файл найден
        files = {'file': open(filepath, 'rb')} # открывает файл в режиме чтени побайтно
        response = requests.post('https://file.io', files=files)
        if response.status_code == 200: # этот код означает, что все в порядке
            link = response.json() ['link'] # в линк придет ссылка для скачивания
            entry.insert(0, link)

window = Tk()
window.title('Сохранение файлов в облаке')
window.geometry('400x200')

button = ttk.Button(text='Загрузить файл', command=upload)
button.pack()

entry = ttk.Entry()
entry.pack()

window.mainloop()
