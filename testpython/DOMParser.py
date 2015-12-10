#xml 解析
#会产生3个事件：
#start_element事件，在读取<a href="/">时；节点开始事件
#char_data事件，在读取python时；节点读取text事件
#end_element事件，在读取</a>时。节点结束事件
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):

    def startparser(self,name,attrs):
        print("sax startparser %s %s" % (name,attrs))

    def chardata(self,name):
        print("sax chardata %s " % (name))

    def endparser(self,name):
        print("sax endparser %s " % (name))

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()

parser.StartElementHandler = handler.startparser
parser.EndElementHandler = handler.endparser
parser.CharacterDataHandler = handler.chardata
print('**********************************Start parser xml**********************************')
parser.Parse(xml)
print('**********************************End parser xml**********************************')

#HtmlParser
from html.parser import HTMLParser

class MyHtmlParser(HTMLParser):
    def handle_charref(self, name):
        print('&#%s;' % name)

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_data(self, data):
        print(data)

    def handle_startendtag(self, tag, attrs):
        print("start end tag %s attrs %s" % (tag,attrs))

    def handle_endtag(self, tag):
        print("end tag %s " %(tag))

    def handle_starttag(self, tag, attrs):
        print("start end tag %s attrs %s" % (tag,attrs))
html = '''<html>
                <head>我是head</head>
                <body>

       '''
parser = MyHtmlParser()
parser.feed(html)
print('once feed success')
parser.feed('''<!-- test html parser -->
                    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
                </body>
</html>''')