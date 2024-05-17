import pyautogui
import time
from pathlib import Path

def take_screenshot_by_pyautogui(
    x: int,
    y: int,
    width: int,
    height: int,
    save_to: str
):
    print(f"x:{x}, y:{y}, w:{width}, h:{height}")
    
    # フォルダを作る
    dir_path = Path(save_to)
    dir_path.mkdir(parents=True, exist_ok=True)

    # スクリーンショットを取る
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    # ファイルパス
    current_time = time.localtime()
    time_str: str = time.strftime("%Y%m%d_%H%M%S", current_time)
    file_path: Path = dir_path / f"{time_str}.png"
    screenshot.save(file_path)
