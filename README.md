# finalProject

## 一、环境要求

操作系统：Windows 10

语言：python 3.x（3.7以上）+JavaScript+Html+CSS

框架：Flask 2.x+JQuery+Bootstrap

数据库：MySQL（目前用于用户管理）、DophinDB（之后用于实时数据存储）

## 二、运行前准备

### 安装项目所需的python依赖

```python
pip install -r requirement.txt
```

### 修改项目配置文件中数据库配置的相关信息

```python
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:991022@127.0.0.1/stockstar"
```

> 双引号里面格式为：mysql://root:密码@127.0.0.1/stockstar

### 创建MySQL和python的连接：

#### 方法1：先在MySQL数据库创建数据表user，再生成Model

先在MySQL创建数据库stockstar,建user表过程略，建表后，自动生成model的语法如下（使用自己的mysql账号密码）：

```python
flask-sqlacodegen "mysql://root:991022@127.0.0.1/stockstar" --tables user --outfile "common/models/user.py"  --flask
```

#### 方法2：根据flask 中已经创建的Model，生成本地MySQL数据表user

需要先在MySQL中建立stockstar数据库，然后在项目根目录，输入命令：

```python
python manage.py db_init
```

## 三、项目运行

### 方法1：pycharm定位到manage.py运行

### 方法2：cmd定位到项目根目录（flaskProject），使用命令：

```
python manage.py runserver
```


