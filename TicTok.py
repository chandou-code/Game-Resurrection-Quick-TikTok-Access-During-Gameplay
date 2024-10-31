import subprocess
import time

import psutil
import pygetwindow as gw
from pynput import mouse, keyboard
import pyautogui
from pywinauto import Application
import subprocess
import time

current_state = True

import pyautogui


def press_space():
    controller = keyboard.Controller()
    controller.press(keyboard.Key.space)
    controller.release(keyboard.Key.space)


def press_right_alt():
    controller = keyboard.Controller()
    controller.press(keyboard.Key.alt_r)  # 按下右 Alt 键
    controller.release(keyboard.Key.alt_r)  # 释放右 Alt 键


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


def start(file_path, window, process_name, window_title):
    # process_name = 'douyin.exe'
    process = subprocess.Popen(file_path)
    time.sleep(1)
    press_right_alt()  # 发送数字键 '3'
    gw.getWindowsWithTitle(window_title)[0].activate()  # 激活窗口
    time.sleep(0.1)  # 确保窗口有时间获得焦点
    press_space()  # 发送空格键


def mini(file_path, window, process_name, window_title):
    window.minimize()


def toggle_window():
    global current_state
    file_path = r"E:\douyin\4.8.1\douyin.exe"
    import pygetwindow as gw

    all_windows = gw.getAllTitles()
    found_window = False
    window_title=''
    process_name=''
    for win in all_windows:
        if win == 'douyin':
            window_title = "douyin"
            process_name = 'douyin.exe'
            found_window = True  # 找到窗口
            break  # 找到后直接退出循环
        elif win == '抖音':
            window_title = "抖音"
            process_name = '抖音.exe'
            found_window = True  # 找到窗口
            break  # 找到后直接退出循环
            # 如果没有找到窗口，执行最后一条语句
    if not found_window:
        print('先运行抖音的小窗模式打开置顶并且在后台最小化暂停')
        return  # 或者其他你想执行的代码

    windows = gw.getWindowsWithTitle(window_title)
    print(windows)
    # start_(file_path=file_path,window_title=window_title)
    if current_state:
        start(file_path=file_path, window=windows[0], process_name=process_name, window_title=window_title)
        print('现在是打开')
    else:
        start(file_path=file_path, window=windows[0], process_name=process_name, window_title=window_title)
        mini(file_path=file_path, window=windows[0], process_name=process_name, window_title=window_title)
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
