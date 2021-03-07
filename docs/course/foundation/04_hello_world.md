# 第一个 Hello World 程序
按照计算机教学体系的传统套路，通常在学习一门语言的第一个程序就是在电脑屏幕上输出 Hello World。

这个页面中的内容能够让你在计算机屏幕上输出字符到屏幕上，同时我们会做得更多一些，将会在命令行控制台中进行输出，我们也会在 IDE 中进行输出。

同时我们还会解释一下输出函数和提供几个实用的小案例。

因为针对计算机的开发多会使用 IDE，因此我们会首先尽量使用 IDE 来输出内容，然后再会捎带一下在控制台上如何输出。

## print 函数
在 Python 中使用的是 print 函数来在计算机上输出你想要输出的东西。

你可以在 print 函数中指定不同的参数来达到不同的目的。

最最简单的办法就是不加入任何内容，直接输出一个句子，如下面的代码

```python
print('hello, world!')
```

## Git 代码仓库
完整的代码，请参考 https://github.com/cwiki-us-docs/python-tutorials/blob/master/tests/HelloWorld.py 页面中的内容，你也可以将上面的项目下载到你的计算机上直接运行。

有关本文档的所有代码也都提交到上面的仓库中了。

## IDE 运行
当你下载 HelloWorld.py 文件到你的本地计算机中，并且已经将我们这个项目导入到 IDE 后，你可以直接在 IDE 上运行 HelloWorld.py 这个文件。

当你运行完成后，你应该可以在你的控制台上看到 HelloWorld.py 运行后的输出。

在 PyCharm 或者 IntelliJ IDEA 运行的方法就是，选择你需要运行的 py 文件，单击鼠标右键，然后选择 Run。

如下图显示的运行方法：

![IDE-python-hello-world-00|387x500](https://cdn.ossez.com/discourse-uploads/original/2X/9/9f219d78fe6b7124d8d6fe481e615f4acb434905.png)

然后在控制台中，你就可以看到上面的方法的输出了。

![IDE-python-hello-world-01|690x406](https://cdn.ossez.com/discourse-uploads/optimized/2X/3/3934138669943464c54c2c551789f8158f20cb27_2_690x406.png)

### IDE 使用的一个小技巧
打开 HelloWorld.py 文件，我们可以看到在这个文件里面有多个 print 函数。

可能你对这个函数不是非常了解。

如果你使用的是 IntelliJ IDEA IDE 的话，你可以将鼠标移动到 print 方法上面，然后使用快捷键 Ctrl +Q，这个时候 IntelliJ IDEA 将会弹出一个浮动窗口。

在这个浮动窗口中有对 print 这个函数的说明，包括可以接受那些参数，可以做什么样的计算。

![IDE-python-hello-world-02|391x399](https://cdn.ossez.com/discourse-uploads/original/2X/c/c39fd4c07afe538e4ffc49051d55722877f17ee4.png)

这就是我们常说的使用 IDE 的好处，能够快速帮你搜索一些文档，你就不需要导出到网站上去搜索参考了。


## 命令行运行
当然我们也可以在命令中运行我们的 Python 代码。

在这个命令行运行中，我们分为在 IDE 的命令行中运行和普通的命令行工具中运行，如果你使用的是 Mac 系统的话，你可以使用你的终端工具。如果你使用的是 Windows 系统的话，那么就需要使用 CMD 或者 PS 了。

### IDEA 命令行运行
在 IntelliJ IDEA 中你是可以启用终端的。

启用终端的快捷键为 Alt + F12，或者你也可以使用你的鼠标来选择终端。当终端被选定后， IDEA 将会默认把路径设置到当前项目的根目录下面。

![IDEA|690x452](https://cdn.ossez.com/discourse-uploads/original/2X/a/a80f68e8267f76fa8c5470b3d83435965b33b865.png)

根据我们当前的项目，我们知道我们的 HelloWorld.py 文件在路径 tests/HelloWorld.py 下面

如果我们希望在终端中测试运行 HelloWorld.py 的话。

你可以在终端工具中输入命令来进行执行。

```
python tests/HelloWorld.py
```

如果系统没有提示路径错误的话，那么你将会看到在你的终端中输出程序运行的结果。

当然，你也可以输入 py + 程序的路径来运行，效果和输入 python 是相同的。

```
py tests/HelloWorld.py
```

![IDEA-terminal-02|690x282](https://cdn.ossez.com/discourse-uploads/original/2X/0/04125f4045f7881dac3fe77b3cafc3ddcb58acff.png)

甚至，你还可以直接输入 py，这个时候将会启动进入 Python 的解释环境中。

然后你输入代码

```python
print('hello, world!')
```

你可以看到在你的终端工具中，python 解释器帮你解释了代码并且运行后输出了结果。

![IDEA-terminal-03|690x177](https://cdn.ossez.com/discourse-uploads/optimized/2X/e/e20395ba2725d17b72b2e241cf09fdb9b508e170_2_690x177.png)

简单来说，在 IDEA 的终端工具中，你可以认为 IDEA 帮你启动了一个 CMD 命令行工具，然后你可以在这个命令行工具中执行任何你想要的操作。

其效果与在命令行中执行是一样的。


