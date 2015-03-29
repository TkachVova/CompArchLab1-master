__author__ = 'roman'

import xml.etree.ElementTree as ET


class XMLResultWriter:

    root = []
    tree = []
    arr = []

    def __init__(self):
        self.root = ET.Element("root")

    def add(self, title, description):
        if (self.notsameadd(title) == 1):
            return 1

        field1 = ET.SubElement(self.root, "item")

        field2 = ET.SubElement(field1, "title")
        field2.text = title

        field2 = ET.SubElement(field1, "description")
        field2.text = description

    def notsameadd(self, elem):
        for i in self.arr:
            if i == elem:
                return 1

        self.arr.append(elem)
        return 0

    def prettify(self):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = ET.tostring(self.root, encoding='utf-8', method='xml').decode('utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="\t")

    def writefile(self, filename):
        f = open(filename, 'a')
        f.write(ET.tostring(self.root, encoding='utf-8', method='xml'))
        f.close()