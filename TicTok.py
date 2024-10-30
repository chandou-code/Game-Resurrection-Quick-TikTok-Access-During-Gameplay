import subprocess
import time
import pygetwindow as gw
from pynput import mouse, keyboard
import pyautogui
current_state = True


def  press_space():
    print(111)
    controller = keyboard.Controller()
    controller.press(keyboard.Key.space)
    controller.release(keyboard.Key.space)


def click_window(window):
    # 获取窗口中心坐标
    window_center_x = window.left + (window.width // 2)
    window_center_y = window.top + (window.height // 2)

    # 移动鼠标到窗口中心并点击
    pyautogui.moveTo(window_center_x, window_center_y)
    pyautogui.click()


def start(file_path):
    process = subprocess.Popen(file_path)


    window_title = "抖音"
    windows = gw.getWindowsWithTitle(window_title)

    if windows:
        window = windows[0]  # 获取第一个窗口
        # window.activate()  # 激活窗口


        # click_window(window)  # 模拟点击窗口
    # else:
    #     print("未找到窗口")

        # time.sleep(1)  # 确保窗口获得焦点







def start_(file_path, window_title):
    start(file_path)
    mini_(window_title, file_path)
    start(file_path)

def mini(window_title):
    # 获取当前窗口列表
    time.sleep(0.1)
    # print('end')
    windows = gw.getWindowsWithTitle(window_title)
    print("当前窗口:", windows)
    # 如果找到了窗口，则最小化
    if windows:
        window = windows[0]  # 假设找到的第一个窗口是我们要操作的窗口
        # window.activate()  # 激活窗口
        time.sleep(0.5)
        press_space()  # 发送空格键


        window.minimize()  # 最小化窗口
        print("程序窗口已最小化")
    else:
        print("未找到窗口")


def mini_(window_title, file_path):
    # mini(window_title)
    # start(file_path)
    mini(window_title)


def toggle_window():
    global current_state
    file_path = r"E:\douyin\4.8.1\douyin.exe"
    window_title = "抖音"
    if current_state:
        start_(file_path, window_title)

        # mini_(window_title, file_path)
        # start_(file_path, wind  ow_title)
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
