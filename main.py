from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#D0FE1D"
YELLOW = "#f7f5dd"
GREY = "#5A5A5A"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer= None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer')
    check_marks.config(text='')
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break_sec= SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text='L* Break', fg=GREEN, font=(FONT_NAME, 15, 'bold'))
    elif reps%2==0:
        countdown(short_break_sec)
        title_label.config(text='S* Break', fg=GREEN, font=(FONT_NAME, 15, 'bold'))
    else:
        countdown(work_sec)
        title_label.config(text='Work')


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    count_min= math.floor(count/60)
    count_sec=count % 60

    if count_sec < 10:
        count_sec= f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer=window.after(1000, countdown, count - 1)
    else:
        start_time()
        mark=''
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            mark += '✔'
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.config(padx=10, pady=5, bg=GREY)
window.overrideredirect(True)
window.attributes("-topmost", True)
screen_width = window.winfo_screenwidth()
window.geometry(f'156x135+{screen_width-356}+0')

title_label=Label(text='Timer',fg=GREEN, font=(FONT_NAME, 15, 'bold'), highlightbackground= YELLOW, bg=GREY)
title_label.grid(column=1, row=0)

start_button=Button(text="Start",highlightthickness=0, command=start_time, border = 0, background=GREY, fg=GREEN)
start_button.grid(column=2, row=1)

reset_button=Button(text='Reset',highlightthickness=0, command=reset_timer, border=0, background=GREY, fg=GREEN)
reset_button.grid(column=2, row=2)

close_button=Button(text='X', command=window.destroy, highlightthickness=0, border=0, background=GREY, fg=GREEN)
close_button.grid(column=2, row=0)

check_marks=Label(fg=GREEN, highlightbackground= YELLOW, bg=GREY, font=(FONT_NAME, 10, 'bold'))
check_marks.grid(column=1, row=3)

canvas = Canvas(width=100, height=50, bg=GREY, highlightthickness=0)

timer_text= canvas.create_text(50,25, text='00:00', fill='white', font=(FONT_NAME, 15, 'bold'))
canvas.grid(column=1, row=1)


window.mainloop()

