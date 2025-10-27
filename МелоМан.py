# Импорт всех необходимых модулей
from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer        # pip install pygame
import os

# Инициализация главного окна и pygame.mixer

# Инициализация микшера
mixer.init()

# Создание главного GUI для музыкального плеера
root = Tk()
root.geometry('725x220')
root.title('МелоМен')  # Можно заменить на "Музыкальный плеер" или другое русское название
root.resizable(0, 0)

# Функции: Воспроизведение, Стоп, Загрузка и Пауза & Продолжить
def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))

    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()

    status.set("Песня воспроизводится")


def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Песня остановлена")


def load(listbox):
    os.chdir(filedialog.askdirectory(title='Выберите папку'))

    tracks = os.listdir()

    for track in tracks:
        listbox.insert(END, track)


def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Песня на паузе")


def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Песня воспроизводится")

button_bg = "#b02020"
button_fg = "#d44848"
frame_bg = "#9c2c2c"


# Все фреймы
song_frame = LabelFrame(root, text='Текущая песня', font=("Comic Sans MS", 9), bg=frame_bg , width=425, height=80)
song_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='Управление', font=("Comic Sans MS", 9), bg=frame_bg, width=425, height=120)
button_frame.place(y=80)

listbox_frame = LabelFrame(root, text='Плейлист', font=("Comic Sans MS", 9), bg=frame_bg)
listbox_frame.place(x=425, y=0, height=200, width=300)

# Все StringVar переменные
current_song = StringVar(root, value='Не выбрана')

song_status = StringVar(root, value='Не доступно')



# ListBox плейлиста
playlist = Listbox(listbox_frame, font=('Comic Sans MS', 11), selectbackground='snow3')

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=5, pady=5)



# Надписи в SongFrame
Label(song_frame, text='СЕЙЧАС ИГРАЕТ:', bg=frame_bg, font=('Comic Sans MS', 10, 'bold')).place(x=5, y=20)

song_lbl = Label(song_frame, textvariable=current_song, bg=button_fg, font=("Comic Sans MS", 12), width=25)
song_lbl.place(x=130, y=20)


# Кнопки на главном экране
pause_btn = Button(button_frame, text='Пауза', bg=button_fg, font=("Comic Sans MS", 13), width=7,
                    command=lambda: pause_song(song_status))
pause_btn.place(x=15, y=10)

stop_btn = Button(button_frame, text='Стоп', bg=button_fg, font=("Comic Sans MS", 13), width=7,
                  command=lambda: stop_song(song_status))
stop_btn.place(x=105, y=10)

play_btn = Button(button_frame, text='Начать', bg=button_fg, font=("Comic Sans MS", 13), width=10,
                  command=lambda: play_song(current_song, playlist, song_status))
play_btn.place(x=195, y=10)

resume_btn = Button(button_frame, text='Продолжить', bg=button_fg, font=("Comic Sans MS", 13), width=10,
                    command=lambda: resume_song(song_status))
resume_btn.place(x=310, y=10)

load_btn = Button(button_frame, text='Загрузить папку', bg=button_fg, font=("Comic Sans MS", 13), width=35, command=lambda: load(playlist))
load_btn.place(x=40, y=55)

# Надпись внизу, отображающая статус музыки
Label(root, textvariable=song_status, bg=button_fg, font=('Comic Sans MS', 9), justify=LEFT).pack(side=BOTTOM, fill=X)


# Завершение GUI
root.update()
root.mainloop()