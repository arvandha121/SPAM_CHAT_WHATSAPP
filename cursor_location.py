# Jalankan dan arahkan kursor kearah chat

import pyautogui

while True:
    x, y = pyautogui.position()
    print(f"X={x}, Y={y}")