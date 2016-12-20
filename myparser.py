import xml.sax
class Handler(xml.sax.ContentHandler):
    def __init__(self):
        pass

    def startElement(self, element, attr):
        pass

    def endElement(self, element):
        if element == "line":
            print(self.text)

    def characters(self, text):
        self.text = text


