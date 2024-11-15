import os
import random
import pandas as pd
from lxml import etree

# 定义 random_value 函数
def random_value(min_val, max_val):
    if isinstance(min_val, str) and '%' in min_val:
        min_val = float(min_val.strip('%')) / 100
        max_val = float(max_val.strip('%')) / 100
        return f"{random.uniform(min_val, max_val) * 100:.0f}%"
    else:
        return random.randint(int(min_val), int(max_val))

# 读取 attr.xlsx 文件并指定列名
attr_df = pd.read_excel('attr.xlsx', header=None, names=['校验值', '属性', '最小值', '最大值'])
print(attr_df.columns)  # 打印列名以检查它们是否正确
attr_dict = {}
for _, row in attr_df.iterrows():
    key = row['校验值']
    if key not in attr_dict:
        attr_dict[key] = []
    attr_dict[key].append((row['属性'], row['最小值'], row['最大值']))

# 检查 XML 文件是否存在，如果不存在则创建一个新的
xml_file = 'setitem_new.xml'
if not os.path.exists(xml_file) or os.path.getsize(xml_file) == 0:
    root = etree.Element("root")
    tree = etree.ElementTree(root)
    tree.write(xml_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# 检查 string_new.xml 文件是否存在，如果不存在则创建一个新的
string_xml_file = 'string_new.xml'
if not os.path.exists(string_xml_file) or os.path.getsize(string_xml_file) == 0:
    string_root = etree.Element("string")
    string_tree = etree.ElementTree(string_root)
    string_tree.write(string_xml_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# 初始化 id
id = 1001
string_id = 901001

# 读取 setitem2.txt 文件
rows = []
with open('setitem2.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            rows.append(line)
        else:
            # 将当前的 rows 添加到 XML 文件中
            if rows:
                tree = etree.parse(xml_file)
                root = tree.getroot()
                new_element = etree.Element("setitem")
                
                # 添加 id 标签
                id_element = etree.Element("id")
                id_element.text = str(id)
                new_element.append(id_element)
                
                # 生成 name 标签内容
                first_row = rows[0]
                name_parts = first_row.split('_')
                name = '_'.join(name_parts[:1] + name_parts[2:])
                
                # 添加 name 标签
                name_element = etree.Element("name")
                name_element.text = name
                new_element.append(name_element)
                
                # 添加 desc 标签
                desc_element = etree.Element("desc")
                desc_element.text = name + "_desc"
                new_element.append(desc_element)
                
                # 添加 item 标签
                for i, row in enumerate(rows):
                    item_element = etree.Element(f"item{i+1}")
                    item_element.text = row
                    new_element.append(item_element)
                
                # 生成 piece_bonus2 和 piece_bonus3 标签内容
                prefix = first_row[:2]
                if prefix in attr_dict:
                    attrs = random.sample(attr_dict[prefix], 4)
                    piece_bonus2 = f"{attrs[0][0]} {random_value(attrs[0][1], attrs[0][2])};{attrs[1][0]} {random_value(attrs[1][1], attrs[1][2])}"
                    piece_bonus3 = f"{attrs[2][0]} {random_value(attrs[2][1], attrs[2][2])};{attrs[3][0]} {random_value(attrs[3][1], attrs[3][2])}"
                    
                    # 添加 piece_bonus2 标签
                    piece_bonus2_element = etree.Element("piece_bonus2")
                    piece_bonus2_element.text = piece_bonus2
                    new_element.append(piece_bonus2_element)
                    
                    # 添加 piece_bonus3 标签
                    piece_bonus3_element = etree.Element("piece_bonus3")
                    piece_bonus3_element.text = piece_bonus3
                    new_element.append(piece_bonus3_element)
                
                root.append(new_element)
                tree.write(xml_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')
                
                # 向 string_new.xml 添加信息
                string_tree = etree.parse(string_xml_file)
                string_root = string_tree.getroot()
                string_element = etree.Element("string")
                
                # 添加 id 标签
                string_id_element = etree.Element("id")
                string_id_element.text = str(string_id)
                string_element.append(string_id_element)
                
                # 添加 name 标签
                string_name_element = etree.Element("name")
                string_name_element.text = desc_element.text
                string_element.append(string_name_element)
                
                # 添加 body 标签
                string_body_element = etree.Element("body")
                string_body_element.text = f"第{string_id}号套装"
                string_element.append(string_body_element)
                
                string_root.append(string_element)
                string_tree.write(string_xml_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')
                
                # 更新 id
                id += 1
                string_id += 1
                rows = []

# 处理文件末尾没有空行的情况
if rows:
    tree = etree.parse(xml_file)
    root = tree.getroot()
    new_element = etree.Element("setitem")
    
    # 添加 id 标签
    id_element = etree.Element("id")
    id_element.text = str(id)
    new_element.append(id_element)
    
    # 生成 name 标签内容
    first_row = rows[0]
    name_parts = first_row.split('_')
    name = '_'.join(name_parts[:1] + name_parts[2:])
    
    # 添加 name 标签
    name_element = etree.Element("name")
    name_element.text = name
    new_element.append(name_element)
    
    # 添加 desc 标签
    desc_element = etree.Element("desc")
    desc_element.text = name + "_desc"
    new_element.append(desc_element)
    
    # 添加 item 标签
    for i, row in enumerate(rows):
        item_element = etree.Element(f"item{i+1}")
        item_element.text = row
        new_element.append(item_element)
    
    # 生成 piece_bonus2 和 piece_bonus3 标签内容
    prefix = first_row[:2]
    if prefix in attr_dict:
        attrs = random.sample(attr_dict[prefix], 4)
        piece_bonus2 = f"{attrs[0][0]} {random_value(attrs[0][1], attrs[0][2])};{attrs[1][0]} {random_value(attrs[1][1], attrs[1][2])}"
        piece_bonus3 = f"{attrs[2][0]} {random_value(attrs[2][1], attrs[2][2])};{attrs[3][0]} {random_value(attrs[3][1], attrs[3][2])}"
        
        # 添加 piece_bonus2 标签
        piece_bonus2_element = etree.Element("piece_bonus2")
        piece_bonus2_element.text = piece_bonus2
        new_element.append(piece_bonus2_element)
        
        # 添加 piece_bonus3 标签
        piece_bonus3_element = etree.Element("piece_bonus3")
        piece_bonus3_element.text = piece_bonus3
        new_element.append(piece_bonus3_element)
    
    root.append(new_element)
    tree.write(xml_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')
    
    # 向 string_new.xml 添加信息
    string_tree = etree.parse(string_xml_file)
    string_root = string_tree.getroot()
    string_element = etree.Element("string")
    
    # 添加 id 标签
    string_id_element = etree.Element("id")
    string_id_element.text = str(string_id)
    string_element.append(string_id_element)
    
    # 添加 name 标签
    string_name_element = etree.Element("name")
    string_name_element.text = desc_element.text
    string_element.append(string_name_element)
    
    # 添加 body 标签
    string_body_element = etree.Element("body")
    string_body_element.text = f"第{string_id}号套装"
    string_element.append(string_body_element)
    
    string_root.append(string_element)
    string_tree.write(string_xml_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')
    
    # 更新 id
    id += 1
    string_id += 1