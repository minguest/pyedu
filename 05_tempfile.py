import tempfile
import time
# filename= tempfile.mkstemp()
# print(filename)

f= tempfile.TemporaryFile()
while True:
    time.sleep(1)
    print("...")
f.close()