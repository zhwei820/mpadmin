## 一、CMDB项目结构

目前分为两部分：

一部分是API，相关接口文档在[API说明](API说明.md)里有，主要功能是
实现对层、组、CI模型、CI对象的增删改查功能。

另一部分是通过Django的Template功能实现了一部分前端页面，包括
CI模型的编辑、CI对象的详情和列表页，目前还不完全。前端页面模版使用了
[AdminLTE](https://github.com/almasaeed2010/AdminLTE)，可以快速
、漂亮的构建出一套UI组件，并且对移动端适配。

## 二、目前存在的问题及解决方向

1. 前端页面的完善。CMDB项目中，前端页面是最复杂的一个部分，之后可能
需要使用React.js或者Vue.js来实现复杂的前端功能（交互动作、数据管理等等）。

2. 后端API的完善。目前主要是基本增删改查功能，之后可能要根据具体需要来
增加相关的API接口（主要使用[django-rest-framework](http://www.django-rest-framework.org)
和[django-rest-framework-mongoengine](https://github.com/umutbozkurt/django-rest-framework-mongoengine)
来快速构建Restful风格的API）。

3. 对CI属性的支持。目前支持的CI属性包括字符串、多行文本、
单选、多选、整数、时间和引用，之后根据具体需要添加其他属性类型。

4. 账户权限管理。目前的django-mongoengine模块有BUG，无法创建用户，因此之后可能需要
手动修复这个BUG，或者换用其他工具。
