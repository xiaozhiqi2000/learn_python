#!/usr/bin/bash
# 关闭selinux,防火墙,设置vim,安装pyenv,安装virtualenv,安装3.6python

#判定selinux是否开启
getenforce | egrep -qi 'enforcing' &>/dev/null
[ $? -eq 0 ] && setenforce 0 && sed -i 's@SELINUX=enforcing@SELINUX=disabled@' /etc/selinux/config

#判定防火墙是否开启
cat /etc/redhat-release | grep 'release 6' &>/dev/null
if [ $? -e 0 ];then
    service iptables stop && chkconfig iptables off
else
    systemctl stop firewalld && systemctl disable firewalld    
fi

#使用命令行vi模式
egrep '\bvi\b' /etc/bashrc &>/dev/null
[ $? -ne 0 ] &&  echo -e "\nset -o vi\nalias cdnet='cd /etc/sysconfig/network-scripts'\nalias grep='grep --color=auto'\nHISTFILESIZE=10000\nHISTSIZE=10000\nHISTTIMEFORMAT=' %F %T'\nexport HISTFILESIZE HISTSIZE HISTTIMEFORMAT\n" >> /etc/bashrc

. /etc/bashrc



#配置vim使用模式
egrep -q '\bnobackup\b' /etc/vimrc
if [ $? -ne 0 ];then 
echo -e "set nobackup\nset tabstop=4\nset shiftwidth=4\nset expandtab\nset smartindent\nset autoindent\nset fileencoding=utf8\nset fileencodings=utf8,gbk,gb18030,big5,gb2312\nset hidden\nset confirm" >> /etc/vimrc
fi

# 安装依赖环境
yum install git curl unzip lrzsz gcc gcc-c++ -y
yum -y install readline readline-static readline-devel gcc sqlite-devel sqlite zlib zlib-devel bzip2-devel bzip2-libs openssl openssl-devel openssl-static -y

#初始化python环境
result=$(ping -w1 -c1 baidu.com | grep 'packet loss' | awk '{print $6}' | awk -F'%' '{print $1}')
if [ $result -ne 0 ];then
    echo "无法连接网络，检查网络"
else
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv &>/dev/null
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
    source ~/.bash_profile
    pyenv --version
fi


curl -O https://www.python.org/ftp/python/3.6.7/Python-3.6.7.tar.xz &>/dev/null
mkdir ~/.pyenv/cache
mv Python-3.6.7.tar.xz ~/.pyenv/cache
pyenv install 3.6.7 && pyenv global 3.6.7

yum clean all
yum install epel* -y
yum install python-pip -y

pip install virtualenv
virtualenv py36
echo 'source ~/py36/bin/activate' >> ~/.bash_profile
