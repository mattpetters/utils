import os
import sys
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from datetime import datetime

scheduler = BlockingScheduler()

def send_imessage(script_path, phone_number, message):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
    # Construct full path to the AppleScript file
    full_script_path = os.path.join(script_dir, script_path)
    
    os.system(f"osascript {full_script_path}")

def schedule_message(when_to_send, phone_number, message):
    scheduler.add_job(send_imessage, 'date', run_date = when_to_send , args=['send_imessage.scpt', phone_number, message])

scheduler.start()