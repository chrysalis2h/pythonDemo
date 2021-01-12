# This is a sample Python script.
import requests
from yahoo_finance import Share


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def testnumpy():
    yahoo = Share('YHOO')
    print(yahoo.get_open())


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def testRequest():
    # Use a breakpoint in the code line below to debug your script.
    url = 'https://www.infoq.cn/public/v1/meeting/get_ppt_list'
    data = {}
    header = {'Referer': 'https://www.infoq.cn/video/9KXwCVpqGoMsOZVd34Y6'}
    result = requests.post(url, data, headers=header)
    print(result.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    testnumpy()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
