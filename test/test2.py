import random


def m1(*number):
    # total = 0
    # for i in number:
    #     total = total + i
    #
    # print(total)

    m2(*number)

    print("-"*20)

def m2(*number):
    total = 0
    for i in number:
        total = total + i

    print(total)



def m3():
    a = [1, 2, 0]
    num = random.choice(a)
    print("被除术 ",num)
    return num

def m4():
    a = [1, 2, 0]

    retry_numbers=0

    while retry_numbers<10:
        num = random.choice(a)
        print("选取的随机数 ", num)

        # 随机数为0, 则停止循环
        if num==0:
            return num

        retry_numbers +=1


if __name__ == '__main__':

    m4()

    # m1(1, 2, 3, 4)

    # try:
    #     for i in range(10):
    #         print(i)
    #         print(i/m3())
    # except Exception as e:
    #     print(e)

    #
    # for i in range(10):
    #     try:
    #         print(i/m3())
    #     except Exception as e:
    #         print(e)
