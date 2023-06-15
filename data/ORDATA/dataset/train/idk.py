import os

l = os.listdir("./Annotations/")

ann = [i.rstrip(".xml") for i in l]
s = ""
for i in ann:
    s += i + "\n"

f = open("./ImageSets/trainval.txt", "w")
f.writelines(s)
f.close()
