import subprocess
import time
import pygetwindow as gw
from pynput import mouse, keyboard
current_state = True

def press_space():
    print(111)
    controller = keyboard.Controller()
    controller.press(keyboard.Key.space)
    controller.release(keyboard.Key.space)


def start(file_path):
    # 启动程序
    print('start')
    process = subprocess.Popen(file_path)
    time.sleep(0.3)  # 等待程序启动

    press_space()


def mini(window_title):
    # 获取当前窗口列表
    time.sleep(0.1)
    print('end')
    windows = gw.getWindowsWithTitle(window_title)
    print("当前窗口:", windows)
    # 如果找到了窗口，则最小化
    if windows:
        window = windows[0]  # 假设找到的第一个窗口是我们要操作的窗口
        window.minimize()  # 最小化窗口
        print("程序窗口已最小化")
    else:
        print("未找到窗口")


def mini_(window_title, file_path):
    mini(window_title)
    start(file_path)
    mini(window_title)


def toggle_window():
    global current_state
    file_path = r"E:\douyin\4.8.1\douyin.exe"
    window_title = "抖音"
    if current_state:
        start(file_path)
    else:

        mini_(window_title, file_path)

    current_state = not current_state

def on_click(x, y, button, pressed):
    if button == mouse.Button.x2 and pressed:  # 检查是否按下侧键 4
        toggle_window()


if __name__ == '__main__':


    with mouse.Listener(on_click=on_click) as listener:
        print("按下鼠标侧键 4 以切换窗口状态（恢复/最小化）...")
        listener.join()  # 持续监听
    # file_path = r"E:\douyin\4.8.1\douyin.exe"
    # window_title = "抖音"
    #
    # # 启动程序
    # process = subprocess.Popen(file_path)

