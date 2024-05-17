import pygetwindow as gw

#from take_screenshot_one_pyautogui import take_screenshot_one_pyautogui
from take_screenshot_one_mss import take_screenshot_one_mss


def take_screenshots(
    window_title: str,
    save_to_dir: str
):
    # ウィンドウを取得
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        print("No matching window found.")
        return 
    
    window = windows[0]
    left, top, width, height = window.left, window.top, window.width, window.height
    #take_screenshot_one_pyautogui(
    take_screenshot_one_mss(
        left, top, width, height,
        save_to_dir
    )


if __name__=="__main__":
    take_screenshots(
        "Minecraft 1.20.6 - シングルプレイ",
        "./data/minecraft"
    )
