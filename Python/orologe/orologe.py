# # import tkinter as tk
# # import time

# # root = tk.Tk()
# # root.geometry("350x250")
# # root.title("Non é ora!")
# # root.grid


# # sveglia = ''
# # butt_on = tk.Button(text="Sveglia", command=sveglia)
# # butt_on.grid(row=3, column=3)
# # # orario = tk.StringVar()
# # # finestra = tk.Label(root, textvariable=orario, font=("Helvetica", 48))
# # # finestra.pack()

# # # def upd_time():
# # #     time_now = time.shiftime("%H:%M:%S")
# # #     orario.set(time_now)
# # #     root.after(1000, upd_time)  # Richiama la funzione ogni 1000 millisecondi (1 secondo)
# # # upd_time()

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import time
import pygame

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def display_time(hour, minute, second):
    time_var.set(f"{hour:02d}:{minute:02d}:{second:02d}")

def on_close():
    pygame.mixer.music.stop()
    root.destroy()

def set_alarm():
    try:
        alarm_hour = int(hour_var.get())
        alarm_minute = int(minute_var.get())
    except ValueError:
        messagebox.showerror("Errore", "Inserisci ore e minuti validi.")
        return

    if not (0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59):
        messagebox.showerror("Errore", "Inserisci ore e minuti validi.")
        return

    alarm_day = day_var.get()
    alarm_time = (alarm_day, alarm_hour, alarm_minute, 0)  # Aggiungi zero secondi per semplificare il confronto
    alarms.append(alarm_time)
    messagebox.showinfo("Sveglia impostata", f"Sveglia impostata per {alarm_day} alle {alarm_hour:02d}:{alarm_minute:02d}")

def check_alarms():
    current_time = time.localtime()
    for alarm in alarms:
        if (alarm[0] == current_time.tm_wday or alarm[0] == 'Everyday') and \
           alarm[1] == current_time.tm_hour and alarm[2] == current_time.tm_min and alarm[3] == current_time.tm_sec:
            messagebox.showinfo("Sveglia", "È ora di svegliarsi!")

root = tk.Tk()
root.title("Sveglia")
root.geometry("300x300")  # Sostituisci con le dimensioni desiderate
root.resizable(width=False, height=False)

background_image_pil = Image.open("C:/Users/Elfo98/OneDrive/Documenti/GitHub/Python/python 2SEMAIN/orologe/img/background_cielo.jpg")
background_image = ImageTk.PhotoImage(background_image_pil)
background_label = tk.Label(root, image=background_image)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

time_var = tk.StringVar()
time_label = tk.Label(root, textvariable=time_var, font=("Helvetica", 40))
time_label.place(relx=0.5, rely=0.2,anchor="center")


audio_file_path = "C:/Users/Elfo98/OneDrive/Documenti/GitHub/Python/python 2SEMAIN/orologe/Music/relaxing-145038.mp3"

# Avvia la musica quando il programma si avvia
play_music(audio_file_path)

# Widget di input per l'ora
hour_var = tk.StringVar()
hour_label = tk.Label(root, text="Ora:")
hour_label.place(relx=0.12, rely=0.4)
hour_entry = tk.Entry(root, textvariable=hour_var, width=8)
hour_entry.place(relx=0.251, rely=0.4)

# Widget di input per i minuti
minute_var = tk.StringVar()
minute_label = tk.Label(root, text="Minuti:")
minute_label.place(relx=0.548, rely=0.4)
minute_entry = tk.Entry(root, textvariable=minute_var, width=8)
minute_entry.place(relx=0.718, rely=0.4)

# Casella di selezione per il giorno della settimana
days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Everyday']
day_var = tk.StringVar()
day_label = tk.Label(root, text="Giorno:")
day_label.place(relx=0.17, rely=0.5)
day_combobox = ttk.Combobox(root, textvariable=day_var, values=days_of_week)
day_combobox.place(relx=0.37, rely=0.5)

# Bottone per impostare la sveglia
set_alarm_button = tk.Button(root, text="Imposta sveglia", command=set_alarm)
set_alarm_button.place(relx=0.35, rely=0.7)

alarms = []

close_button = tk.Button(root, text="Chiudi", command=on_close)
close_button.place(relx=0.5, rely=0.9, anchor="center")

# Funzione di aggiornamento dell'ora
def update_time():
    current_time = time.localtime()
    display_time(current_time.tm_hour, current_time.tm_min, current_time.tm_sec)
    check_alarms()
    root.after(1000, update_time)

update_time()

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()