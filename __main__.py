import MyXmlParser
import conf
import gevent
import urllib
import time
import ConfigParser
from gevent import monkey
from WriteResultXML import XMLResultWriter

monkey.patch_all()
__author__ = 'vladymyr'

def fetch(url):
    xmlParser = MyXmlParser.myXMLParser(conf.getUrlPath())
    file = urllib.urlopen(url)
    text = file.read()
    if (text):
        xmlParser.parseRss(text)


class Main:
    def main(self):
        xmlParser = MyXmlParser.myXMLParser(conf.getUrlPath())
        urlList = xmlParser.getDirectChildrenTagText("url")
        print(urlList)
        for url in urlList:
            file = urllib.urlopen(url[0])
            text = file.read()
            # print("\n")
            # print("read", len(text), "bytes in " + url[1])
            if (text):
                xmlParser.parseRss(text)



    def multi_thread(self):
        threads = []
        xmlParser = MyXmlParser.myXMLParser(conf.getUrlPath())
        urlList = xmlParser.getDirectChildrenTagText("url")
        print(urlList)
        for url in urlList:
            threads.append(gevent.spawn (fetch, url[0]))
        gevent.joinall(threads)
        xmlParser.resultWriter.writefile(conf.getResultPath())

m = Main()
resultWriter = XMLResultWriter();
# m.main()

config = ConfigParser.RawConfigParser()
config.read('config.cfg')
an_int = config.getint('Section1', 'an_int')

f = open(conf.getResultPath(), 'w')
f.close()
startTime = time.time()
if an_int == 0:
    m.main()
    print('onethread')
elif an_int == 1:
    m.multi_thread()
    print('multithread')
else:
    print('wrong config')
finishTime = time.time()
print('Time : ')
print(finishTime - startTime)