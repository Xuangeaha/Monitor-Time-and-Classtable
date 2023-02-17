import tkinter as tk
import tkinter.messagebox
import time
import sys
import threading

lastClickX = 0
lastClickY = 0

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x , y))

def breakwindow():
    root.destroy()
    sys.exit()
    
root = tk.Tk()
root.title("值日班长、时间与课程表")
root.overrideredirect(True)

root.bind('<Button-1>', SaveLastClickPos)
root.bind('<B1-Motion>', Dragging)

a = time.asctime().split(" ")
print(a)
b = a[3].split(":")
tick_hour = int(b[0])
tick_minute = int(b[1])
se = int(b[2])

is_1 = a[0] == "Mon"
is_2 = a[0] == "Tue"
is_3 = a[0] == "Wed"
is_4 = a[0] == "Thu"
is_5 = a[0] == "Fri"

if is_1:
    monitor = "周子辰"
    class_list = ["物理","语文","道法","化学","英语","美术","体育","数学",""]
elif is_2:
    monitor = "江华"
    class_list = ["英语","化学","语文","数学","体育","英语","语文","物理","自修"]
elif is_3:
    monitor = "陈邵祺"
    class_list = ["生命科学","英语","道法","物理","语文","体育","化学","语文","数学"]
elif is_4:
    monitor = "尤景暄"
    class_list = ["道法","化学","物理","体育","语文","数学","数学","英语","英语"]
elif is_5:
    monitor = "张扬"
    class_list = ["英语","化学","物理","语文","体育","数学","数学","班会","自修"]
else:
    monitor = "朱欣诚"
    class_list = ["美术","沙画","音乐","法语","生命科学","体育","体育","88","99"]

class_colour = ["","Black","Black","Black","Black","Black","Black","Black","Black","Black"]

entry = tk.Label(root,font=("华文中宋",38),text="今日值日班长："+monitor)
entry.grid(row=1,column=0,columnspan=9)

def refresh_colour():
    global a,b,tick_hour,tick_minute,se
    while True:
        a = time.asctime().split(" ")
        b = a[3].split(":")
        tick_hour = int(b[0])
        tick_minute = int(b[1])
        tick_second = int(b[2])
        print(a,b,tick_hour,tick_minute,tick_second)
        
        if tick_hour == 6 or tick_hour == 7 and 0 <= tick_minute <= 58:
            pass
        elif tick_hour == 7 and 58 <= tick_minute == 59 or tick_hour == 8 and 0 <= tick_minute <= 40: #1
            class_colour[1] = "#00FF00"
        elif tick_hour == 8 and 41 <= tick_minute <= 57:
            class_colour[1] = "Red"
        elif tick_hour == 8 and 58 <= tick_minute <= 59 or tick_hour == 9 and 0 <= tick_minute <= 40: #2
            class_colour[1] = "Red"
            class_colour[2] = "#00FF00"
        elif tick_hour == 9 and 41 <= tick_minute <= 47:
            class_colour[1] = "Red"
            class_colour[2] = "Red"
        elif tick_hour == 9 and 48 <= tick_minute <= 59 or tick_hour == 10 and 0 <= tick_minute <= 30: #3
            class_colour[1] = "Red"
            class_colour[2] = "Red"
            class_colour[3] = "#00FF00"
        elif tick_hour == 10 and 31 <= tick_minute <= 32:
            class_colour[1] = "Red"
            class_colour[2] = "Red"
            class_colour[3] = "Red"
        elif tick_hour == 10 and 33 <= tick_minute <= 59 or tick_hour == 11 and 0 <= tick_minute <= 20: #4
            class_colour[1] = "Red"
            class_colour[2] = "Red"
            class_colour[3] = "Red"
            class_colour[4] = "#00FF00"
        elif tick_hour == 11 and 21 <= tick_minute <= 37:
            class_colour[1] = "Red"
            class_colour[2] = "Red"
            class_colour[3] = "Red"
            class_colour[4] = "Red"
        elif tick_hour == 11 and 28 <= tick_minute <= 59 or tick_hour == 12 and 0 <= tick_minute <= 10: #5
            class_colour[1] = "Red"
            class_colour[2] = "Red"
            class_colour[3] = "Red"
            class_colour[4] = "Red"
            class_colour[5] = "#00FF00"
        elif tick_hour == 12 and 11 <= tick_minute <= 57:
            class_colour[1] = "Red"
            class_colour[2] = "Red"
            class_colour[3] = "Red"
            class_colour[4] = "Red"
            class_colour[5] = "Red"
        elif tick_hour == 12 and 58<= tick_minute <= 59 or tick_hour == 13 and 0 <= tick_minute <= 40: #6
            class_colour[1] = "Red"
            class_colour[2] = "Red"
            class_colour[3] = "Red"
            class_colour[4] = "Red"
            class_colour[5] = "Red"
            class_colour[6] = "#00FF00"
        elif tick_hour == 13 and 41 <= tick_minute <= 52:
            class_colour[1] = "Red"
            class_colour[2] = "Red"
            class_colour[3] = "Red"
            class_colour[4] = "Red"
            class_colour[5] = "Red"
            class_colour[6] = "Red"
        elif tick_hour == 13 and 53 <= tick_minute <= 59 or tick_hour == 14 and 0 <= tick_minute <= 35: #7
            class_colour[1] = "Red"
            class_colour[2] = "Red"
            class_colour[3] = "Red"
            class_colour[4] = "Red"
            class_colour[5] = "Red"
            class_colour[6] = "Red"
            class_colour[7] = "#00FF00"
        elif tick_hour == 14 and 36 <= tick_minute <= 59 or tick_hour == 15 and 0 <= tick_minute <= 2:
            class_colour[1] = "Red"
            class_colour[2] = "Red"
            class_colour[3] = "Red"
            class_colour[4] = "Red"
            class_colour[5] = "Red"
            class_colour[6] = "Red"
            class_colour[7] = "Red"
        elif tick_hour == 15 and 3 <= tick_minute <= 45: #8
            class_colour[1] = "Red"
            class_colour[2] = "Red"
            class_colour[3] = "Red"
            class_colour[4] = "Red"
            class_colour[5] = "Red"
            class_colour[6] = "Red"
            class_colour[7] = "Red"
            class_colour[8] = "#00FF00"
        elif tick_hour == 15 and 46 <= tick_minute <= 52:
            class_colour[1] = "Red"
            class_colour[2] = "Red"
            class_colour[3] = "Red"
            class_colour[4] = "Red"
            class_colour[5] = "Red"
            class_colour[6] = "Red"
            class_colour[7] = "Red"
            class_colour[8] = "Red"
        elif tick_hour == 15 and 53 <= tick_minute <= 59 or tick_hour == 16 and 0 <= tick_minute <= 40: #9
            class_colour[1] = "Red"
            class_colour[2] = "Red"
            class_colour[3] = "Red"
            class_colour[4] = "Red"
            class_colour[5] = "Red"
            class_colour[6] = "Red"
            class_colour[7] = "Red"
            class_colour[8] = "Red"
            class_colour[9] = "#00FF00"
        else:
            class_colour[1] = "Red"
            class_colour[2] = "Red"
            class_colour[3] = "Red"
            class_colour[4] = "Red"
            class_colour[5] = "Red"
            class_colour[6] = "Red"
            class_colour[7] = "Red"
            class_colour[8] = "Red"
            class_colour[9] = "Red"

        for x in range(0,9):
            classlabel = tk.Label(root,text=class_list[x],fg=class_colour[x+1],font=("华文中宋",30))
            classlabel.grid(row=3,column=x)

        time.sleep(10)

colour_thread = threading.Thread(target=refresh_colour)
colour_thread.start()

def up():
    entry2.delete(0,"end")
    entry2.insert(0,time.asctime())
    entry2.after(1000,up)

entry2 = tk.Entry(root,width=35,justify="center",font=("",35))
entry2.grid(row=2,column=0,columnspan=9)
entry2.after(1000,up)

for x in range(0,9):
    classlabel = tk.Label(root,text=class_list[x],fg=class_colour[x+1],font=("华文中宋",30))
    classlabel.grid(row=3,column=x)


def new():
    r = tk.Tk()
    r.title("值日班长、时间与课程表 - 自定义显示")

    l = tk.Label(r,text="设置自定义显示内容：",font=("华文中宋",25))
    l.grid(row=1,column=1,columnspan=2)

    e = tk.Entry(r,font=("",25),justify="center")
    e.grid(row=2,column=1,columnspan=2)

    def check():
        entry["text"] = e.get()
        root.update()
        r.destroy()

    def ex():
        r.destroy()
        
    b = tk.Button(r,text="确定",command=check,width=6,font=("华文中宋",15))
    b.grid(row=3,column=1)

    b2 = tk.Button(r,text="取消",command=ex,width=6,font=("华文中宋",15))
    b2.grid(row=3,column=2)
    
    r.mainloop()
    pass


def wnew():
    wr = tk.Tk()
    wr.title("值日班长、时间与课程表 - 临时值日班长")

    wl = tk.Label(wr,text="设置临时值日班长：",font=("华文中宋",25))
    wl.grid(row=1,column=1,columnspan=2)

    we = tk.Entry(wr,font=("",25),justify="center")
    we.grid(row=2,column=1,columnspan=2)

    def wcheck():
        entry["text"] = "今日值日班长：" + we.get()
        root.update()
        wr.destroy()

    def wex():
        wr.destroy()
        
    wb = tk.Button(wr,text="确定",command=wcheck,width=6,font=("华文中宋",15))
    wb.grid(row=3,column=1)

    wb2 = tk.Button(wr,text="取消",command=wex,width=6,font=("华文中宋",15))
    wb2.grid(row=3,column=2)
    
    wr.mainloop()
    pass

def change():
    qr = tk.Tk()
    qr.title("值日班长、时间与课程表 - 临时调课")

    ql = tk.Label(qr,text="设置临时课程调整：",font=("华文中宋",25))
    ql.grid(row=1,column=1,columnspan=2)

    qe = tk.Entry(qr,font=("",25),justify="center")
    qe.grid(row=2,column=1,columnspan=2)

    def qcheck():
        qgget = qe.get().split(" ")
        class_list[int(qgget[0])-1] = str(qgget[1])
        root.update()
        qr.destroy()

    def qex():
        qr.destroy()
        
    qb = tk.Button(qr,text="确定",command=qcheck,width=6,font=("华文中宋",15))
    qb.grid(row=3,column=1)

    qb2 = tk.Button(qr,text="取消",command=qex,width=6,font=("华文中宋",15))
    qb2.grid(row=3,column=2)
    
    qr.mainloop()
    pass

def writer():
    msgbox = tk.messagebox.showinfo("值日班长、时间与课程表 - 关于","值日班长、时间与课程表 v2.1\n\n作者：轩哥啊哈OvO\n\nCopyright © 2022 - 轩哥啊哈OvO")

menubar = tk.Menu(root, bg="red")
root.config(menu=menubar)
exitMenu = tk.Menu(menubar, tearoff=0)
eMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="值日班长、时间与课程表 2.1")
menubar.add_cascade(label="设置",menu=exitMenu)
exitMenu.add_command(label="自定义显示..",command=new)
exitMenu.add_separator()
exitMenu.add_command(label="临时值日班长..",command=wnew)
exitMenu.add_command(label="临时调课..",command=change)
menubar.add_cascade(label="关于",menu=eMenu)
eMenu.add_command(label="关于..",command=writer)
eMenu.add_command(label="退出..", command=breakwindow)

root.mainloop()
