import datetime
import math
import os
import re
import time
from pathlib import Path

"""
This module searches through the file of a specific path for serial numbers
and returns all the ones found in tabular form
"""

file_serial_dict = dict()


def search_folders():
    #Search each subfolder and file within for serial numbers
    #Add both file names and serial numbers to appropriate list which is returned

    path = Path("C:\\Users\\Niky\\Desktop\\Python\\Day9\\ProjectDay9")
    pattern = r'N\w{3}-\d{5}'
    for folder, subfolders, files in os.walk(path):
        for file in files:
            filepath = Path(folder) / file
            file_content = filepath.read_text()

            # Any matches add the file name to the dictionary and the found
            matching_serial = re.findall(pattern, file_content)
            if matching_serial:
                file_serial_dict[file] = matching_serial


    return file_serial_dict

def display_results(file_serial_dict):
    #Accept the list from the search function and tabulate the results correctly

    serial_list = []

    for file, serial_no in file_serial_dict.items():
        if file == "Instructions.txt":
            continue
        else:
            print(f"{file}\t\t\t\t{serial_no}")
            serial_list.append(serial_no)

    return serial_list

def main():

    today = datetime.datetime.now()
    day = f"{today.day}/{today.month}/{today.year} {today.hour}:{today.minute}:{today.second}"


    print("---------------------------------------------------------")
    print(f"Search date: \t {day}\n")
    print("FILE\t\t\t\t\tSERIAL NO.\n____\t\t\t\t\t__________\n")

    start = time.time()
    file_serial_dict = search_folders()
    serial_list = display_results(file_serial_dict)
    stop = time.time()

    print(f"\nNumbers found: {len(serial_list)}")
    print(f"Search duration: {math.ceil(stop-start)} s")

    print("---------------------------------------------------------")

if __name__ == '__main__':
    main()






