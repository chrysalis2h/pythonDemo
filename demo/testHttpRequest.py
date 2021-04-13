# This is a sample Python script.
import json

import requests


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def downloadPPT():
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.
    url = 'https://www.infoq.cn/public/v1/meeting/get_ppt_list'
    data = {}
    header = {'Referer': 'https://www.infoq.cn/video/9KXwCVpqGoMsOZVd34Y6'}
    result = requests.post(url, data, headers=header)
    if result.status_code == 200:
        resultObj = json.loads(result.text)
        data = resultObj['data']
        exist_list = []
        for dataItem in data:
            ppt_list_url = dataItem["ppt_list_url"]
            if ppt_list_url not in exist_list:
                exist_list.append(ppt_list_url)
        return exist_list
    print("end")


def forEachDownload():
    resultLists = []
    for i in range(20):
        oneRequest = downloadPPT()
        for oneRequestItem in oneRequest:
            if oneRequestItem not in resultLists:
                resultLists.append(oneRequestItem)
                print(f'ppt_list_url ===== {oneRequestItem}')
    print('==============================================')
    # print(f'resultLists ==== {resultLists}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    forEachDownload()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
