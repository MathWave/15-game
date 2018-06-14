from tkinter import *
from random import randrange
from time import time


numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '0']
begin = 0

root = Tk()
root.title('15-game by MathWave')
root.geometry('430x550')
root.resizable(width=False, height=False)

btn_start = Button(root, text='Начать игру!')
btn_start.place(x=10, y=10)
btn_start.bind("<Button-1>", lambda event: Start())

btn_finish = Button(root, text='Закончить игру!')
btn_finish.place(x=125, y=10)
btn_finish.bind("<Button-1>", lambda event: Stop())

canvas = Canvas(root, bg='black', height=400, width=400)
canvas.place(x=10, y=60)

result = Canvas(root, bg='black', height=50, width=400)
result.place(x=10, y=480)

########################################################################################################################

def PrintNumbers():
    global numbers
    canvas.delete('all')
    canvas.create_line(100, 0, 100, 400, fill='white')
    canvas.create_line(200, 0, 200, 400, fill='white')
    canvas.create_line(300, 0, 300, 400, fill='white')
    canvas.create_line(0, 100, 400, 100, fill='white')
    canvas.create_line(0, 200, 400, 200, fill='white')
    canvas.create_line(0, 300, 400, 300, fill='white')
    arr = [50, 150, 250, 350]
    for i in range(4):
        for j in range(4):
            if numbers[j * 4 + i] != '0':
                canvas.create_text(arr[i], arr[j], text=numbers[j * 4 + i], fill='white', font='Comic 32')


def ZeroPosition():
    global numbers
    for i in range(16):
        if numbers[i] == '0':
            return i


def Up():
    global numbers
    n = ZeroPosition()
    if not (n >= 12 and n <= 15):
        numbers[n] = numbers[n + 4]
        numbers[n + 4] = '0'
    PrintNumbers()


def Down():
    global numbers
    n = ZeroPosition()
    if not (n >= 0 and n <= 3):
        numbers[n] = numbers[n - 4]
        numbers[n - 4] = '0'
    PrintNumbers()


def Left():
    global numbers
    n = ZeroPosition()
    if (n + 1) % 4 != 0:
        numbers[n] = numbers[n + 1]
        numbers[n + 1] = '0'
    PrintNumbers()


def Right():
    global numbers
    n = ZeroPosition()
    if n % 4 != 0:
        numbers[n] = numbers[n - 1]
        numbers[n - 1] = '0'
    PrintNumbers()


def Mix():
    for i in range(100):
        n = randrange(4)
        if n == 0:
            Up()
        elif n == 1:
            Down()
        elif n == 2:
            Left()
        else:
            Right()


def Start():
    global begin
    result.delete('all')
    Mix()
    begin = time()


def Stop():
    global begin
    if numbers == ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '0']:
        result.create_text(200, 25, text=('Пятнашки решены за ' + str(int(time() - begin)) + ' секунд'), fill='white')
    else:
        result.create_text(200, 25, text='Вы не решили пятнашки:(', fill='white')

########################################################################################################################

root.bind('<w>', lambda event: Up())

root.bind('<s>', lambda event: Down())

root.bind('<a>', lambda event: Left())

root.bind('<d>', lambda event: Right())


root.mainloop()
