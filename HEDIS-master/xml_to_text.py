import re
from lxml import etree as et
import os


try:
    from cStringIO import StringIO
except:
    from io import StringIO

def chief(xml_path):
	text_lines = StringIO()
	xml_file = open(xml_path)
	data = xml_file.read()
	try:
		datastr = data.read()
	except AttributeError:
		datastr = data
	doc = et.fromstring(datastr.encode('utf-8'))
	pages = doc.findall('Page')
	for page in pages:
		zones = page.findall('Zone')
		for zone in zones:
			lines = zone.findall('Line')
			for line in lines:
				text_lines.write(line.find('OCRCharacters').text)
				text_lines.write(" ")
	return text_lines.getvalue()





	



