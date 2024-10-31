import subprocess
import time

import psutil
import pygetwindow as gw
from pynput import mouse, keyboard
import pyautogui
from pywinauto import Application
import subprocess
import time
import sound

current_state = True


import pyautogui

def press_space():
    controller = keyboard.Controller()
    controller.press(keyboard.Key.space)
    controller.release(keyboard.Key.space)


def get_process_count(process_name):
    count = 0
    pids = []
    for process in psutil.process_iter(['name', 'pid']):
        try:
            if process.info['name'] == process_name:
                count += 1
                pids.append(process.info['pid'])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return count, pids
def start(file_path, window, process_name,window_title):
    # process_name = 'douyin.exe'
    process = subprocess.Popen(file_path)
    time.sleep(1)
    windows = gw.getWindowsWithTitle(window_title)
    press_space()
    windows[0].activate()  # 激活窗口
    time.sleep(0.1)  # 确保窗口有时间获得焦点
    press_space()  # 发送空格键

def mini(file_path, window, process_name,window_title):

    window.minimize()


def toggle_window():
    global current_state
    file_path = r"E:\douyin\4.8.1\douyin.exe"
    window_title = "douyin"
    window_title = "抖音"
    process_name = 'douyin.exe'
    process_name = '抖音.exe'

    windows = gw.getWindowsWithTitle(window_title)
    print(windows)
    # start_(file_path=file_path,window_title=window_title)
    if current_state:
        start(file_path=file_path, window=windows[0], process_name=process_name,window_title=window_title)
        print('现在是打开')
    else:
        start(file_path=file_path, window=windows[0], process_name=process_name, window_title=window_title)
        mini(file_path=file_path, window=windows[0], process_name=process_name,window_title=window_title)
        print('现在是关闭')
    current_state = not current_state


def on_click(x, y, button, pressed):
    if button == mouse.Button.x2 and pressed:  # 检查是否按下侧键 4
        toggle_window()


if __name__ == '__main__':

    with mouse.Listener(on_click=on_click) as listener:
        print("按下鼠标侧键 4 以切换窗口状态（恢复/最小化）...")
        listener.join()  # 持续监听.
    # file_path = r"E:\douyin\4.8.1\douyin.exe"
    # window_title = "douyin"
    # p = start(file_path)
    # print(p)
    # time.sleep(1)

    #
    # # 启动程序
    # process = subprocess.Popen(file_path)
