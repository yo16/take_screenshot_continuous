import time

from take_screenshot import take_screenshot


def take_screenshots_continuous(
    window_title: str,
    save_to_dir: str,
    sleep_time_s: int = 5,
    max_count: int = 1000
):
    for _ in range(max_count):
        take_screenshot(
            window_title,
            save_to_dir
        )

        time.sleep(sleep_time_s)


if __name__=='__main__':
    take_screenshots_continuous(
        "Minecraft 1.20.6 - シングルプレイ",
        "./data/minecraft",
        sleep_time_s = 5,
        max_count = 10
    )
