from time import sleep
import pyodbc
import random
from lxml import etree
import pandas as pd
# Set up the connection string
server = '82.156.19.137'
database = 'xmlparser2'
username = 'sa'
password = 'aion.tera.2020'
driver = '{ODBC Driver 18 for SQL Server}'  # Update the driver if needed

# Establish the connection
conn = pyodbc.connect(f'SERVER={server};DATABASE={database};UID={username};PWD={password};DRIVER={driver};TrustServerCertificate=yes')
# Create a cursor object
cursor = conn.cursor()
# Execute SQL queries
cursor.execute('''select name from [XMLParser2].[dbo].[item_armors] 
               where level>24 and name not like '&pvp%' and name not like '&test%' 
               and quality in ('unique','epic','mythic') and 
               (name  like 'rb%' or name  like 'lt%'or name  like 'ch%'or name  like 'pl%')
''')

?



# ##读取setitem.xml文件中的内容，存入setitem中
# ##读取item_armors.xml文件中的内容，存入item_armors中
# # 读取 setitem.xml 文件
# setitem_tree = etree.parse('setitem.xml')
# setitem_root = setitem_tree.getroot()
# print("setitem.xml 文件中的 id:")
# for item in setitem_root.findall('.//'):
#########处理装备类型###########
#########处理属性###########

#     #打印出所有字段值
#     print(item.text)
#     #打印出所有字段名
#     print(item.tag)

# 读取 item_armors.xml 文件
#item_armors_tree = etree.parse('item_armors.xml')
#item_armors_root = item_armors_tree.getroot()
#print("item_armors.xml 文件中的 id:")
#for item in item_armors_root.findall('.//id'):
#    print(item.text)
#    print(item.text)

##读取属性列表attr.xlsx文件中的内容，存入attr中。每行第一个数据为种类，第二个为属性，第三个为最小值，第四个为最大值，
#打印出文件中的内容
# attrs = pd.read_excel('attr.xlsx', header=None).values.tolist()
# for attr in attrs:
#     print(attr)






##循环1 单次循环可以写setitem.xml文件中的四套数据，并写入四条string，执行次数根据set_tail的长度决定


    ##读取set_tail的第n条数据，存入set_tail(n)中


    ##对比settail(n)是否在setitem中，如果在则跳过这个settail，继续下一个循环1，如果不在setitem中，则继续下面的操作
  

    ##从results中筛选以set_tail(n)结尾的数据，存入mixset中


    ##按照开头的字符串将mixset中的数据分组，以rb开头的数据存入set(1)中,以lt开头的数据存入set(2)中,以ch开头的数据存入set(3)中,以pl开头的数据存入set(4)中


        #id=1000
        ##循环2    单次循环可以写setitem.xml文件中的一套数据，并写入一条string，循环4次写入4中不同护甲类型的数据


            ##循环3 分别读取item
                ##将set(n)第n个数据存入item(i)中
            ##结束循环3
            #for i in range(1, 5):
                #item = set(n)[i]
            
            


            ##循环4 随机属性随机值，取4个
                ##根据attr对应的护甲种类， 选取对应的随机属性prop_name1，并在取值范围内取随机值prop_value1
            ##结束循环4
            #for i in range(1, 5):
                #prop_name1 = attr[i][1]
                #prop_value1 = random.randint(attr[i][2], attr[i][3])



            ##设置xml中的id，id每次加1
            #id += 1

            ##拼name，前两个字符取自护甲类型，后面的字符取自set_tail，用'_'拼成新的set_name
            #set_name = set_tail[n][:2] + '_' + set_tail[n]

            ##拼desc，以set_name开头，以字符'DESC'结尾，以'_'拼接成set_desc
            #set_desc = set_name + '_DESC'

            ##将id的内容写入setitem.xml文件,以xml格式写入,格式为<setitem>/n<id>id</id>/n
                    
            ##将name写入setitem.xml文件，格式为<name>set_name</name>/n   
    
            ##将desc写入setitem.xml文件，格式为<desc>set_desc</desc>/n         

                    
            ##循环5 将装备的内容写入setitem.xml文件,以xml格式写入，格式为<itemn>item(i)</itemn>/n

            ##循环6 将属性的内容写入setitem.xml文件,以xml格式写入，格式为<piece_bonus2>prop_name1,' ',prop_value1,';',prop_name2,' ',prop_value2</piece_bonus2>/n<piece_bonus4>prop_name3,' ',prop_value3,';',prop_name4,' ',prop_value4</piece_bonus4>/n</setitem>/n

            ##写入string*****************************

            ##打印set_name

        ##结束循环2
    
    ##结束循环1


                   




# Close the cursor and connection
cursor.close()
conn.close()