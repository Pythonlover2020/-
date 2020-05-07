from MyQR import myqr
from tkinter import Tk, Button, Label, Entry, StringVar, END

'''
本软件由个人研发，如有雷同纯属巧合
'''

win = Tk()
win.title('二维码生成器')
win.geometry('+814+340')
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
Label(win, text='文本内容：').grid(row=0, column=0, padx=10, pady=5)
Label(win, text='图片路径：').grid(row=1, column=0, padx=10)
Label(win, text='是否黑白（Y/N）：').grid(row=2,column=0, padx=10)
entry1 = Entry(win, textvariable=var1)
entry1.grid(row=0, column=1, padx=10, pady=5)
entry2 = Entry(win, textvariable=var2)
entry2.grid(row=1, column=1, padx=10)
entry3 = Entry(win, textvariable=var3)
entry3.grid(row=2, column=1, padx=10)


def get():
    _in_pic = var2.get()
    _in = var3.get()
    if _in_pic == '默认':
        myqr.run(words=var1.get())
    else:
        colorized = _in == 'N'
        myqr.run(words=var1.get(),picture=_in_pic,colorized=colorized)


def dele():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)


Button(win, text='生成', command=get).grid(row=5, column=0, padx=10, pady=5)
Button(win, text='清空', command=dele).grid(row=5, column=1, padx=10, pady=5)

win.mainloop()