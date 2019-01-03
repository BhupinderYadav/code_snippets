'''
 Program to move application logs from list of servers to one shared location. 
 This script can be used to deploy dll or other files on multiple servers in one go without much manual efforts.
'''

import os
import shutil
import csv

server_list = [] # a blank list to hold server name

# importing server name from a excel file and adding it to the list
with open("C:/Users/Alfa/Desktop/server_details.csv", 'r') as server_details: 
    csv_reader = csv.reader(server_details)
    for row in csv_reader:
        server_list.append(row[0])

# fetching logs from all the server and placing it to one shared location

for x in range(len(server_list)):
    server_name = server_list[x]
    file_name = "G:/Alfa/SDIS_20_07_18/Log_07_20_2018_" + str(server_name) + ".txt"
    source_path = '//' + server_name + "/E$/ApplicationLogs/03_Adapter/Log_07_20_2018.txt"
    destination_path = "G:/Alfa/_20_07_18/"
    shutil.copy(source_path, destination_path)
    os.rename("G:/Alfa/SDIS_20_07_18/Log_07_20_2018.txt", file_name)
