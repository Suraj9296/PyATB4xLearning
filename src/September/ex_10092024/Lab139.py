import os


print(os.name)
if os.name == "posix":
    print("using mac")
else:
    print("windows")
print(os.getcwd())