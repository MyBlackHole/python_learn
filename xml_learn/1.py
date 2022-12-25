from xml.etree import ElementTree
from xml.etree.ElementTree import tostring

# root节点
eve = ElementTree.Element("fyu")
# 二级节点
eve_1 = ElementTree.SubElement(eve, "name", attrib={"en": "yes"})
# 三级节点
eve_2 = ElementTree.SubElement(eve_1, "age", attrib={"checked": "no"})
# 生成文档
tree = ElementTree.ElementTree(eve_1)

# 写入文件
tree.write("learn.xml", encoding="utf-8", short_empty_elements=False)

print(tostring(tree.getroot()))
