# django_restful 标准API接口开发

#### 介绍
- 基于 django rest framework 开发，重写了部分模块，例如： 分页、过滤、搜索、排序、自定义返回、错误处理、缓存等功能
- 增加 request_id 用于错误排查

#### 软件架构
Python == 3.8+
Django == 4.2

#### 新建沙盒
```bash
python3 -m venv env
source env/bin/activate
```
#### 安装教程

```shell
pip install -r requirements.txt
```


#### 使用说明
1.  python manage.py runserver 0.0.0.0:8000
2.  curl http://localhost:8000/api/
