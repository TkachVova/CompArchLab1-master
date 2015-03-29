__author__ = 'vladymyr'
 # coding=utf8


import unittest
import MyXmlParser
import conf
import xml.etree.ElementTree as ET

test_file_path = "/home/pythonProjects/CompArcLab1.1.1-master/CompArcLab1.1/UnitTest/Test.py"



class MyTest(unittest.TestCase):
    def test_getUrlPath(self):
        str = conf.getUrlPath()
        self.assertEqual(str, '/home/vladymyr/Downloads/CompArchLab1-master/source/urls_uk.xml')

    def test_InfoPath(self):
        str = conf.getInfoPath()
        self.assertEqual(str, '/home/vladymyr/Downloads/CompArchLab1-master/gns/data_uk.txt')


    def test_getDirectChildrenTagText(self):
        xmlParser = MyXmlParser.myXMLParser('/home/vladymyr/Downloads/CompArchLab1-master/source/urls_uk.xml')
        urlList = xmlParser.getDirectChildrenTagText("url")
        self.assertEqual(len(urlList), 3)
        self.assertEqual(urlList[0], ('http://www.pravda.com.ua/rus/rss/', 'pravda'))

    def test_searchForInfo(self):
        xmlParser = MyXmlParser.myXMLParser('/home/vladymyr/Downloads/CompArchLab1-master/source/urls_uk.xml')
        file = open('MyTestRSS.xml', 'r')
        text = file.read()
        rss = ET.fromstring(text)
        for item in rss.iter('item'):
            for child in item:
                content = child.text
                if (child.tag == "title" or child.tag == "description"):
                    self.assertEqual(xmlParser.searchForInfo(content, conf.getInfoList()) , True)

        xmlParser = MyXmlParser.myXMLParser('/home/vladymyr/Downloads/CompArchLab1-master/source/urls_uk.xml')
        file = open('MyTestRSS2.xml', 'r')
        text = file.read()
        rss = ET.fromstring(text)
        for item in rss.iter('item'):
            for child in item:
                content = child.text
                if (child.tag == "title" or child.tag == "description"):
                    self.assertEqual(xmlParser.searchForInfo(content, conf.getInfoList()) , False)


    def test_findWholeWord(self):
        xmlParser = MyXmlParser.myXMLParser('/home/vladymyr/Downloads/CompArchLab1-master/source/urls_uk.xml')
        res = xmlParser.findWholeWord('word')('one ttt word')
        res = xmlParser.findWholeWord(u'Крым')(u'Крым')
        self.assertTrue(xmlParser.findWholeWord('word')('one ttt word'))
        self.assertFalse(xmlParser.findWholeWord(u'Крым')(u'one ttt word'))
        self.assertTrue(xmlParser.findWholeWord(u'Крым')(u'one Крым word'))
        self.assertFalse(xmlParser.findWholeWord('word')('one ttt '))


    def test_ParseRss(self):
        xmlParser = MyXmlParser.myXMLParser('/home/vladymyr/Downloads/CompArchLab1-master/source/urls_uk.xml')
        file = open('MyTestRSS.xml', 'r')
        text = file.read()
        xmlParser.parseRss(text)
        xmlParser.resultWriter.writefile('/home/vladymyr/Downloads/CompArchLab1-master/UnitTests/Testresult.xml')
        fileres = open('Testresult.xml', 'r')
        res = fileres.read()
        self.assertEqual(res,'<root><item><title>Example entry. Крым Russia</title><description>Here is some text containing an interesting description. Крым UKRAINE</description></item></root>')
        fileres = open('Testresult.xml', 'w')