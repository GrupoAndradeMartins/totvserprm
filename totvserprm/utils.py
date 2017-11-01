# -*- coding: utf-8 -*-
from lxml import etree, objectify
from io import StringIO, BytesIO
import xml.etree.ElementTree as ET

def normalize_tags(root):
    root.tag = root.tag.lower()
    for child in root:
        normalize_tags(child)

def normalize_attr(root):
    for attr,value in root.attrib.items():
        norm_attr = attr.lower()
        if norm_attr != attr:
            root.set(norm_attr,value)
            root.attrib.pop(attr)

    for child in root:
        normalize_attr(child)

def normalize_xml(xml):
    parser = etree.XMLParser(ns_clean=True)
    tree   = etree.parse(StringIO(unicode(xml)), parser)
    root = tree.getroot()
    normalize_tags(root)
    normalize_tags(root)
    return ET.tostring(root)
