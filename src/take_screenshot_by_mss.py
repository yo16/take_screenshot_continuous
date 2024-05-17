import mss
import mss.tools
import time
from pathlib import Path

def take_screenshot_by_mss(
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

    with mss.mss() as sct:
        # キャプチャ領域の定義
        monitor = {"top": y, "left": x, "width": width, "height": height}
        screenshot = sct.grab(monitor)
        
        # 現在の日時を取得し、ファイル名を生成
        current_time = time.localtime()
        time_str: str = time.strftime("%Y%m%d_%H%M%S", current_time)
        file_path: Path = dir_path / f"{time_str}.png"
        
        # 画像を保存
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=str(file_path))
        print(f"Screenshot taken and saved as '{file_path}'")
