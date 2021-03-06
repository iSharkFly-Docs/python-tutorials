# 开发工具
要提高软件开发的效率，通常都会推荐使用 IDE 工具来进行开发。

可能很多人都记得在第一次写 Java 程序的时候，很多人都说应该使用记事本来写代码，其实这个感觉有点无聊，能用 IDE 为什么不用而使用记事本呢？

如果使用记事本的话，通常会有一些空格错误，或者变量错误或者是字符串的错误，因此没有任何意义。

在本页中，我们将会介绍一些常用的编辑器。

## IDLE
IDLE 是Python 的 Integrated Development and Learning Environment 首字母的简写。

如果你在 Windows 使用 Python 的安装程序进行安装的话，这个 IDLE 是默认进行安装的。这个是可以直接在 Windows 的运行对话框中输入 idle 运行的。

运行的界面如下图。

![idle-01|468x500](https://cdn.ossez.com/discourse-uploads/original/2X/b/b172baaa638f65e20314bf35b893fc03e39051e4.png)

IDLE 运行界面与使用控制台的运行界面是相同的，只是 IDLE 的界面更好。

相对来说这个编辑器比较简陋，通常没有一些商用编辑器的那么功能强大。

![idle-02|590x229](https://cdn.ossez.com/discourse-uploads/original/2X/c/c51ecf9c63d9e7a33803a0a732237e32b4665531.png)

如果是 Windows 10 的话，可以通过你的 Windows 任务栏来进行启用。当然你也可以在运行中输入 idle 中直接运行。

## IntelliJ IDEA 和 PyCharm
Jetbrains 有很多开发工具，其中最核心的就是 IntellIJ IDEA。

### IntellIJ IDEA 和 PyCharm 的关系

如果你计算机中已经安装了 IntellIJ IDEA Ultimate 版本的话，你可以在 IntellIJ IDEA 中通过安装插件的方式扩展 Python，然后就能达到和 PyCharm 一样的功能了。

![IDEA-01|640x400](https://cdn.ossez.com/discourse-uploads/original/2X/9/992d2e13125dd11768de366f757760b0ac1611d1.png)

因为我们是通过 Java 平台转到一个小项目中使用 Python，所以我们只需要在 IDEA 中安装插件就好了。

所以说 PyCharm 是 IntellIJ IDEA 的一个子集，如果你的公司有 Java 项目同时可能也有 Python 项目需要进行处理的话，只需要有 IntellIJ IDEA 的许可证就可以了。

### 安装插件
在 IntellIJ IDEA 中，安装 Python 插件就可以了。

可以在你的 IntellIJ IDEA 中查看设置以确定插件是否被正确安装了。

![IDEA-02|690x492](https://cdn.ossez.com/discourse-uploads/original/2X/e/e6c45335330c4204bec964cfaeac2dd4b4f6cd9c.png)

如果针对一个特定的项目。你需要确定在你的项目中是否安装了 Python 的 SDK。

如果没有配置Python SDK 的话，你需要配置你的 SDK。

![IDEA-03|690x492](https://cdn.ossez.com/discourse-uploads/original/2X/e/edfed16a6d40ec9fa9bad9c198cd80aac220dbd6.png)

### 运行一个测试程序
如果一切配置准确你，你可以在你的 Python 项目中运行一个 Python 的程序。

比如说我们在这里允许一个 HelloWorld.py 的程序。

右键，然后选择运行。

![IDEA-04|317x500](https://cdn.ossez.com/discourse-uploads/original/2X/8/8a14128b8948156be9178ee702ea2edb4f3cdb8c.png)

随后在控制台中，你应该能够看到你程序运行结果的输出。

![IDEA-05|690x197](https://cdn.ossez.com/discourse-uploads/optimized/2X/1/1d7568c38fb8afd1a00d5b0ffd883a3f21eaedfa_2_690x197.png)

### IntellIJ IDEA 插件配置讨论
有关 IntellIJ IDEA 的 Python 插件配置讨论，请访问下面的链接。

在下面的链接中，我们针对一些常见的问题进行了总结，通常这些可能都是初学者容易遇到的问题。
* [IntelliJ 安装 Python 插件](https://www.ossez.com/t/intellij-python/114)
* [IntelliJ 配置 Python 项目提示 no python interpreter](https://www.ossez.com/t/intellij-python-no-python-interpreter/125)


## Visual Studio Code
Visual Studio Code 是一个免费的开发工具，比较轻量，很多人都会用。

如果你还没有安装 Python 扩展的话，在第一次使用 Visual Studio Code 导入 Python 项目，将会提示你安装 Python 扩展。

### 安装扩展
在 VSC 的右下角，将会提示你安装 Python 扩展。

单击 install 进行安装即可。

![vsc-python-01|690x377](https://cdn.ossez.com/discourse-uploads/original/2X/a/ae9ade24a133d339042e51a2b25712a31f1c3973.png)

下面的图显示扩展正在进行安装。

![vsc-python-023|690x377](https://cdn.ossez.com/discourse-uploads/optimized/2X/5/5d7644fea17c57c8a7a445f08b7cef5e50fa0db3_2_690x377.png)

如果还需要其他一些扩展需要进行安装的话，按照提示进行安装即可。

有可能能够在控制台中看到扩展正在安装的过程。

![vsc-python-03|690x377](https://cdn.ossez.com/discourse-uploads/original/2X/5/5d737321243566f333b5e86f0c8b99c42759d99c.png)

当刷新所有的项目和配置后，可以单击界面上面的小箭头来运行。

![vsc-python-04|690x458](https://cdn.ossez.com/discourse-uploads/optimized/2X/7/79e1b9669d7ec1ed154b6635e83d98b2947d3db4_2_690x458.png)

非常不建议在学习 Python 或者 Java 的时候按照书本上的内容使用记事本来进行开发书写代码，因为这种方式没有任何意义。

同时，学会使用配置 IDE，熟练使用 IDE 中的各种快捷键对以后的开发来说也是一个基本技能。

因为 Visual Studio Code 是免费使用，并且能够很好的结合 Git，因此推荐初学者安装一个进行学习。

如果条件允许，或者经济状况不错的话，IntellIJ IDEA 也是非常好的选择。

## 其他工具
Python 的开发工具不限于上面提到的那几个。

我们在下面列出了一些可能会用到，也可能会听到过的开发工具，如果你还有什么需要补充的也请 Fork 项目后修改。

因为下面的开发工具可能不是非常主流，功能也达不到上面的提到的几个那么强大，但是针对不同的操作系统平台，进行一些尝试也未尝不是好事。

- [IPython](https://ipython.org/) - IPython是一种基于Python的交互式解释器，提供了强大的编辑和交互功能。
- [Eclipse + PyDev](www.pydev.org) - 在 Eclipse 中添加插件，让 Eclipse 能够支持 Python。
- [Sublime Text](http://www.sublimetext.com) - 代码编辑器，这个编辑器比较小巧，有比较完善的社区，但这个编辑器不是免费的。
- [Atom](https://atom.io/) - 能够全平台支持运行，插件安装快速。但 Atom 的插件安装比较繁琐，同时针对 Python 的 debug 功能不是非常好。
- [GNU Emacs](https://www.gnu.org/software/emacs/) - 文本编辑器，多在 Unix/linux 平台上使用。
- [Vi / Vim](https://www.vim.org/) - 文本编辑器，多在 Unix/linux 平台上使用。
- [Spyder](https://github.com/spyder-ide/spyder) - 开源的 Python IDE。
- [Thonny](http://thonny.org/) - 多针对初学者使用的 IDE。塔尔图大学 (University of Tartu)  针对 python 初学者开发的一个款小 IDE，貌似可以在 Raspberry Pi 上安装，能够帮助初学者快速了解下语言。
