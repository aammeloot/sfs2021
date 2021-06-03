import binascii

# Open in binary
pics = ['get_rich_quick.jpg', 'hacker.jpg', 'linux.jpg']

# Open each file individually
for p in pics:
    f = open('files_week5/'+p, 'rb')
    result = binascii.hexlify(f.read(3))
    f.close
    print("File signature for " + p)
    print(result)
    if result != b'ffd8ff':
        print("WARNING:", p,"is suspicious")
