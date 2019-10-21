# Mac系统下将python程序打包成mac应用程序

## 1. 安装py2app
```
pip3 install py2app
```


## 2. 生成setup文件
```
py2applet --make-setup xxx.py
```
> #### 2.1 `setup.py`文件是对应用的基本定义
```
from setuptools import setup
APP = ['test.py']
APP_NAME = "TEST"
DATA_FILES = []
OPTIONS = {
'argv_emulation': True,
'iconfile': 'app.icns',
'plist': {
'CFBundleName': APP_NAME,
'CFBundleDisplayName': APP_NAME,
'CFBundleGetInfoString': "taoxx",
'CFBundleIdentifier': "com.taoxx",
'CFBundleVersion': "1.0.0",
'CFBundleShortVersionString': "1.0.0",
'NSHumanReadableCopyright': "Copyright @ 2019, taoxx, All Rights Reserved"
}
}
setup(
name=APP_NAME,
app=APP,
data_files=DATA_FILES,
options={'py2app': OPTIONS},
setup_requires=['py2app'],
)
```
> #### 2.2 资源文件
> 1. 应用图标及其他资源文件都与`setup.py`在同一目录下
> 2. 如果你的应用使用的其他资源文件，应该将其包含在`DATA_FILES`中
>> `DATA_FILES = ['testdata.json', 'picture.png']`

> #### 2.3 png图片转icns图标
>> 1. 准备一张1024X1024或者像素更高的图片，命名为app.png
>> 2. 创建文件夹 app.iconset，手动创建或`mkdir test.iconset`，并将app.png放入该文件夹
>> 3. 转换png图片为各种尺寸
```
$ sips -z 16 16     app.png --out app.iconset/icon_16x16.png
$ sips -z 32 32     app.png --out app.iconset/icon_16x16@2x.png    // 2x是专供Retina屏幕使用的
$ sips -z 32 32     app.png --out app.iconset/icon_32x32.png
$ sips -z 64 64     app.png --out app.iconset/icon_32x32@2x.png
$ sips -z 128 128   app.png --out app.iconset/icon_128x128.png
$ sips -z 256 256   app.png --out app.iconset/icon_128x128@2x.png
$ sips -z 256 256   app.png --out app.iconset/icon_256x256.png
$ sips -z 512 512   app.png --out app.iconset/icon_256x256@2x.png
$ sips -z 512 512   app.png --out app.iconset/icon_512x512.png
$ sips -z 512 512   app.png --out app.iconset/icon_512x512@2x.png
```
>> 4. 打包为icns
```
iconutil -c icns tmp.iconset -o app.icns
```

## 3. 打包应用
> #### 3.1 自己开发，打包速度快。（因为本机安装了依赖库，所以可以直接运行）
```
python3 setup.py py2app -A
```
> #### 3.2 给其他没有sdk的电脑使用，包括lib库
```
python3 setup.py py2app
```

## 4. xxx文件下出现dist文件夹，打开后里面有个app，双击即可运行
![Alt text](/pngpic.iconset/icon_64x64@2x.png)
![Alt text](/app.icns)
