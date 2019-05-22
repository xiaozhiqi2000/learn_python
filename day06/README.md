# 今天主要内容
1. [sys](https://github.com/xiaozhiqi2000/learn_python/tree/master/day06#subprocess%E6%A8%A1%E5%9D%97)
2. [os](https://github.com/xiaozhiqi2000/learn_python/tree/master/day06#os%E6%A8%A1%E5%9D%97)
3. [hashlib](https://github.com/xiaozhiqi2000/learn_python/tree/master/day06#hashlib%E6%A8%A1%E5%9D%97)
4. [random](https://github.com/xiaozhiqi2000/learn_python/tree/master/day06#random%E6%A8%A1%E5%9D%97)
5. [time](https://github.com/xiaozhiqi2000/learn_python/tree/master/day06#time%E6%A8%A1%E5%9D%97)
6. [datetime](https://github.com/xiaozhiqi2000/learn_python/tree/master/day06#datetime%E6%A8%A1%E5%9D%97)
7. [logging](https://github.com/xiaozhiqi2000/learn_python/tree/master/day06#logging%E6%A8%A1%E5%9D%97)
8. [subprocess](https://github.com/xiaozhiqi2000/learn_python/tree/master/day06#subprocess%E6%A8%A1%E5%9D%97)

## sys模块

用于提供对Python解释器相关的操作
```
sys.argv           命令行参数List，第一个元素是程序本身路径
sys.exit(n)        退出程序，正常退出时exit(0)
sys.version        获取Python解释程序的版本信息
sys.maxint         最大的Int值
sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       返回操作系统平台名称
sys.stdin          输入相关
sys.stdout         输出相关
sys.stderror       错误相关
```
进度条示例：
```
#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys
import time

def view_bar(num,total):
    rate = num / total
    rate_num = int(rate * 100)
    r = '\r%s%d%%' % (">"*num,rate_num)
    sys.stdout.write(r)
    sys.stdout.flush()

if __name__ == '__main__':

    for i in range(0, 100):
        time.sleep(0.1)
        view_bar(i, 100)
```
## os模块

用于提供系统级别的操作
```
os.getcwd()                 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")         改变当前脚本工作目录；相当于shell下cd
os.curdir                   返回当前目录: ('.')
os.pardir                   获取当前目录的父目录字符串名：('..')
os.makedirs('dir1/dir2')    可生成多层递归目录
os.removedirs('dirname1')   若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')         生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')         删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')       列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()                 删除一个文件
os.rename("oldname","new")  重命名文件/目录
os.stat('path/filename')    获取文件/目录信息
os.sep                      操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep                  当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep                  用于分割文件路径的字符串
os.name                     字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")   运行shell命令，直接显示,不能保存执行结果<br>os.popen("bash command").read()   运行shell命令,可以保存执行结果
os.environ                  获取系统环境变量
os.path.abspath(path)       返回path规范化的绝对路径
os.path.split(path)         将path分割成目录和文件名二元组返回
os.path.dirname(path)       返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)      返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)        如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)         如果path是绝对路径，返回True
os.path.isfile(path)        如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)         如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)      返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)      返回path所指向的文件或者目录的最后修改时间
```
## hashlib模块

用于加密相关的操作，代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
```
#这是md5加密的,其他sha1、sha256、sha384、sha512换下就好
import hashlib
  
hash = hashlib.md5()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())
print(hash.digest())
```
以上加密算法虽然依然非常厉害，但时候存在缺陷，即：通过撞库可以反解。所以，有必要对加密算法中添加自定义key再来做加密。　　
```
import hashlib
  
hash = hashlib.md5(bytes('898oaFs09f',encoding="utf-8"))
hash.update(bytes('admin',encoding="utf-8"))
print(hash.hexdigest())
```
## random模块
```
import random
  
print(random.random())              # 生成0-1之间的随机小数
print(random.randint(1, 20))        # 生成1到20的整数包括20
print random.uniform(10, 20)        # 生成10到20之间的浮点数
print(random.randrange(1, 10))      # 生成1到10的数字不包括10,第3个参数可以指定步长
print(random.choice(["JGood", "is", "a", "handsome", "boy"])) # 从序列中随机选一个数
 
# 每次对序列随机排序
p = ["Python", "is", "powerful", "simple"]
random.shuffle(p)
print(p)
```
随机6位验证码:
```
#!/usr/bin/env python
#-*-cofding:utf-8-*-
import random

li = []
for i in range(6):
    r = random.randint(0, 4)
    if r == 2 or r == 4:
        num = random.randrange(0, 10)
        li.append(str(num))
    else:
        temp = random.randrange(65,91)
        c = chr(temp)
        li.append(c)

result = "".join(li)
print(result)
```
## time模块

时间相关的操作，时间有三种表示方式：
- 时间戳            1970年1月1日之后的秒，即：time.time()
- 格式化的字符串    2014-11-11 11:11，    即：time.strftime('%Y-%m-%d')
- 结构化时间        元组包含了：年、日、星期等... time.struct_time    即：time.localtime()
```
import time
 
print(time.clock())        #返回处理器时间,3.3开始已废弃
print(time.process_time()) #返回处理器时间,3.3开始已废弃<br>
print(time.time())    #返回当前系统时间戳输出：1471161757.5214906
print(time.ctime())   #输出字符串格式时间：Sun Aug 14 16:04:02 2016 ,当前系统时间
print(time.ctime(time.time()-86640))   #将时间戳转为字符串格式
print(time.gmtime())  #获取结构化时间
print(time.gmtime(time.time()-86640))    #将时间戳转换成struct_time格式
print(time.localtime(time.time()-86640)) #将时间戳转换成struct_time格式,但返回的本地时间
print(time.mktime(time.localtime()))     #与time.localtime()功能相反,将struct_time格式转回成时间戳格式
time.sleep(4)  #睡上4秒
print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()) ) #将struct_time格式转成指定的字符串格式
print(time.strptime("2016-01-28","%Y-%m-%d") ) #将字符串格式转换成struct_time格式
```
## datetime模块
```
import datetime
 
print(datetime.date.today()) #输出格式 2016-01-26
print(datetime.date.fromtimestamp(time.time()-864400) )  #2016-01-16 将时间戳转成日期格式
current_time = datetime.datetime.now() #
print(current_time)   #输出2016-01-26 19:04:30.335935
print(current_time.timetuple())  #返回struct_time格式
  
#datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]])
print(current_time.replace(2014,9,12))  #输出2014-09-12 19:06:24.074900,返回当前时间,但指定的值将被替换
  
str_to_date = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M") #将字符串转换成日期格式
new_date = datetime.datetime.now() + datetime.timedelta(days=10) #比现在加10天
new_date = datetime.datetime.now() + datetime.timedelta(days=-10) #比现在减10天
new_date = datetime.datetime.now() + datetime.timedelta(hours=-10) #比现在减10小时
new_date = datetime.datetime.now() + datetime.timedelta(seconds=120) #比现在+120s
```

## logging模块

很多程序都有记录日志的需求，并且日志中包含的信息即有正常的程序访问日志，还可能有错误、警告等信息输出，python的logging模块提供了标准的日志接口，你可以通过它存储各种格式的日志，logging的日志可以分为 debug(), info(), warning(), error() and critical() 5个级别，下面我们看一下怎么用。

日志级别对应的数字：
```
CRITICAL = 50   ERROR = 40   WARNING = 30   INFO = 20   DEBUG = 10   NOTSET = 0
```
日志记录格式：
```
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息
```
### 1.日志记录到文件
```
import logging
 
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    filename='test.log',
                    filemode='w')
 
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
```
### 2.日志记录到文件并输出到屏幕
```
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import logging
 
#获取日志器对象
logger = logging.getLogger('TEST-LOG')  # 返回一个logger对象,没有指定的话默认是root logger
logger.setLevel(logging.DEBUG)  #设置全局日志级别
 
#定义屏幕控制器把日志输出屏幕
ch = logging.StreamHandler()  
ch.setLevel(logging.DEBUG)   # 输出屏幕的日志级别
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)   # 给输出屏幕的日志设置日志格式
logger.addHandler(ch)        # 将设定好的控制器添加到日志器中
 
#定义文件控制器把日志输出文件
fh = logging.FileHandler("access.log") 
fh.setLevel(logging.WARNING)  #设置输出文件的日志级别
formatter1 = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter1)   # 给输出文件的日志设置日志格式
logger.addHandler(fh)         # 将设定好的控制器添加到日志器中
 
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
```
注意:局部日志级别只有大于全局日志级别才会记录

## subprocess模块

可以执行shell命令的相关模块和函数有：
- os.system('ls')   直接使用shell命令,不能保存运行的结果
- os.popen('ls').read() 直接使用shell命令,可以保存运行的结果
- subprocess

### 1. subprocess.call() 执行命令，返回状态码
- shell=False,第一个参数必须是列表
- shell=True,第一个参数就直接输入命令即可
```
ret = subprocess.call(["ls", "-l"], shell=False)
或
ret = subprocess.call("ls -l", shell=True)
```
### 2. subprocess.check_call() 执行命令，如果执行成功状态码是0，否则抛异常
- shell=False,第一个参数必须是列表
- shell=True,第一个参数就直接输入命令即可
```
ret = subprocess.check_call(["ls", "-l"],shell=False)
print(ret)
ret = subprocess.check_call("exit 1", shell=True)
print(ret)
```
### 3. subprocess.check_output() 执行命令，如果成功状态码是 0 ，则返回执行结果，否则抛异常，注意这里返回的是字节类型,需要转换
- shell=False,第一个参数必须是列表
- shell=True,第一个参数就直接输入命令即可
```
ret = subprocess.check_output(["echo", "Hello World!"],shell=False)
print(str(ret,encoding='utf-8'))
或
ret = subprocess.check_output("exit 1", shell=True)
print(str(ret,encoding='utf-8'))
```
### 4. subprocess.run()  python3.5新加的功能,代替os.system,os.spawn
- shell=False,第一个参数必须是列表
- shell=True,第一个参数就直接输入命令即可
```
import subprocess
subprocess.run(["ls","-l"], shell=False)
total 56
-rw-rw-r-- 1 tomcat tomcat    61  8月 11 23:27 a.py
-rw-rw-r-- 1 tomcat tomcat 12929  8月  8 18:03 a.txt
CompletedProcess(args=['ls', '-l'], returncode=0)
 
subprocess.run("ls -l /dev/null", shell=True, stdout=subprocess.PIPE)
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0, stdout=b'crw-rw-rw- 1 root root 1, 3 Mar 28 17:00 /dev/null\n')
```
### 5. subprocess.Popen()  用于执行复杂的系统命令,是上面方法的底层实现

调用subprocess.run(...)是推荐的常用方法，在大多数情况下能满足需求，但如果你可能需要进行一些复杂的与系统的交互的话，你还可以用subprocess.Popen(),语法如下：
- shell=False,第一个参数必须是列表
- shell=True,第一个参数就直接输入命令即可
```
p = subprocess.Popen("find ~/ -size +1000 -exec ls -shl {} \;",shell=True,stdout=subprocess.PIPE)
print(p.stdout.read())
```
参数：
- args：shell命令，可以是字符串或者序列类型（如：list，元组）
- bufsize：指定缓冲。0 无缓冲,1 行缓冲,其他 缓冲区大小,负值 系统缓冲
- stdin, stdout, stderr：分别表示程序的标准输入、输出、错误句柄
- preexec_fn：只在Unix平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用
- close_sfs：在windows平台下，如果close_fds被设置为True，则新创建的子进程将不会继承父进程的输入、输出、错误管道。
- 所以不能将close_fds设置为True同时重定向子进程的标准输入、输出与错误(stdin, stdout, stderr)。
- shell：同上
- cwd：用于设置子进程的当前目录,相当于shell中cd进入当前目录
- env：用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承。
- universal_newlines：不同系统的换行符不同，True -> 同意使用 \n
- startupinfo与createionflags只在windows下有效
- 将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如：主窗口的外观，进程的优先级等等
(1)输入即可得到输出
```
import subprocess
 
obj = subprocess.Popen(["mkdir","test"],cwd='/tmp/',)
或者
obj1 = subprocess.Popen("mkdir test1", shell=True, cwd='/tmp/',)
```
(2)输入进行某环境，依赖再输入,通过输入，输出，错误管道，输入数据，获取数据
```
import subprocess
 
obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
obj.stdin.write("print(1)\n")
obj.stdin.write("print(2)")
obj.stdin.close()
 
cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()
 
print(cmd_out)
print(cmd_error)
 
或者
obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
obj.stdin.write("print(1)\n")
obj.stdin.write("print(2)")
 
out_error_list = obj.communicate()
print(out_error_list)
 
或者
obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
 
out_error_list = obj.communicate('print("hello")')
print(out_error_list)
```
