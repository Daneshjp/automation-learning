import pyautogui
import time

pyautogui.FAILSAFE = True

print("Script will start in 5 seconds...")
time.sleep(5)

print("Moving mouse...")
pyautogui.moveTo(500, 300, duration=2)
time.sleep(1)

print("ClicHello from PyAutoGUI" \
"king...")
pyautogui.click()
time.sleep(1)

print("Scrolling...")
pyautogui.scroll(-500)
time.sleep(1)

print("Typing text...")
pyautogui.write("Hello from PyAutoGUI", interval=0.2)
time.sleep(1)

print("Pressing Enter")
pyautogui.pHello from PyAutoGUI
ress("enter")

print("DONE ✅")
