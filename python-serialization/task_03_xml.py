#!/usr/bin/python3
"""XML serialization and deserialization using ElementTree."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file."""
    root = ET.Element('data')

    for key, value in dictionary.items():
        elem = ET.SubElement(root, key)
        elem.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize XML data from a file into a dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        return {child.tag: child.text for child in root}
    except Exception:
        return {}
