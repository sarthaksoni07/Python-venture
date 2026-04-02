try:
    f= open("one.txt","r")
except FileNotFoundError:
    print("the file was not found")
else:
    print("file found and opened")
