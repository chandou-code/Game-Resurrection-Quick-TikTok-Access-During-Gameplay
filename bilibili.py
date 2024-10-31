
from pynput import mouse, keyboard


def press_keys():
    controller = keyboard.Controller()
    controller.press(keyboard.Key.shift)
    controller.press(keyboard.Key.ctrl)
    controller.press('c')
    controller.release('c')
    controller.release(keyboard.Key.ctrl)
    controller.release(keyboard.Key.shift)

def on_click(x, y, button, pressed):
    if button == mouse.Button.x2 and pressed:
        press_keys()
if __name__ == '__main__':

    with mouse.Listener(on_click=on_click) as listener:
        print("按下鼠标侧键 4 以切换窗口状态（恢复/最小化）...")
        listener.join()  
