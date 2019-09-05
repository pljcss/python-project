import requests

def screen_size():
    """使用tkinter获取屏幕大小"""
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height

if __name__ == '__main__':
    # w,h = screen_size()
    # print(w,h)


    print(requests.get('http://106.12.39.147/').text)