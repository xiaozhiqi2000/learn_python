# 今天主要内容
1. [json]()
2. [pickle]()
3. [XML]()
4. [PyYAML]()
5. [configparser]()
6. [shutil]()

## json模块

Python中用于序列化的两个模块

json     用于【字符串】和 【python基本数据类型】 间进行转换
pickle   用于【python特有的类型】 和 【python基本数据类型】间进行转换
- json()将字符串形式的列表或字典转换为list或dict类型，json是所有语言相互通信的方式
- 注意外层字符形式一定是''单引号,'{"a":"xiao","b":"xiao"}'列表或字典中的字符串一定要""双引号,否则报错
```
import json
 
# json.dumps() 将python基本数据类型转化成字符串形式
dic = {'k1':'v1'}
print(dic,type(dic))
result = json.dumps(dic)
print(result,type(result))
  
# json.loads() 将python字符串形式转化成基本数据类型
s = '{"k1":123}'
dic = json.loads(s)
print(dic,type(dic))
 
# json.dump() 先序列化，再写入文件
li = [11,22,33]
json.dump(li,open('db','w'))
 
# json.load() 读取文件反序列化
l = json.load(open('db','r'))
print(l,type(l))
```
## pickle模块

pickple只有python才能用,用于复杂类型的序列化,(如果是序列化一个对象,在别的模块中反序列化的时候一定要导入该对象所属的类,否则报错)
```
import pickle
 
# pickle.dumps() 序列化
li = [11,22,33]
r = pickle.dumps(li)
print(r)
 
# pickle.loads() 反序列化
result = pickle.loads(r)
print(result,type(result))
 
# pickle.dump() 先序列化，再写入文件
l1 = [11,22,33,55]
pickle.dump(l1,open('db','wb'))
 
# pickle.load() 读取文件反序列化
result1 = pickle.load(open('db','rb'))
print(result1,type(result1))
```

## XML模块

xml是实现不同语言或程序之间进行数据交换的协议，跟json差不多，但json使用起来更简单，不过，古时候，在json还没诞生的黑暗年代，大家只能选择用xml呀，至今很多传统公司如金融行业的很多系统的接口还主要是xml
```
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2023</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
</data>
```
[XML文件xo.xml]()

### 1.解析XML两种方法
- (1)利用ElementTree.XML将字符串解析成xml对象
```
from xml.etree import ElementTree as ET
 
str_xml = open('xo.xml', 'r').read()    # 打开文件，读取XML内容
root = ET.XML(str_xml)    # 将字符串解析成xml特殊对象，root代指xml文件的根节点
```
- (2)利用ElementTree.parse将文件直接解析成xml对象
```
from xml.etree import ElementTree as ET
 
tree = ET.parse("xo.xml")   # 直接解析xml文件
root = tree.getroot()   # 获取xml文件的根节点
```

### 2.操作XML
- (1)遍历XML文档的所有内容
```
上面两种解析XML方法随便一种获取到了xml的root节点 
root = tree.getroot()   # 获取xml文件的根节点
 
print(root.tag)  # 顶层标签
 
# 遍历XML文档的第二层
for child in root:
    # 第二层节点的标签名称和标签属性
    print(child.tag, child.attrib)
    # 遍历XML文档的第三层
    for i in child:
        # 第二层节点的标签名称和内容
        print(i.tag,i.text)
```
- (2)遍历XML中指定的节点
```
上面两种解析XML方法随便一种获取到了xml的root节点 
root = tree.getroot()   # 获取xml文件的根节点

print(root.tag) # 顶层标签
 
# 遍历XML中所有的year节点
for node in root.iter('year'):
    # 节点的标签名称和内容
    print(node.tag, node.text)
```
- (3)修改节点内容
```
由于修改的节点时，均是在内存中进行，其不会影响文件中的内容。所以，如果想要修改，则需要重新将内存中的内容写到文件。
解析字符串方式，修改，保存

上面两种解析XML方法随便一种获取到了xml的root节点 
root = tree.getroot()   # 获取xml文件的根节点

print(root.tag) # 顶层标签
 
# 循环所有的year节点
for node in root.iter('year'):
    # 将year节点中的内容自增一
    new_year = int(node.text) + 1
    node.text = str(new_year)
 
    # 设置属性
    node.set('name', 'alex')
    node.set('age', '18')
    # 删除属性
    del node.attrib['name']
 
# 保存文件
tree = ET.ElementTree(root)
tree.write("newnew.xml", encoding='utf-8')
```
- (4)删除节点
```
上面两种解析XML方法随便一种获取到了xml的root节点 
root = tree.getroot()   # 获取xml文件的根节点
print(root.tag)         # 顶层标签
 
# 遍历data下的所有country节点
for country in root.findall('country'):
    # 获取每一个country节点下rank节点的内容
    rank = int(country.find('rank').text)
 
    if rank > 50:
        # 删除指定country节点
        root.remove(country)
 
# 保存文件
tree = ET.ElementTree(root)
tree.write("newnew.xml", encoding='utf-8')
```
### 3. 创建XML文档
- 创建方式（一）
```
from xml.etree import ElementTree as ET
 
# 创建根节点
root = ET.Element("famliy")
 
# 创建节点大儿子
son1 = ET.Element('son', {'name': '儿1'})
# 创建小儿子
son2 = ET.Element('son', {"name": '儿2'})
 
# 在大儿子中创建两个孙子
grandson1 = ET.Element('grandson', {'name': '儿11'})
grandson2 = ET.Element('grandson', {'name': '儿12'})
son1.append(grandson1)
son1.append(grandson2)
 
# 把儿子添加到根节点中
root.append(son1)
root.append(son1)
 
tree = ET.ElementTree(root)
tree.write('oooo.xml',encoding='utf-8', short_empty_elements=False)
```
- 创建方式（二）
```
from xml.etree import ElementTree as ET
 
# 创建根节点
root = ET.Element("famliy")
 
# 创建节点大儿子
son1 = ET.SubElement(root, "son", attrib={'name': '儿1'})
# 创建小儿子
son2 = ET.SubElement(root, "son", attrib={"name": "儿2"})
 
# 在大儿子中创建一个孙子
grandson1 = ET.SubElement(son1, "age", attrib={'name': '儿11'})
grandson1.text = '孙子'
 
 
et = ET.ElementTree(root)  #生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True, short_empty_elements=False)
```
- 由于原生保存的XML时默认无缩进，如果想要设置缩进的话， 需要修改保存方式：
```
from xml.etree import ElementTree as ET
from xml.dom import minidom
 
def prettify(elem):
    """
    将节点转换成字符串，并添加缩进。
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")
 
# 创建根节点
root = ET.Element("famliy")
 
# 创建大儿子
# son1 = ET.Element('son', {'name': '儿1'})
son1 = root.makeelement('son', {'name': '儿1'})

# 创建小儿子
# son2 = ET.Element('son', {"name": '儿2'})
son2 = root.makeelement('son', {"name": '儿2'})
 
# 在大儿子中创建两个孙子
# grandson1 = ET.Element('grandson', {'name': '儿11'})
grandson1 = son1.makeelement('grandson', {'name': '儿11'})

# grandson2 = ET.Element('grandson', {'name': '儿12'})
grandson2 = son1.makeelement('grandson', {'name': '儿12'})
 
son1.append(grandson1)
son1.append(grandson2)
 
# 把儿子添加到根节点中
root.append(son1)
root.append(son1)
 
raw_str = prettify(root)
 
f = open("xxxoo.xml",'w',encoding='utf-8')
f.write(raw_str)
f.close()
```
### 4.命名空间
[详细介绍](http://www.w3school.com.cn/xml/xml_namespaces.asp)
```
from xml.etree import ElementTree as ET
 
ET.register_namespace('com',"http://www.company.com") #some name
 
# build a tree structure
root = ET.Element("{http://www.company.com}STUFF")
body = ET.SubElement(root, "{http://www.company.com}MORE_STUFF", attrib={"{http://www.company.com}hhh": "123"})
body.text = "STUFF EVERYWHERE!"
 
# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(root)
 
tree.write("page.xml",
           xml_declaration=True,
           encoding='utf-8',
           method="xml")
```

## PyYAML模块

Python也可以很容易的处理ymal文档格式，只不过需要安装一个模块，参考文档：http://pyyaml.org/wiki/PyYAMLDocumentation 

























