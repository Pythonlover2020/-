from wordcloud import WordCloud
from tkinter import Tk,Button,Label,Entry,StringVar,END
from jieba import cut
from time import localtime
from PIL import Image
from numpy import array

'''
本软件由个人研发，如有雷同纯属巧合'''

#文本路径用r'%s' % （用户输入）来获取
font = r'C:\Windows\Fonts\simkai.ttf'#字体路径（配置中文词云）
def cy(in_文本路径,in_图片路径,in_输出路径,in_背景颜色,in_大小):
    if in_图片路径 == '默认':
        text = ' '.join(cut(str(open(in_文本路径,'r',encoding='gbk').read())))
        wordcloud = WordCloud(background_color=in_背景颜色,font_path=font,width=int(str(in_大小).split('x')[0]),height=int(str(in_大小).split('x')[1]))
        wordcloud.generate(text)
        wordcloud.to_file(in_输出路径)
    else:
        text = ' '.join(cut(str(open(in_文本路径,'r',encoding='gbk').read())))
        photo = Image.open(in_图片路径)
        photoarray = array(photo)
        wordcloud = WordCloud(background_color=in_背景颜色,font_path=font,mask=photoarray)
        wordcloud.generate_from_text(text)
        wordcloud.to_file(in_输出路径)

win = Tk()
win.title('词云生成器')
win.geometry('+814+340')
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
Label(win,text='文本路径：').grid(row=0,column=0,padx=10,pady=5)
Label(win,text='图片路径：').grid(row=1,column=0,padx=10)
Label(win,text='输出路径：').grid(row=2,column=0,padx=10)
Label(win,text='背景颜色：').grid(row=3,column=0,padx=10)
Label(win,text='图片大小：').grid(row=4,column=0,padx=10)
entry1 = Entry(win,textvariable=var1)
entry1.grid(row=0,column=1,padx=10,pady=5)
entry2 = Entry(win,textvariable=var2)
entry2.grid(row=1,column=1,padx=10)
entry3 = Entry(win,textvariable=var3)
entry3.grid(row=2,column=1,padx=10)
entry4 = Entry(win,textvariable=var4)
entry4.grid(row=3,column=1,padx=10)
entry5 = Entry(win,textvariable=var5)
entry5.grid(row=4,column=1,padx=10)

def get():
    out_文本路径 = r'%s' % str(var1.get())
    a = str(var2.get())
    if a == '默认':
        out_图片路径 = a
    
    else:
        out_图片路径 = r'%s' % a
    b = localtime()
    name = '词云'
    for each in b:
        name += str(each)
    name += '.png'
    out_输出路径 = r'%s\%s' % (str(var3.get()),name)
    out_背景颜色 = str(var4.get())
    out_图片大小 = str(var5.get())
    cy(in_文本路径=out_文本路径,in_图片路径=out_图片路径,in_大小=out_图片大小,in_背景颜色=out_背景颜色,in_输出路径=out_输出路径)

def dele():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    entry5.delete(0,END)

Button(win,text='生成',command=get).grid(row=5,column=0,padx=10,pady=5)
Button(win,text='清空',command=dele).grid(row=5,column=1,padx=10,pady=5)
    
win.mainloop()