#####  安装pycrypto报错之旅
> 1. pip install pycrypto 安装报错error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools
>    ![第一次报错](http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1593765216636.png)
>    根据报错提示，缺少Microsoft Visual C++ 14.0必要组件，<a href="https://pan.baidu.com/s/1OM5yw7w2ai6HWgCexcgOww">点击下载</a> 提取码：ogpp   Microsoft Visual C++ 14.0 工具安装 
>    添加用户变量，注意是用户变量  VCINSTALLDIR=C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC
>    进命令终端执行命令 set CL=/FI"%VCINSTALLDIR%\INCLUDE\stdint.h" %CL%

> 2. 再次执行pip install pycrypto 安装命令报错：error: command ‘C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\BIN\\x86_amd64\\cl.exe‘ failed with exit status 2
>    ![第二次报错](http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1593766569703.png)
>    修改inttypes.h文件：
>    ①先复制stdint.h文件到inttypes.h文件同目录下
>    stdint.h文件位置是安装Microsoft Visual Studio 14.0工具的目录，例如：C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\include
>    ![安装目录](http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1593766842489.png)
>    inttypes.h文件目录，报错日志：C:\Program Files (x86)\Windows Kits\10\include\10.0.10240.0\ucrt\inttypes.h
>    ②修改inttypes.h文件
>    将 #include <stdint.h> 修改成 #include "stdint.h"

> 3.执行 pip install pycrypto 安装成功
> 
