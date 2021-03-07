# 变量和常量
变量和常量的定义如字面上的表示。

变量：在程序执行的过程中，定义的存储空间存储的内容**会**被改变。

常量：在程序执行的过程中，定义的存储空间存储的内容**不会**被改变。

不是所有的语言都会有变量和常量的，有些语言不能定义常量。

![images|387x130](https://cdn.ossez.com/discourse-uploads/original/2X/e/e9b6f7dbaf6e6157b36e61cce79aec73a7c44065.png)

比如说：**Python 没有常量**。

对于 Java，我们可以使用关键字来定义一个常量。例如，我们可以使用下面的语句在 Java 程序中定义个一常量 DAYS_IN_WEEK，这个常量在程序的过程中是不能够被改变的。

```
static final int DAYS_IN_WEEK = 7;
```

Python 没有这个常量的定义。

![python-variables3|555x203](https://cdn.ossez.com/discourse-uploads/original/2X/8/84dfd55cd3230addeac1acddc5fcc88574b979db.png)

## 指定类型
Python 在定义变量的时候是不需要强制指定类型的。

我们都知道在计算机存储的时候都会定义一些基础的数据类型，比如说整型，字符串类型等。

Python 在定义变量的时候是不需要指定的类型的，有关变量的类型是是什么，Python 将会在定义变量并且初始化的时候进行指定。

这个与 Java 是相对的，Java 语言在定义变量或者常量的时候，必须要指定变量类型，这就导致了在 Java 语言中存在有大量的数据类型转换方法，并且在运行的时候也会经常出现类型错误或者 Null 对象异常。

当然，Python 也提供了类型转换的函数供你使用，只是这些类型转换的函数远没有 Java 那么多。

## 初始化
Python 在定义变量后，需要马上初始化。

换句话说说，Python 不能定义空对象，这个与 Python 的变量类型是相同的，因为不对 Python 的变量初始化的话，Python 没有办法知道你定义的变量类型是什么。

与 Java 相对，Java 就可以定义空对象，然后在运行的时候进行初始化。

## 本地变量和全局变量
这个定义比较简单，就是定义在函数内的变量为本地变量。

如果变量定义在函数外，那么这个变量就是全局变量。

## 变量实例
针对上面有关变量的定义，我们将会在下面对变量的定义进行一些实际上的应用。

### 定义变量和使用变量
下面的代码显示了对变量的定义和使用。

```python
# 创建变量和指定变量类型
x = 1  # 变量赋值定义一个变量x
print(id(x))  # 打印变量x的标识
print(x + 1)  # 使用变量

x = 2  # 量赋值定义一个变量x
print(id(x))  # 此时的变量x已经是一个新的变量
print(x + 1)  # 名称相同，但是使用的是新的变量x

x = 4  # x 是整数类型的
x = "OSSEZ"  # x 类型将会修改为字符串
print(x)
```

当你运行上面的程序后，程序将会输出为：

```text
2131838986544
2
2131838986576
3
OSSEZ
```

![python-v-01|674x500](https://cdn.ossez.com/discourse-uploads/original/2X/2/2671ed853eed10737b2e9a680778ffc5b1c1e30b.png)

从上面的代码，你可以看到 Python 是如何定义变量的，并且 Python 的变量是如何被修改的。

id 是一个获得 Python 对象 ID 的函数。

在 Python 中是使用对象的，因此你定义的变量是一个对象，使用 id 这个函数可以找到你定义对象的引用。

### 变量类型转换
和所有的程序语言都一样，如果使用了变量，但是变量是不同的数据类型，那么就会涉及到类型的转换。

Python 也提供了一些类型转换的函数，能够用于帮你将 Python 的变量类型完成转换。

考察下面的代码：

```python
# 类型转换
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0
```

经过上面的函数进行转换后，不同的变量将会被使用不同的变量类型。

![python-v-02|690x238](https://cdn.ossez.com/discourse-uploads/optimized/2X/f/f43e23132355e6c301b071a5994d11676373f503_2_690x238.png)

通过 IDE 的调试窗口，我们就可以看到变量被定义的类型和使用。

### 获得变量类型
如果你对你 Python 使用的变量类型不是非常清楚的话，你可以使用函数 type 来获得变量的类型。

通常如果使用 IDE 的话，IDE 会告诉你的变量类型是什么。

考察下面的代码：
```python
x = 5
y = "John"
print(type(x))
print(type(y))
```

上面的代码将会输出
```text
<class 'int'>
<class 'str'>
```

通过上面的输出内容，我们就非常容易明白在 Python 中你定义的变量使用的数据类型是什么。

![python-v-03|690x364](https://cdn.ossez.com/discourse-uploads/original/2X/7/7b226789e2bd294f0474cbf91ce85a68f776f214.png)

如果我们使用 IDE 的调试模式的话，我们可以非常容易的在 IDE 中设置断点。

然后通过断点的查看数据类型来查看你定义的数据类型是什么。
