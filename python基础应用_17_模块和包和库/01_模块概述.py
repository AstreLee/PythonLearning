# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/15 - 15:53
@file : 01_模块概述.py
@ide : PyCharm
"""


"""
模块概述：
1. 一个模块就是一个py结尾的python文件
2. 对于同一类型的模块进行有效的管理，Python中引入了包(package)来组织模块。
包是Python模块文件所在的目录，并且在该目录下必须有一个名为_init_.py的文件；
否则，Python就将该目录作为普通目录，而不是一个包。_init_.py可以是一个空文件，也可以包含Python代码
3. 具有相关功能的模块和包组合在一起就形成了库，如Python标准库等。按照来源来分：Python中的库可以
分为三类：标准库(Python自带)、第三方库和自定义库
"""