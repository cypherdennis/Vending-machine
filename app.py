file = open("express.txt", "r+")
content = file.write("\n awesome to hear")
file.close()
print(content)