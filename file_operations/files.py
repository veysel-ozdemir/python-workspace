import os

# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if doesn't exist
f = open("file_operations\\names.txt")

print(f.read())  # read whole file
print(f.read(4))  # read first 4 characters

print(f.readline())  # reads the 1st line
print(f.readline())  # reads the 2nd line

for line in f:
    print(line)

f.close()  # close the file (apply changes)

try:
    f = open("file_operations\\names_lists.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()

# Append - creates the file if doesn't exist
f = open("file_operations\\names.txt", "a")
f.write("\nNeil")
f.close()

f = open("file_operations\\names.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("file_operations\\context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("file_operations\\context.txt")
print(f.read())
f.close()

# Two ways to create a new file:
# Opens a file for writing, creates the file if it doesn't exist
f = open("file_operations\\name_list.txt", "w")
f.close()

# Creates the specified file, but retuns an error if the file exists
if not os.path.exists("file_operations\\new_file.txt"):
    f = open("file_operations\\new_file.txt", "x")
    f.close()
else:
    print("The file you wish to create already exists")

# Delete a file
# avoid an error if it doesn't exist
if os.path.exists("file_operations\\phone_list.txt"):
    os.remove("file_operations\\phone_list.txt")
else:
    print("The file you wish to delete doesn't exist")

# using with
with open("file_operations\\more_names.txt") as f:
    content = f.read()

with open("file_operations\\names.txt", "w") as f:
    f.write(content)
