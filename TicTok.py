import subprocess
import time

import psutil
import pygetwindow as gw
from pynput import mouse, keyboard
import pyautogui

current_state = True


def press_space():
    controller = keyboard.Controller()
    controller.press(keyboard.Key.space)
    controller.release(keyboard.Key.space)

def start(file_path):
    process = subprocess.Popen(file_path)
    return process

def mini(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    windows[0].minimize()  # 最小化窗口


def toggle_window():
    global current_state
    file_path = r"E:\douyin\4.8.1\douyin.exe"
    window_title = "douyin"
    # start_(file_path=file_path,window_title=window_title)
    if current_state:
        start(file_path=file_path)
        print('现在是打开')
    else:
        mini(window_title=window_title)
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
