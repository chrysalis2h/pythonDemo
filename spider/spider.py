# coding=utf-8

from html.parser import HTMLParser
import requests

# 创建类MyHTMLParser并继承HTMLParser
class MyHTMLParser(HTMLParser):
    #重写handle_starttag方法
    def handle_starttag(self, tag, attrs):
        print ("开始标签  :", tag)
        for attr in attrs:
            print ("     属性:", attr)

    #重写handle_endtag方法
    def handle_endtag(self, tag):
        print ("结束标签  :", tag)

    #重写handle_data方法
    def handle_data(self, data):
        print ("数据     :", data)

    #重写handle_comment方法
    def handle_comment(self, data):
        print ("注释     :", data)

    #重写handle_charref方法
    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print ("Num ent  :", c)

    def handle_decl(self, data):
        print ("Decl     :", data)


if __name__ == "__main__":
    url = 'https://www.infoq.cn/public/v1/meeting/get_ppt_list'
    result = requests.get(url)
    print(result)
    parser = MyHTMLParser()
    parser.feed('<html><head></head><body><p class = "aa" >Some&nbsp;<a href=\"#123\">html</a>parser&#62;<!-- comment --><br>END</p></body></html>')