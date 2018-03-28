from xml.sax.handler import ContentHandler
from xml.sax import parse

class PageMaker(ContentHandler):
    def startElement(self, name, attrs):
        print(name,attrs.keys())
parse('data.xml', PageMaker ())