# （参考）classを使ったバージョン
import time
import mouse
from datetime import datetime


class Clicker:

    def __init__(self, sleep_sec: int) -> None:
        self.sleep_sec = sleep_sec

    def start_loop(self):
        while True:
            ts = datetime.now().strftime("%F %T")
            mouse.click('right')
            print(f'[{ts}] clicked.')
            time.sleep(self.sleep_sec)


if __name__ == '__main__':
    Clicker(sleep_sec=10).start_loop()
