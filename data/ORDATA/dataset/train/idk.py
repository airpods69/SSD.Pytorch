import os

images = os.listdir("./JPEGImages/")

l = [i.rsplit(".jpg") for i in images]

s = ""
for i in l:
    s += i[0] + "\n"

f = open("./ImageSets/trainval.txt", 'w')
f.writelines(s)
f.close()
