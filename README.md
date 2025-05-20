暂停！程序都运行时OK的，但这只是ESP32S3作为执行的时候。
然而程序已知写不进去，各种软件都试过了，pycharm给的原因比较直接 错误ENODEV 
不知道这个错误代表着什么，但就是写不进去：（，只是执行的话是正常的。
或许就是得windows才可以写入Flash？
总之暂停了，ESP32程序已经入门了，比树莓派简单一些。
在做别的开发版吧
```
学习使用esp32，用micropython开发。
1. 其micornpython主要是识别python文件，boot.py和 main.py 作为入口然后执行。
2. 安装第三方库有点麻烦，还好micropython本身已经有了很多内容。
3. 写入Flash已知报错ENODEV，试了各种办法都没用，气死我了，总之程序可以运行，只是不能写入，这个问题不大。
```


第一次使用： 刷新版本的固件（1～5月发布一个![img.png](img.png)）：https://micropython.org/download/ESP32_GENERIC_S3/
    1. 安装存根，pip安装esptool  micropython-esp32-stable
    2. 自动擦除闪存（自动识别仅限只有一个esp32的情况）：在虚拟环境中使用 “esptool.py erase_flash”
    3. 下载新固件：https://micropython.org/download/ESP32_GENERIC_S3/
    4. 刷入新固件：
        然后将固件部署到主板上，从地址0开始：
            esptool.py --baud 460800 write_flash 0 ESP32_BOARD_NAME-DATE-VERSION.bin
        用从此页面下载的.bin文件替换ESP32_BOARD_NAME-DATE-VERSION.bin。
        如上所述，如果esptool.py无法自动检测串行端口，那么您可以在命令行上明确地传递它。例如：
            esptool.py --port PORTNAME --baud 460800 write_flash 0 ESP32_BOARD_NAME-DATE-VERSION.bin
        故障排除
            如果闪烁开始，然后中途失败，请尝试删除--baud 460800选项，以较慢的默认速度闪烁。
            If these steps don't work, consult the MicroPython ESP32 Troubleshooting steps and the esptool documentation.
            重要信息：从以下选项中，为您的董事会下载.bin文件。
                1. 下载固件：https://micropython.org/download/ESP32_GENERIC_S3/
    5. pycharm的micropython也要选择对应固件版本的存根    

- 概念：
    基本上，micropython是一个库，只能导入这个库中过的包。
    也可以安装第三方库，但不太一样。
    此外包含部分python本身有的库

- 测试：
    输出信息：esptool.py flash_id


- 链接：先调试好存根与固件，重新连接usb那个口

- 运行：
    1. 测试运行：
        有时候直接点运行无效，需要先停止，然后再点运行
    2. （文件架构）写入文件运行：
       - 会自动寻找三个文件进行执行：
         1. main.py
            这里是主程序，应该放置一个循环以不断执行。
            也是一个*入口*
         2. boot.py
            这里是定义一些初始化的地方，这种延迟初始化的目的是在boot.py中预配置特定硬件,连网之类的，然后让它从正确的配置开始。
            ！boot.py应该总是退出，而不是无限期地运行。
            tip: 可以没有boot.py，而是将任何初始化代码放在main.py的顶部会更简单。
            在boot.py中设置的任何全局变量仍将在main.py的全局上下文中设置
            也就是boot就是C开发时的bootloader
         3. _boot.py
            这个不用管，是来自micropython比较低层的内容


- 关于安装第三方库：
    可以用Thonny安装，这个方便一点。
    micropython官方下载的bin文件里只有有限的micropython基础库，当你想实现某个功能时突然发现运行不起来，REPL或串口log提示没有你import的 module，这就要网络安装库文件了。
    顺便说一下，标准的Python库被 “微型化”后，就是micropython标准库。它们仅仅提供了该模块的核心功能。一些模块没有直接使用标准的Python的名字，而是冠以"u"，例如 ujson 代替 json 。也就是说micropython标准库（=微型库），只实现了一部分模块功能。 微型化的库大多只实现了标准库的部分功能，例如ure仅支持match/search, findall是不支持的，无法用来提取字符串。
    在嵌入式平台上，可添加Python级别封装库从而实现命名兼容CPython，微模块即可调用他们的u-name，也可以调用non-u-name。 根据non-u-name包路径的文件可重写。例如，import json 的话，首先搜索一个 json.py 文件或 json 目录进行加载。 如果没有找到，它回退到加载内置 ujson 模块。

    包管理途径至少有二，一是借助工具比如Thonny内嵌的MannagePackages， 二是在REPL模式下让板子连wifi上网，通过mip（类似pip， 早期版本是pip）安装特定包。推荐使用Thonny，成功率100%，缺点是要擦亮眼睛看清楚搜索到的包是micropython版本的。mip操作复杂还经常失败报搜不到包。
    
    mip操作，先在REPL shell里导入network模块配置WiFi让设备连网
    
    import network
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect("YOUR_WIFI_SSID", "YOUR_WIFI_PASSWORD")
    sta_if.isconnected()
    设备连网完毕，导入mip，安装你要的包。
    
    import mip
    mip.install('micropython-uasyncio')
- 

