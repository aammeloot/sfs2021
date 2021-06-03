# Reminder of how to open and manipulate a text file

# Open the file and create a reference to the file
f = open('files_week5/first_haiku.txt')

# Read individual characters
print(f.read(10))
f.seek(0) # Go back to beginning of file

print(f.readline()) # Read a whole line of text
f.seek(0)

lines = f.readlines() # Read all the lines and store in a list
f.close() # Don't forget to close the file when not needed

print(lines)

for l in lines:
    print(l.strip())
