
# 学习 sphinx

## 开始之前

* 可以用 markdown 也可以用rst 语法
* 文本文件在 source 文件夹下面，编译好的文件在 build文件夹下面
* 整个文档的设置是在 config.py 中修改，我这里用的是 [pyData Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/index.html)



### 安装依赖和开始编译

* [sphinx official page](https://github.com/sphinx-doc/sphinx) 安装 sphinx
* 

```
pip install sphinx
pip install myst jupyter_sphinx myst_nb
pip install pydata_sphinx_theme  # sphinx 主题
```

* 安装完成之后开始编译

```
# sphinx-quickstart # 这个命令可以在空文件夹中创建 sphinx 项目，但不是必须的，可以直接复制老项目的结构。
sphinx-build -M html source build   # source 文件夹里面是文档，build 文件夹是目标文件夹，build 完成后 html 文件在build 文件夹下的 html 文件夹下


```


## 开始

### 文档首页
* 文档的首页就是 source 文件夹下面的 index.md 文件
* 文件头是一些设置，TODO 具体怎么修改
```
---
myst:
  html_meta:
    "description lang=en": |
      Top-level documentation for pydata-sphinx theme, with links to the rest
      of the site..
html_theme.sidebar_secondary.remove: False
---

```

* 然后是下面的目录，:maxdepth:  调整显示到几级目录(可以显示页面下面的目录)
* 下面的示例就是文件的路径，指向 source 文件夹下的 sphinx_guide 文件夹中的 index.md 文件

```{toctree}
:maxdepth: 1

sphinx_guide/index
review/index

```
### 具体文本文档

* md 文件的文件头

```
---
file_format: mystnb
---

```

