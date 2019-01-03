'''
	This program is to find drive space on all the server in a domain
	put one csv file in d: having list of all servers
'''

import os
import shutil
import csv
import psutil

server_list = []

# importing server name from a excel file and adding it to the list

with open("D:\server_details.csv", 'r') as server_details:
    csv_reader = csv.reader(server_details)
    for row in csv_reader:
        server_list.append(row[0])

# output file details 

filename = "D:\drive_data.csv"
file1 = open(filename, "w")
file1.write('server disk_usage' + '\n')

# fetching disk space details from each server and putting it into an csv file

for i in range(len(server_list)):
    server_name = server_list[i]
    x = psutil.disk_usage('//'+ server_name + '/D$')
    #x = psutil.disk_usage('C:')
    v = str(x)
    val = str(server_name) + ' ' + str(v[10:])
    file1.write(val + '\n')
