# -*- coding:utf-8 -*-


def main():
    with open("/Users/saicao/Desktop/aa.txt") as f:
        all = f.readlines()

        for line in all:
            # print("private String " + line[1:line.find("`", 1)] + ";")
            print(line[1:line.find("`", 1)] + " AS")



if __name__ == '__main__':
    main()