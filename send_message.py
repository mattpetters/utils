import os
import sys

def send_imessage(script_path):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
    # Construct full path to the AppleScript file
    full_script_path = os.path.join(script_dir, script_path)
    
    os.system(f"osascript {full_script_path}")

# Replace with the name of your AppleScript file
script_path = "send_imessage.scpt"
send_imessage(script_path)

