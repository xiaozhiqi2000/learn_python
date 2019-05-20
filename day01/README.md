# 今天主要内容
1. [python对象](https://github.com/xiaozhiqi2000/learn_python/tree/master/day01#python%E5%AF%B9%E8%B1%A1%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD)
2. [变量定义](https://github.com/xiaozhiqi2000/learn_python/tree/master/day01#%E5%8F%98%E9%87%8F)
3. [字符编码](https://github.com/xiaozhiqi2000/learn_python/tree/master/day01#%E5%AD%97%E7%AC%A6%E7%BC%96%E7%A0%81)
4. [运算符](https://github.com/xiaozhiqi2000/learn_python/tree/master/day01#%E8%BF%90%E7%AE%97%E7%AC%A6)
5. [If流程控制](https://github.com/xiaozhiqi2000/learn_python/tree/master/day01#if%E6%B5%81%E7%A8%8B%E6%8E%A7%E5%88%B6)
6. [For/While循环](https://github.com/xiaozhiqi2000/learn_python/tree/master/day01#forwhile%E5%BE%AA%E7%8E%AF)
7. [输入/输出/注释](https://github.com/xiaozhiqi2000/learn_python/tree/master/day01#%E8%BE%93%E5%85%A5%E8%BE%93%E5%87%BA%E6%B3%A8%E9%87%8A)
8. [格式化输出](https://github.com/xiaozhiqi2000/learn_python/tree/master/day01#%E6%A0%BC%E5%BC%8F%E5%8C%96%E8%BE%93%E5%87%BA)

## python对象相关术语
1. python对象：
   - 程序中存储的所有数据都是对象
   - 每个对象都有一个身份、一个类型和一个值
      - 例如，school='MaGe Linux'会以 'MaGe Linux' 创建一个字符串对象，其身份是指向它在内存中所处位置的指针(其在内存中的地址),而school就是引用这个具体位置的名称
   - 对象的类型也称对象的类别，用于描述对象的内部表示及它支持的方法和操作
   - 创建特定类型的对象时，有时也将该对象称为该类型的实例
   - 实例被创建后，其身份和类型就不可改变
      - 如果对象的值是可修改的，则称为可变对象
      - 如果对象的值不可修改，则称为不可变对象
   - 如果某个对象包含对其他对象的引用，则将其称为容器
   - 大多数对象都拥有大量特有的数据属性和方法
      - 属性：与对象相关的值
      - 方法：被调用时将在对象上执行某些操作的函数
      - 使用点(.)运算符可以访问属性和方法
2. 对象的身份与类型
   - python内置函数id()可返回一个对象的身份，即该对象在内存中的位置
   - is 运算符用于比较两个对象的身份
   - type() 用于返回一个对象的类型
   - 对象类型本身也是一个对象，称为对象的类
      - 该对象的定义是唯一的，且对于某类型的所有实例都是相同的
      - 所有类型对象都有一个指定的名称，可用于执行类型检查,如list、dict
     ```
     >>> num1 = 5
     >>> num2 = 5
     >>> num1 == num2 #值比较
     >>> True
     
     >>> id(num1)     #内存中的地址
     9119808
     >>> id(num2)
     9119808
     
     >>> num1 is num2 #身份比较
     True
     
     >>> type(num1) is type(num2) #类型比较
     True
     ```

## 变量
1. 变量声明
   - Python将所有数据存为内存对象
   - Python中，变量事实上是指向内存对象的引用
   - 动态类型：在任何时刻，只要需要，某个对象引用都可以重新引用一个不同的对象（可以是不同的数据类型）内建函数type()用于返回给定数据项的数据类型
   - "="用于将变量名与内存中的某个对象绑定：如果对象实现存在，就直接进行绑定；否则，则由"="创建引用的对象,变量名也是对象存在内存，比如：name='jerry',name这个指针指向jerry，name='tom'的时候，name是指针指向tom，但是jerry仍在内存中存放着，只是没有被变量名指向，到一定时候会被垃圾收集器回收，和java有点像。其中当test='jerry'时，test和name这两个变量名指向内存的地址是一样的。id(test),id(name)，变量名是内存引用的标识或符号。
2. 变量定义的规则
   - 变量名只能是 字母、数字或下划线的任意组合
   - 变量名的第一个字符不能是数字
   - 以下关键字不能声明为变量名
     ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise','return', 'try', 'while', 'with','yield']
3. 变量最佳命名方式
   - 使用下划线'_'作为连接,如 name_variables
   - 使用大小写,称为驼峰法,如 NameVariables,nameVariables
   - 注意：两种命名方式不要混用,只要你喜欢的一种即可
4. 变量命名惯例
   - 以单一下划线开头的变量名(_x)不会被from module import * 语句导入
   - 以两个下划线开头但结尾没有下划线的变量名(__x)是类的本地变量
   - 前后有双下划线的变量名(__x__)是系统定义的变量名，对python解释器有特殊意义
   - 交互式模式下，变量名"_"用于保存最后表达式的结果

## 字符编码
1. ASCII

   ASCII（American Standard Code for Information Interchange，美国标准信息交换代码）是基于拉丁字母的一套电脑编码系统，主要用于显示现代英语和其他西欧语言，其最多只能用 8 位来表示（一个字节），即：2**8 = 256-1，所以，ASCII码最多只能表示 255 个符号，python2.x解释器默认是ASCII编码。显然ASCII码无法将世界上的各种文字和符号全部表示，所以，就需要新出一种可以代表所有字符和符号的编码，即：Unicode 
   二进制和数字转换：128 64 32 16 8 4 2 1  比如：2表示二进制 0000 0010 
   字符和数字转换 ： 查看ASCII码表  比如： A字母 表示数字是65，二进制是0100 0001
2. Unicode

   Unicode（统一码、万国码、单一码）是一种在计算机上使用的字符编码。Unicode 是为了解决传统的字符编码方案的局限而产生的，它为每种语言中的每个字符设定了统一并且唯一的二进制编码，规定所有的字符和符号最少由 16 位来表示（2个字节），即：2 **16 = 65536，注：此处说的的是最少2个字节，可能更多，比如汉字就需要3个字节，python3.x解释器默认是Unicode编码。
3. UTF-8

   是对Unicode编码的压缩和优化，他不再使用最少使用2个字节，而是将所有的字符和符号进行动态分类：ASCII码中的内容用1个字节保存、欧洲的字符用2个字节保存，汉字用3个字节保存...

## 运算符
1. 算数运算
![](/day01/imgs/1.png)
2. 比较运算
![](/day01/imgs/2.png)
3. 赋值运算
![](/day01/imgs/3.png)
4. 逻辑运算
![](/day01/imgs/4.png)
5. 成员运算
![](/day01/imgs/5.png)
6. 身份运算
![](/day01/imgs/6.png)
7. 位运算
![](/day01/imgs/7.png)
8. 运算符优先级
![](/day01/imgs/8.png)

## If流程控制
1. if语法结构
   ```
   if boolean_expression1:
       suite1
   elif boolean_expression2:
       suite2
   else:
       else_suite
   ```
2. python中真和假
   - 非0数字为真，否则为假
   - 非空对象为真，否则为假
   - None则始终为假
   比较和相等测试会递归地应用于数据结构中
   返回值为True或False
3. 测试操作符
   - == 操作符测试值的相等性
   - is 表达式测试对象的一致性
   - in 成员关系测试
   - X and Y: 与运算
   - X or Y: 或运算
   - not X : 非运算
4. if/else三元表达式
   ```
   if Y:
       A = X
   else
       A = Z
   
   简写：
   A = X if Y else Z
   ```

## For/While循环
   循环机制及应用场景
   - while循环：
      - 用于编写通用迭代结构
      - 顶端测试为真即会执行循环体，并会重复多次测试知道为假后执行循环后的其他语句
   - for循环：
      - 一个通用的序列迭代器，用于遍历任何有序的序列对象内的元素
      - 可用于字符串、元组、列表和其他的内置可迭代对象，以及通过类所创建的新对象
   - 控制循环 
      - break: 跳出最内层的循环
      - continue: 跳出所处的最近层循环的开始处
      - pass: 占位语句 

## 输入/输出/注释
1. input
   - python3中格式化输出默认接收的都视为字符串
   - 如果你获取的是要数字类型则需要另外强制转换为int()转换为数字类型才能获得数字
2. print
   - print("String %format1 %format2 ...." %(variable1,variable2))
   - print("String" + variable1)
3. 注释
   - #号可以从一行的任何地方开始
   - '''''',"""""",三引号用于多行注释
   - \,表示续行符 
   注意：如果''''''三引号是在一个def 函数或者class 定义类的下方则是对这个函数或者类的说明,可以通过__doc__动态获得文档子串

## 格式化输出
1. 百分号格式化
```
%[(name)][flags][width][.precision]typecode ....
```
- (name) 可选，用于选择指定的key
- flags 可选，可供选择的值有:
   - \+ 右对齐；正数前加正好，负数前加负号；
   - \- 左对齐；正数前无符号，负数前加负号；
   - 空格 右对齐；正数前加空格，负数前加负号；
   - 0 右对齐；正数前无符号，负数前加负号；用0填充空白处
- width 可选，占有宽度
- .precision 可选，小数点后保留的位数
- typecode 必选
   - s，获取传入对象的__str__方法的返回值，并将其格式化到指定位置
   - r，获取传入对象的__repr__方法的返回值，并将其格式化到指定位置
   - c，整数：将数字转换成其unicode对应的值，10进制范围为 0 <= i <= 1114111（py27则只支持0-255）；字符：将字符添加到指定位置
   - o，将整数转换成 八 进制表示，并将其格式化到指定位置
   - x，将整数转换成十六进制表示，并将其格式化到指定位置
   - d，将整数、浮点数转换成 十 进制表示，并将其格式化到指定位置
   - e，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（小写e）
   - E，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（大写E）
   - f， 将整数、浮点数转换成浮点数表示，并将其格式化到指定位置（默认保留小数点后6位）
   - F，同上
   - g，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是e；）
   - G，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是E；）
   - %，当字符串中存在格式化标志时，需要用 %%表示一个百分号

   注意：%s, %d, %f这3个是非常常用的,当不确定用%s or %d,最好使用%s不会出错
   ```
   d = {'x':32,'y':27.49325,'z':65}
   print('%(x)-10d %(y)0.3g' % d)
   
   tpl = "i am %s" % "tomcat"
    
   tpl = "i am %s age %d" % ("tomcat", 18)
    
   tpl = "i am %(name)s age %(age)d" % {"name": "tomcat", "age": 18}
    
   tpl = "percent %.2f" % 99.97623
    
   tpl = "i am %(pp).2f" % {"pp": 123.425556, }
    
   tpl = "i am %.2f %%" % {"pp": 123.425556, }
   ```

2. Format()方式
```
[[fill]align][sign][#][,][width][.precision][type]
```
- fill 可选，空白处填充的字符
- align 可选，对齐方式（需配合width使用）
   - <，内容左对齐
   - \>，内容右对齐(默认)
   - =，内容右对齐，将符号放置在填充字符的左侧，且只对数字类型有效。 即使：符号+填充物+数字
   - ^，内容居中
- sign 可选，有无符号数字
   - +，正号加正，负号加负；
   - -，正号不变，负号加负；
- 空格，正号空格，负号加负；
- \# 可选，对于二进制、八进制、十六进制，如果加上#，会显示 0b/0o/0x，否则不显示
- ，可选，为数字添加分隔符，如：1,000,000
- width 可选，格式化位所占宽度
- .precision 可选，小数位保留精度
- type 【可选】格式化类型
   - 传入” 字符串类型 “的参数
      - s，格式化字符串类型数据
      - 空白，未指定类型，则默认是None，同s
   - 传入“ 整数类型 ”的参数
      - b，将10进制整数自动转换成2进制表示然后格式化
      - c，将10进制整数自动转换为其对应的unicode字符
      - d，十进制整数
      - o，将10进制整数自动转换成8进制表示然后格式化；
      - x，将10进制整数自动转换成16进制表示然后格式化（小写x）
      - X，将10进制整数自动转换成16进制表示然后格式化（大写X）
      - 传入“ 浮点型或小数类型 ”的参数
      - e，转换为科学计数法（小写e）表示，然后格式化；
      - E，转换为科学计数法（大写E）表示，然后格式化;
      - f，转换为浮点型（默认小数点后保留6位）表示，然后格式化；
      - F，转换为浮点型（默认小数点后保留6位）表示，然后格式化；
      - g，自动在e和f中切换
      - G，自动在E和F中切换
      - %，显示百分比（默认显示小数点后6位）
   ```
   tpl = "i am {}, age {}, {}".format("seven", 18, 'alex')
   
   tpl = "i am {}, age {}, {}".format(*["seven", 18, 'alex'])
   
   tpl = "i am {0}, age {1}, really {0}".format("seven", 18)
   
   tpl = "i am {0}, age {1}, really {0}".format(*["seven", 18])
   
   tpl = "i am {name}, age {age}, really {name}".format(name="seven", age=18)
   
   tpl = "i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 18})
   
   tpl = "i am {0[0]}, age {0[1]}, really {0[2]}".format([1, 2, 3], [11, 22, 33])
   
   tpl = "i am {:s}, age {:d}, money {:f}".format("seven", 18, 88888.1)
   
   tpl = "i am {:s}, age {:d}".format(*["seven", 18])
   
   tpl = "i am {name:s}, age {age:d}".format(name="seven", age=18)
   
   tpl = "i am {name:s}, age {age:d}".format(**{"name": "seven", "age": 18})
   
   tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
   
   tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
   
   tpl = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
   
   tpl = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)
   
   ```
