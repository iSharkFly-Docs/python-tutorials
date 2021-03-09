# 关键字
很多语言都是有关键字的，Python 也不例外。

不同的编程语言提供了不同的保留关键字集，但是在所有编程语言中都有一个重要且通用的规则，我们不能使用保留关键字来命名我们变量、函数、类、模板以及其他对象命名。

Python 是大小写敏感（区分大小写）的， and 是关键字，AND 就不是关键字了。

程序语言关键字的作用通常有一些特定的用途，比如说 Python 的 import，就是用来导入包的。

如果尝试在 Python 中使用关键字定义变量的话，编译器将会提示错误。


![kw-error-01|563x287](https://cdn.ossez.com/discourse-uploads/original/2X/5/5e57e65eaeec5f7ede4749c7c2cf559a9671f85f.png)

## 关键字数量
可以使用下面的方法来查看 Python 的关键字。

```python
import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))
```

首先可以使用 import keyword 来导入包，然后就可以通过上面的方法打印 Python 的关键字，然后使用 len 函数查看关键字的数量。

我们可以知道 Python 3.9 的版本一共有 36 个关键字。

不同的 Python 版本关键字数量不一样。

![kw-error-02|690x183](https://cdn.ossez.com/discourse-uploads/optimized/2X/d/d231c5dec0ede5c01230b3833706e9dba8f01b17_2_690x183.png)

因为不同版本的关键字数量不一样，因此我们就不在这里列出来了，请使用上面的代码直接跑一下就可以查看当前版本的关键字列表了。