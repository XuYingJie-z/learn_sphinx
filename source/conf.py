# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys


sys.path.append("scripts")
from gallery_directive import GalleryDirective
import pydata_sphinx_theme

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# 文件开头的信息
project = 'test'
copyright = '2022, yingjie'
author = 'yingjie'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxext.rediraffe",
    "sphinx_design",
    "sphinx_copybutton",
    # For extension examples and demos
    # "ablog",  # 生成 blog 的插件，暂时不需要
    "jupyter_sphinx",
    "matplotlib.sphinxext.plot_directive",
    "myst_nb",
    # "nbsphinx",  # Uncomment and comment-out MyST-NB for local testing purposes.
    "numpydoc",
    "sphinx_togglebutton",
]


autosummary_generate = True

## myst 的拓展
# This allows us to use ::: to denote directives, useful for admonitions
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
]
myst_url_schemes = ("http", "https", "mailto")
nb_execution_mode = "auto" # 不执行 jupyter notebook

templates_path = ['_templates']
exclude_patterns = ["tmp"]  # 排除tmp文件夹


language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']
# logo 暂时没有
# html_logo = "_static/logo.svg"
# html_favicon = "_static/logo.svg"
html_css_files = [
    'css/custom.css',
]

# markdown 配置

from recommonmark.parser import CommonMarkParser
source_suffix = {
    '.rst': 'restructuredtext',
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',
}
source_suffix = [".rst",'.md', ".ipynb"]


# header 栏的配置

## html 主题的配置
html_theme_options = {

    "header_links_before_dropdown": 4,

    # "use_edit_page_button": True,
    "show_toc_level": 2,
    "navbar_align": "left",  # [left, content, right] For testing that the navbar items align properly
    "navbar_center": [ "navbar-nav"]

}

def setup(app):
    # Add the gallery directive
    app.add_directive("gallery-grid", GalleryDirective)
