
import os
import csv
import psutil

# def find_procs_by_name(name):
#     "Return a list of processes matching 'name'."
#     ls = []
#     for p in psutil.process_iter(['pid', 'name', 'exe', 'cpu_percent', 'memory_percent']):
#         if p.info['name'] == name:
#             ls.append(p.info)
#     return ls

# processes = []

# find_procs_by_name("pid")

# Get a list of all the running processes
processes = []
for proc in psutil.process_iter(['pid', 'name', 'exe', 'cpu_percent', 'memory_info']): # cpu usage and memory usage
    processes.append([proc.info['pid'], proc.info['name'], proc.info['exe'],  
                      proc.info['cpu_percent'], proc.info['memory_info'].rss]) # p.info = dictionary containing process information to the end of the list

# Write the process information to a CSV file
with open('running_processes.csv', mode='w', newline='') as file: # value can be read or write depending on whether the mode is ‘r’ or ‘w’; If csvfile is a file object, it should be opened with newline=''
    writer = csv.writer(file)
    writer.writerow(['Process ID', 'Name', 'Executable Path', 'CPU Usage', 'Memory Usage'])
    for process in processes:
        writer.writerow(process)
print("CSV file has been created successfully.")

# mock_processes = [
#     {'pid': 1, 'name': 'process1', 'exe': '/path/to/process1', 'cpu_percent': 10, 'memory_info': psutil.Process(1).memory_info()},
#     {'pid': 2, 'name': 'process2', 'exe': '/path/to/process2', 'cpu_percent': 20, 'memory_info': psutil.Process(2).memory_info()},
#     # Add more mock process data as needed
# ]

processes = []
