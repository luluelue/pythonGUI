# coding=utf-8

from os.path import abspath, dirname, join
import sys

sys.path.append(join(abspath(dirname(__file__)), 'venv'))
sys.path.append(join(abspath(dirname(__file__)), 'venv\\Lib\\site-packages'))
import requests
import pandas as pd
import os
import shutil
import tkinter as tk
import tkinter.messagebox #这个是消息框，对话框的关键



# pyinstaller -F xxxx.py
# pyinstaller -F -i label.ico main.py -n 接小球游戏 --noconsole
# pip install pyinstaller -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__11':
    # tkinter.messagebox.showinfo('提示', '人生苦短')
    # tkinter.messagebox.showwarning('警告', '明日有大雨')
    window = tk.Tk()
    # window.withdraw()
    window.title('消息框')
    window.geometry('190x80+300+300')  # 设置窗口大小和位置
    txt = tk.Entry(window, width=20).pack()  # 注意，输入框就是单行文本，它是没有height属性的

    window.mainloop()


    # flag = tkinter.messagebox.askokcancel('提示', '要执行此操作吗')  # 确定/取消，返回值true/false
    # print("弹窗结果：{}".format(flag))

    args = sys.argv
    fileName = "test.txt"
    if len(args) > 1:
        fileName = args[1]
    file = open(fileName, 'w')
    file.write("test txt")
    file.close()
    print("logloglog ------------")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# 登录联系
if __name__ == '__main__':
    window = tk.Tk()
    window.title('Welcome to Mofan Python')
    window.geometry('450x300')

    # welcome image
    canvas = tk.Canvas(window, height=200, width=500)
    image_file = tk.PhotoImage(file='welcome.gif')
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)
    canvas.pack(side='top')

    # user information
    tk.Label(window, text='User name: ').place(x=50, y=150)
    tk.Label(window, text='Password: ').place(x=50, y=190)

    var_usr_name = tk.StringVar()
    var_usr_name.set('example@python.com')
    entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
    entry_usr_name.place(x=160, y=150)
    var_usr_pwd = tk.StringVar()
    entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
    entry_usr_pwd.place(x=160, y=190)


    def usr_login():
        userName = var_usr_name.get()
        print("用户名：{}".format(userName))
        tk.messagebox.showinfo(title='Welcome', message='How are you? ' + userName)



    def usr_sign_up():
        pwd = var_usr_pwd.get()
        print("用户名：{}".format(pwd))
        res = tk.messagebox.askyesno('Welcome',
                               'You have not sign up yet. Sign up today?')
        print("result:{}".format(res))


    # login and sign up button
    btn_login = tk.Button(window, text='Login', command=usr_login)
    btn_login.place(x=170, y=230)
    btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
    btn_sign_up.place(x=270, y=230)

    window.mainloop()