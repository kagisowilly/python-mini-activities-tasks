import os
import shutil
import datetime 
import schedule
import time

source_dir = "C:\Users\Admin\Pictures\projects\source"
destination_dir = "C:\Users\Admin\Pictures\projects\destination"

def copy_folder_to_directory(a_source, a_dest):
    l_today = datetime.date.today()
    l_destination_dir = os.path.join(a_dest, str(l_today))

    try:
        shutil.copytree(a_source, l_destination_dir)
        print("Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"FOlder already exists in: {a_dest}")

schedule.every().day.at("06:28").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep()