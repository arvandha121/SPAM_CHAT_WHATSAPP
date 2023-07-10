import pyautogui
import time

pyautogui.moveTo(3530, 983) # Lokasi kursor kearah chat
pyautogui.click()

# Spam chat 100 pesan.
for i in range(100):
    pyautogui.write("PING!!!") # Message pesan spam
    time.sleep(0.01) # Waktu jeda spam
    pyautogui.press("Enter")