
# DOM vs SAX
from xml.parsers.expat import ParserCreate

# 举个例子，当SAX解析器读到一个节点时：
#<a href="/">python</a>
#会产生3个事件：
#start_element事件，在读取<a href="/">时；
#char_data事件，在读取python时；
#end_element事件，在读取</a>时。

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax: start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax: end_element: %s' % name)

    def char_data(self, text):
        print('sax: char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

# 最简单也是最有效的生成XML的方法是拼接字符串
# L = []
# L.append(r'<?xml version="1.0"?>')
# L.append(r'<root>')
# L.append(encode('some & data'))
# L.append(r'</root>')
# return ''.join(L)