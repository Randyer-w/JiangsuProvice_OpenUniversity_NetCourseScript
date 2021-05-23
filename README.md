
### 1、摘要

本项目是朋友找我帮他弄得,原来的存储库里面因为commit记录中可以看到密码，我已经删除了。

前后进行了四次修复和调试，目前来说应该是没有问题了。

### 2、请求

因为脚本刚发布没多久，有一位老哥fork了我的老仓库，如果老哥看得见的话，麻烦把fork的仓库delete一下，然后fork这个仓库。

另外没有太多问题需要修复的话基本不会再往仓库修改和增加代码了。

### 3、模块

大部分都是自带的模块，用到的三方模块有：requests和beautifulsoup4 (都是pip install的安装名称，直接安装即可)

另外，开启代理可能会引起requests请求报错，务必关闭代理使用。


### 4、错误

代码属于一次性用品，从头到尾没有做任何异常处理，现简单说明出现异常的情况：

1、账号密码错误，导致无法正常截取302跳转拿到location

2、页面改版，登录页面的元素改变，无法正常找到页面中的参数从而报错

3、报出Json错误，一般来说这种情况属于IP被临时ban了，无法获取到返回数据。

4、长时间无回显，和3的情况相同，也可能是自己网络原因，因为没有设置timeout参数。

## MIT License
```
MIT License

Copyright (c) 2021 JdeshengKno

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

