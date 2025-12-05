from pynput import keyboard
import pyautogui
import time

SHOUT_MESSAGE = "/shout Like squeezing a lemon LOLL!"

# Replace this with the key you want to press
TRIGGER_KEY = keyboard.Key.f6


def send_shout():
    # Type the message
    pyautogui.typewrite(SHOUT_MESSAGE)
    time.sleep(0.05)
    pyautogui.press("enter")


def on_press(key):
    if key == TRIGGER_KEY:
        send_shout()


with keyboard.Listener(on_press=on_press) as listener:
    print("Shout macro running... Press F6 to send the message.")
    listener.join()
