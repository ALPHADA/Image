from tkinter import *
import random

list = ["가위", "바위", "보"]

def choice(x):
    # 리스트중 랜덤하게 하나 선택
    y = ______________
    change1(x) # change1 함수를 통해 사용자가 선택한 것으로 사진을 바꿔 줌
    change2(y) # change2 함수를 통해 랜덤으로 돌린 숫자로 사진을 바꿔 줌
    game(x,y) # 결과값을 보여주는 함수

def change1(x): # 사용자 사진 교체
    photo1 = PhotoImage(file=__________)
    label1.configure(image=photo1)
    label1.image = photo1

def change2(x): # 컴퓨터 사진 교체
    photo2 = PhotoImage(file=__________)
    label3.configure(image=photo2)
    label3.image = photo2

def game(x,y):
    # 사용자가 가위를 냈을 때
    pass
    # 사용자가 바위를 냈을 때
   
    # 사용자가 보를 냈을 때
    

def win(): # 사용자가 가위바위보를 이겼을 경우
    label2.configure(text=">>>>>")
    label4.configure(text="사용자 승!")
def lose(): # 사용자가 졌을 경우
    label2.configure(text="<<<<<")
    label4.configure(text=________)
def draw(): # 비겼을 경우
    label2.configure(text="=====")
    label4.configure(text="________)

win = Tk()
win.title("가위바위보 게임")
font1 = ("굴림체",30,"bold") # 폰트 설정
font2 = ("굴림체",20,"bold") # 폰트 설정

# 딕셔너리를 이용해 파일 경로를 저장
photo = {list[0]:"가위.png", list[1]:_______, _______:________}

# 파일 경로를 설정하여 사진을 불러옴
photo1 = PhotoImage(file=photo[list[2]])
photo2 = PhotoImage(file=photo[_______])

label1 = Label(win, image=photo1)
label2 = Label(win, text = "=====",font=font1)
label3 = Label(win, image=photo2)
label1.grid(row=0, column=0)
label2.grid(row=0, column=1, padx=50)
label3.grid(row=0, column=2)

label4 = Label(win, text = "무승부!",font=font2,fg="green")
label4.grid(row=1, column=1)

button1 = Button(win, text=list[0], command=lambda: choice(list[0]))
button2 = Button(win, text=_______, command=lambda: choice(_______))
button3 = Button(win, text=_______, command=lambda: choice(_______))
button1.grid(row=2, column=0, ipadx=50)
button2.grid(row=2, column=1, ipadx=50)
button3.grid(row=2, column=2, ipadx=50)

win.mainloop()
