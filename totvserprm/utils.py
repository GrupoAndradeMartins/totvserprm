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


class BaseClass(object):
    def __init__(self, classtype):
        self._type = classtype

def ClassFactory(name, argnames, BaseClass=BaseClass):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            # here, the argnames variable is the one passed to the
            # ClassFactory call
            if key not in argnames:
                raise TypeError("Argument %s not valid for %s"
                    % (key, self.__class__.__name__))
            setattr(self, key, value)
        BaseClass.__init__(self, name[:-len("Class")])
    newclass = type(name, (BaseClass,),{"__init__": __init__})
    return newclass
