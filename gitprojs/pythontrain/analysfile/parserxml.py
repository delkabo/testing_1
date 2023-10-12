import xml.etree.ElementTree as ET
import re

# Parsing xml file

xml = ET.parse("sample.xml")
root = xml.getroot()

""" print(root.text)
# group() for xmlns in xml file
ns = re.match('{.*}', root.tag).group(0)
featurestag = root.find("{}features".format(ns))
elementtag = featurestag.find("{}element".format(ns))
mariadbt = elementtag.find("{}mariadb".format(ns))

print("the mariadb contains: {}".format(mariadbt.text))
 """
# way 2

for child in root:
    if child.tag == ("{}ip".format("{xmlns}")):
        print(child.tag, child.attrib, child.text)

print(xml.findall('.//mariadb'))