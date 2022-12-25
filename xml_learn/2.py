from xml.etree.ElementTree import Element, tostring


def dict_to_xml(tag, d):
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        child.set("wo", "BlackHole")
        elem.append(child)
    return elem


s = {"a": 1, "B": "b", "c": "C"}
e = dict_to_xml("stock", s)
print(tostring(e).decode())
