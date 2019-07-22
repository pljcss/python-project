import os

file_dir = "/Users/caosai/Desktop/interface_count/1、bd-daihou-app/172.20.23.215/"

files = os.listdir(file_dir)


for file in files:
    if ".DS_Store" not in file:
        print(file)
        pwd = file_dir + file
        str1 = "cat %s | awk '{print $7}' |sort | uniq -c" % (pwd, )

        os.system(str1)

