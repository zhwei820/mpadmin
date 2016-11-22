# CMDB-V1.0

运维自动化的核心项目

## 部署准备:

系统使用python3.5.2 + django + MongoDB开发，环境依赖在 requirements.txt 中列出；

方便部署环境隔离，需要先安装python虚拟环境, python3有自己的默认虚拟环境 pyvenv

创建python环境 >> pyvenv CMDBEnv

进入目录 >> cd CMDBEnv

拉取线上代码 >> git clone git@git.yxpopo.com:ops/cmdb.git

启动 CMDBEnv 进入python虚拟环境，在不同系统下的不同启动方式

- linux/mac启动方式：在CMDBEnv目录中执行 >> source bin/activate
- windows启动方式：执行CMDBEnv\Scripts\activate.bat

在python虚拟环境中安装依赖模块，执行 >> pip install -r msg_pusher/requirements.txt ;