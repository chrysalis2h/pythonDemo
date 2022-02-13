# This is a sample Python script.
import json
import requests
from lxml import etree
import time
import wget

# 设置请求载体
headers = {
    # 在浏览器中，network查看
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
}

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def getHtml():
    htmlUrl = 'https://wangxiao.xisaiwang.com/rk/xxzl/1001.html'
    resqonse = requests.get(htmlUrl, headers=headers)
    # 参考链接 https://www.cnblogs.com/sanyue/p/15272889.html
    # 获取页面资源
    page_text = resqonse.text
    # 构造一个etree对象
    tree = etree.HTML(page_text)
    # 从根节点开始，通过属性名称获取,如果属性名唯一，则中间层可以直接 //表示
    pdfNamePList = tree.xpath('/html//div[@id="div_content"]//li[@class=" clearfix"]//div[@class="content-mind"]/p[1]/text()')
    pdfUrlAList = tree.xpath('/html//div[@id="div_content"]//a[@class="btn-small-down download"]/@data-url')

    for index in range(len(pdfNamePList)):
        print('---------------Start---------------')
        print("Start : %s" % time.ctime())
        pdfName = pdfNamePList[index]
        dataUrl = pdfUrlAList[index]
        print(index)
        print('-----' + pdfName + '-----' + dataUrl)
        try:
            # 保存的路径
            path = 'D:/Downloads/idmdownload/xisai-3/' + pdfName + '.pdf'
            # 下载
            wget.download(dataUrl, path)
        except:
            print('exception:' + '-----' + pdfName + '-----' + dataUrl)
        print("End : %s" % time.ctime())
        time.sleep(1)
        print('---------------End---------------')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    getHtml()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
