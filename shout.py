from pynput import keyboard
import pyautogui
import time

SHOUT_MESSAGE = "/shout Like squeezing a lemon"

# Replace this with the key you want to press
TRIGGER_KEY = keyboard.Key.f12


def send_shout():
    # Type the message
    pyautogui.typewrite("t")
    time.sleep(0.5)
    pyautogui.typewrite(SHOUT_MESSAGE)
    time.sleep(0.5)
    pyautogui.press("enter")


def on_press(key):
    if key == TRIGGER_KEY:
        send_shout()


with keyboard.Listener(on_press=on_press) as listener:
    print("Shout macro running... Press f12 to send the message.")
    listener.join()

