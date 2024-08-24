import os
# print(os.environ["PATH"])

# os.chdir("c:/")
# print(os.getcwd())

f= os.popen("dir")
print(f.read())