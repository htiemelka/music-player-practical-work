from tkinter import *
import tkinter as tk
import webbrowser
import datetime
from playsound import playsound

# Получаем текущую дату и время
currentDate = datetime.datetime.now()

# Создаем главное окно приложения

root = Tk()
root.geometry('1024x512')
root.title('Международный колледж бизнеса и дизайна')
root.configure(bg='#fe6075')

# Загружаем изображения
logotypeOfColledge = PhotoImage(file='homeworkThree/logo.png')
logotypeOfColledge1 = PhotoImage(file='homeworkThree/вапвап.png')

# Размещаем логотипы
logo = Label(root, image=logotypeOfColledge).pack()
logo1 = Label(root, image=logotypeOfColledge1, bg='#fe6075').place(x=75, y=20)
logo2 = Label(root, image=logotypeOfColledge1, bg='#fe6075').place(x=775, y=20)

# Информация о студенте
studentInfo = [
    'Международный колледж бизнеса и дизайна\n',
    'Информационые системы и програмирование\n',
    '3 курс\n',
    'Аганин\n',
    f'Текущее время и дата: {currentDate}\n',
    'Рекламная фраза'
]
infoStudent = Label(root, text=''.join(studentInfo), bg='#fe6075').pack()
def open_link():
    webbrowser.open('https://biscol.ru')
def play_sound():
    playsound('video5197466209813025316 (audio-extractor.net).mp3')
# Функция для отображения информации о предмете
def showSubject():
    subject_info = {
        listSubjects[0]: (f'{listSubjects[0]}: Преподают основы Python и его базовые инструменты\nПреподаватель Ноздрюхин.Т.Ю'),
        listSubjects[1]: (f'{listSubjects[1]}: Моделирование и анализ програмнмного обеспечения\nПреподаватель Пушкина М.С'),
        listSubjects[2]: (f'{listSubjects[2]}: Правовое обеспечение профессиональной деятельности\nПреподаватель Забрамная Н.Ю'),
        listSubjects[3]: (f'{listSubjects[3]}: Технология разработки программного обеспечения\nПреподаватель Пушкина М.С'),
        listSubjects[4]: (f'{listSubjects[4]}: Интеллектуальные системы и технологии\nПреподаватель Кузин О.В'),
        listSubjects[5]: (f'{listSubjects[5]}: Обучают документированию и сертификации ПО\nПреподаватель Прохоров В.А')
    }
    
    selected_subject = clicked.get()
    if selected_subject in subject_info:
        info = subject_info[selected_subject]
        infoAboutSubject.config(text=info)

# Список предметов
listSubjects = [
    'Python',
    'Моделирование и анализ програмнмного обеспечения',
    'ПОПД',
    'Технология разработки программного обеспечения',
    'Интеллектуальные системы и технологии',
    'Инструментальные средства разработки программного обеспечения'
]

clicked = StringVar()
clicked.set('Выберите предмет')

# Выпадающий список для выбора предмета
drop = OptionMenu(root, clicked, *listSubjects, command=lambda _: showSubject())
drop.pack()

# Метка для отображения информации о предмете
infoAboutSubject = Label(root, text='', bg='#fe6075')
infoAboutSubject.pack()


play_button = tk.Button(root, text="Play Sound", command=play_sound)
play_button.pack(pady=10)

link_button = tk.Button(root, text="Open Link", command=open_link)
link_button.pack(pady=10)

root.mainloop()
