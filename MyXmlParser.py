import xml.etree.ElementTree as ET
import conf
import re
from WriteResultXML import XMLResultWriter
__author__ = 'vladymyr'


class myXMLParser:

    resultWriter = XMLResultWriter()

    def __init__(self, path):
        tree = ET.parse(path)
        self.root = tree.getroot()
        self.info = conf.getInfoList()

# returns list of root children tag texts
    def getDirectChildrenTagText(self, tagName):
        res = []
        for tag in self.root.findall(tagName):
            res.append((tag.text, tag.get("name")))
        return res

    def findWholeWord(self, w):
        f = format(w)
        return re.compile(ur'\b({0})\b'.format(w), re.UNICODE|re.IGNORECASE)\
            .search

    def searchForInfo(self, content, info):   # finds info in content
        for word in info:
            if (self.findWholeWord(word)(unicode(content))):
                print(word)
                return True
        return False

    def parseRss(self, text):
        try:
            rss = ET.fromstring(text)
            i = 0
            for item in rss.iter('item'):
                for child in item:
                    content = child.text
                    if (child.tag == "title" or child.tag == "description"):
                        if (self.searchForInfo(content, self.info)):
                            # search for Ukrainian city
                            # print("title: " + item.find("title").text)
                            # print("description: " + item.find("description").text)
                            print("link: "
                                    + item.find("link").text)
                            myXMLParser.resultWriter.add(
                                item.find("title").text,
                                item.find("description").text)
        except Exception:
            print("some error occured")






