import os

path = "/Users/caosai/Desktop/app_logs2"

files = os.listdir(path)


for file in files:
    if ".DS_Store" not in file:
        # print(file)
        pwd = "/Users/caosai/Desktop/app_logs2/" + file
        str1 = "cat %s | awk '{print $7}' |sort | uniq -c" % (pwd,)

        os.system(str1)

