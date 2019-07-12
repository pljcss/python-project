

if __name__ == '__main__':

    dict1 = {"a":"1","b":"2"}

    del dict1["a"]

    print("c" in dict1)





    with open("/Users/caosai/Desktop/ss1.txt") as f:
        ff = f.readlines()

        for f1 in ff:
            print(f1.strip("\n").strip().split("  "))




