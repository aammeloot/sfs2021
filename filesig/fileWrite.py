# Write a haiku

haiku = ['','','']
print("Enter the three lines of a haiku below")

# Input of the lines
haiku[0] = input("Enter first line")
haiku[1] = input("Enter second line")
haiku[2] = input("Enter third line")

# Write the content into a file
f = open("haiku.txt", "wt")

for l in haiku:
    f.write(l + '\n')

f.close()
