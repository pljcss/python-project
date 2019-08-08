import pandas as pd

def write_csv():
    a = [1,2,3]
    b = [4,5,6]

    dataframe = pd.DataFrame({'name':a,'age':b})

    dataframe.to_csv("/Users/caosai/Desktop/test.csv",index=False,sep=',')


if __name__ == '__main__':
    write_csv()