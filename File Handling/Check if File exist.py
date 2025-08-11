import os
if os. path.exists("demo"):
    os.remove("demo.txt")
else:
    print("The file does not exist")
