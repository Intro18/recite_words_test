# recite_words_test
###################################################################################

在命令行中启动Python脚本的时候，经常会用到-m参数，那么-m起了什么作用呢？
run library module as a script (terminates option list)意思是将库中的python模块用作脚本去运行。

1.python xxx.py
2.python -m xxx.py
这是两种加载py文件的方式:
1叫做直接运行,要给出路径
2相当于import,叫做当做模块来启动。不需要给出路径自动去查找path里的路径。

###################################################################################

建立虚拟环境:
python -m venv C:\myEnv

激活虚拟环境:
C:\myEnv\\scripts\activate.bat

停止使用虚拟环境:
C:\myEnv\\scripts\deactivate.bat

安装django：因为已经activate了，进入了这个环境里面（变成myEnv$）
所以直接使用pip，会装到当前环境下的Lib\site-packages里
pip install Django 

升级pip程序：
python -m pip install --trusted-host pypi.python.org --upgrade pip

根据文件列表安装所有包：
python -m pip install --trusted-host pypi.python.org -r 文件列表位置

创建django项目
django-admin startproject recite_words_test

创建应用程序
python manage.py startapp recite_words(appname)

以上基本构建命令执行完之后，开始用开发工具编写代码。
如果使用pycharm，打开此工程之后要在Project Interpreter里面设置python.exe路径

常用快捷键
Ctrl + Alt + L     代码格式化
Ctrl + Alt + O     优化导入（去掉用不到的包导入）
Ctrl + 鼠标        简介/进入代码定义    
Ctrl + /           行注释 、取消注释

Ctrl + F          当前文件查找
Ctrl + Shift + F  全局查找

创建表结构
python manage.py migrate

让 Django 知道我们在我们的模型有一些变更
python manage.py makemigrations recite_words

创建指定表结构
python manage.py migrate recite_words

添加超级用户
python manage.py createsuperuser