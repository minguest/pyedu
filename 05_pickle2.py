import pickle
f= open("test.txt", "rb")
data= pickle.load(f)
f.close()
print(data)