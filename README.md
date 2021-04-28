# 为postman测试准备的简单接口
## 内容简介
* 使用的是Django 3.1.2
* 内含目录页、登录页、成功页、添加页、更新页、删除页以及一个按账号搜索的URL
* 目前包含了get方法、post方法、put方法和delete方法
* "软件测试展示.postman_collection.json"为postman的测试设置文件
## 测试说明
* get搜索测试：http://127.0.0.1:8000/app01/findUser/
* get登录测试：http://127.0.0.1:8000/app01/login/（按账号搜索）
* post添加测试：http://127.0.0.1:8000/app01/addUser/（账号与密码）
* post登录测试：http://127.0.0.1:8000/app01/login/
* put更新测试：http://127.0.0.1:8000/app01/ajax_put/
* delete删除测试：http://127.0.0.1:8000/app01/ajax_delete/
* （后两种测试需<Headers增加参数：Content-Type 为：application/x-www-form-urlencoded, X-Requested-With  为：xmlhttprequest>
* <Body选择为：x-www-form-urlencoded，更新内容为序号、账号、密码，删除内容为序号）>