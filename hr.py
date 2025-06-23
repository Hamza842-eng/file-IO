# this is a file handling
# read a file
'''
f = open("demo.txt",'r')
data = f.read()
print(data)

# write a file
f = open("demo.txt",'w')
f.write("am a web developer")

f.close()

# append a file 
f = open("demo.txt",'a')
f.write("and python developer")

f.close()

#overwrite a file
f = open("demo.txt",'r+')
f.write("abc")

f.close()
'''

import os

# Define names
folder_name = "demo_folder"
file_name = "demo_file.txt"
new_file_name = "renamed_file.txt"

# Create directory if it doesn't exist
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Directory '{folder_name}' created.")

# Create full file path
file_path = os.path.join(folder_name, file_name)

# Write to the file
with open(file_path, 'w') as f:
    f.write("This is the first line.\n")
print(f"File '{file_name}' created and written to.")

# Append to the file
with open(file_path, 'a') as f:
    f.write("This line was appended.\n")
print("Text appended to the file.")

# Read the file
with open(file_path, 'r') as f:
    content = f.read()
print("File content:\n", content)

# Rename the file
new_file_path = os.path.join(folder_name, new_file_name)
os.rename(file_path, new_file_path)
print(f"File renamed to '{new_file_name}'.")

# Get file details
print("Absolute path:", os.path.abspath(new_file_path))
print("File exists?", os.path.isfile(new_file_path))
print("File size (bytes):", os.path.getsize(new_file_path))

# Delete the file
os.remove(new_file_path)
print(f"File '{new_file_name}' deleted.")

# Clean up directory
os.rmdir(folder_name)
print(f"Directory '{folder_name}' deleted.")
