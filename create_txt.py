#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-18 17:40
# @Author  : taoxx


import subprocess
import os
import time

'''
1. 安装py2app
pip3 install py2app
2. 生成setup文件
py2applet --make-setup create_txt.py
3. 打包
#自己开发，打包速度快。（因为本机安装了依赖库，所以可以直接运行）
python3 setup.py py2app -A
#给其他没有sdk的电脑使用，包括lib库。
python3 setup.py py2app
'''


# textutil -convert txt 文件路径，这句代码中的 txt 处，可以替换为任何你需要转换到的文件格式，
# 文件路径则可以采用拖拽文件到终端的方法自动填充
# 文件格式中互相转换 txt, html, rtf, rtfd, doc, docx, wordml, odt, webarchive


def create_txt():
    home_path = os.environ['HOME']
    desktop = home_path + os.sep + 'Desktop/'
    txt_name = 'undefined_' + time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime()) + '.txt'
    subprocess.run('touch ' + desktop + txt_name + ';open ' + desktop + txt_name, shell=True)
    # print(txt_name, ' has been create.')


def main():
    create_txt()


if __name__ == '__main__':
    main()
