from lxml import etree

# 读取 setitem.xml 文件
setitem_tree = etree.parse('setitem.xml')
setitem_root = setitem_tree.getroot()

print("setitem.xml 文件中的 id:")
for item in setitem_root.findall('.//id'):
    print(item.text)

# 读取 item_armors.xml 文件
item_armors_tree = etree.parse('item_armors.xml')
item_armors_root = item_armors_tree.getroot()

print("item_armors.xml 文件中的 id:")
for item in item_armors_root.findall('.//id'):
    print(item.text)