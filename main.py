import datetime
import os
import tkinter
import configparser
from chinese_calendar import is_holiday


def refreshTime():
    now = datetime.datetime.now()
    time_now = now.time()
    date_now = now.date()

    if is_holiday(date_now):
        result = '快乐时间！！！'
    elif time_now > off_duty_time:
        result = '快乐时间！！！'
    else:
        time_count_down = datetime.datetime.combine(date_now, off_duty_time) - now
        date_count_down = date_now + datetime.timedelta(days=1)
        while True:
            if is_holiday(date_count_down):
                break
            else:
                date_count_down += datetime.timedelta(days=1)
                time_count_down += datetime.timedelta(days=1)
        result = strfdelta(time_count_down, "{days}天{hours}小时{minutes}分{seconds}秒")
    myLabel.configure(text=result)
    root.after(200, refreshTime)  # 每隔200ms循环调用自身


def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)


def set_window_location(root, width, height, x, y):
    if x == 0 and y == 0:
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    else:
        size = '%dx%d+%d+%d' % (width, height, x, y)
    root.geometry(size)
    root.update()


def myquit(*args):
    root.destroy()


def startMove(event):
    global x, y
    x = event.x
    y = event.y


def stopMove(event):
    global x, y
    x = None
    y = None
    conf.set("location", "x", str(root.winfo_x()))
    conf.set("location", "y", str(root.winfo_y()))
    conf.write(open("cfg.ini", "w"))


def onMotion(event):
    global x, y
    deltax = event.x - x
    deltay = event.y - y
    root.geometry("+%s+%s" % (root.winfo_x() + deltax, root.winfo_y() + deltay))
    root.update()
    # print(event.x, event.y, root.winfo_x(), root.winfo_y(), root.winfo_width(), root.winfo_height())


if __name__ == '__main__':
    # 配置信息读取
    conf = configparser.ConfigParser()
    conf.read("cfg.ini", encoding='utf8')
    MyHour = conf.get("off_duty_time", "hour")
    MyMinute = conf.get("off_duty_time", "minute")
    off_duty_time = datetime.time(int(MyHour), int(MyMinute), 0)
    x = conf.get("location", "x")
    y = conf.get("location", "y")

    # 窗口创建
    root = tkinter.Tk()
    root.title('假期倒计时')
    set_window_location(root, 200, 20, int(x), int(y))
    root.overrideredirect(1)  # 去除窗口边框
    root.wm_attributes("-alpha", 0.5)  # 透明度(0.0~1.0)
    root.wm_attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
    root.wm_attributes("-topmost", True)  # 永远处于顶层
    myLabel = tkinter.Label(root, text='-', font=("Arial Bold", 15))
    myLabel.pack(fill=tkinter.X, side=tkinter.TOP)

    # 事件绑定
    root.bind("<Any-KeyPress>", myquit)
    root.bind("<ButtonPress-1>", startMove)  # 监听左键按下操作响应函数
    root.bind("<ButtonRelease-1>", stopMove)  # 监听左键松开操作响应函数
    root.bind("<B1-Motion>", onMotion)  # 监听鼠标移动操作响应函数
    refreshTime()

    # 启动窗口
    root.mainloop()
