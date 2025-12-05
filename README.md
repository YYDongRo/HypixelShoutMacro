# ***Hypixel Shout Macro (Manual Keybind)***

A simple Python tool that lets you send a predefined **/shout** message in Hypixel Bedwars using **one manual key press**.  
This follows Hypixel’s allowed modification rules: **one physical key press per action**, no automation.

## Features
- Press a key (default: **F6**) to send a custom `/shout` message
- Fully manual, Hypixel-compliant
- Simple and lightweight Python script

## Requirements
Install dependencies using the terminal:

```python
python3 -m pip install -r requirements.txt
```

## Usage
```python
python3 shout.py
```
You will then be able to see:
*Shout macro running... Press F6 to send the message.*

**This implies the system is working!**

## Customization
Simply edit *shout.py*

**Change the message**:
```python
SHOUT_MESSAGE = "/shout GG!"
```
**Change the key binding**:
```python
TRIGGER_KEY = keyboard.Key.f7
```




