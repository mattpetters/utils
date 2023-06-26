import os

def send_imessage(script_path):
    os.system(f"osascript {script_path}")

# Replace with the path to your AppleScript file
script_path = "/path/to/your/script.scpt"
send_imessage(script_path)

