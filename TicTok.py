import pygetwindow as gw
import pynput.mouse as mouse
import time
import time
import pygetwindow as gw
from pynput import mouse, keyboard
current_state = False  # False 表示窗口最小化，True 表示窗口恢复
def press_space():
    controller = keyboard.Controller()
    controller.press(keyboard.Key.space)
    controller.release(keyboard.Key.space)

def restore_window(window_title, target_hWnd):
    windows = gw.getWindowsWithTitle(window_title)
    for window in windows:
        if window._hWnd == target_hWnd:
            if window.isMinimized:
                window.restore()
                time.sleep(0.1)  # 确保窗口恢复后再进行激活
            window.activate()
            press_space()
            print(f"窗口 '{window_title}' (hWnd={target_hWnd}) 已被激活。")
            return
    print(f"没有找到标题为 '{window_title}' 且句柄为 '{target_hWnd}' 的窗口。")

def minimize_window(window_title, target_hWnd):
    windows = gw.getWindowsWithTitle(window_title)
    for window in windows:
        if window._hWnd == target_hWnd:
            window.minimize()
            print(f"窗口 '{window_title}' (hWnd={target_hWnd}) 已被最小化。")

            return

    print(f"没有找到标题为 '{window_title}' 且句柄为 '{target_hWnd}' 的窗口。")

def get_second_max_hWnd(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if len(windows) < 2:  # 如果窗口数量少于2，返回None
        return None
    hWnds = sorted(window._hWnd for window in windows)  # 按照hWnd排序
    return hWnds[-2]  # 返回第二大的hWnd


def toggle_window():
    global current_state
    window_title = "抖音"
    target_hWnd = get_second_max_hWnd(window_title)  # 获取最大 hWnd
    # target_hWnd = 265778  # 获取最大 hWnd

    if target_hWnd is None:
        print(f"没有找到标题为 '{window_title}' 的窗口。")
        return

    if current_state:
        minimize_window(window_title, target_hWnd)
        restore_window(window_title, target_hWnd)
        minimize_window(window_title, target_hWnd)
    else:
        restore_window(window_title, target_hWnd)


    current_state = not current_state  # 切换状态

# 监听鼠标侧键 4
def on_click(x, y, button, pressed):
    if button == mouse.Button.x2 and pressed:  # 检查是否按下侧键 4
        toggle_window()

# 开始监听鼠标事件
with mouse.Listener(on_click=on_click) as listener:
    print("按下鼠标侧键 4 以切换窗口状态（恢复/最小化）...")
    listener.join()  # 持续监听
