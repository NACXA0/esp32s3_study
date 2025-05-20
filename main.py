# 这里是主程序文件
from machine import Pin, TouchPad
import time, random

# 测试LED
def test_LED():
    import neopixel
    num=48
    GPIO_IN = Pin(num, Pin.OUT)
    LED = neopixel.NeoPixel(pin=GPIO_IN, n=1)  # 创建控制对象
    (0,0,0).write()
    while True:
        time.sleep(1)
        print(num)
        LED[0] = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))  # 依次设置LED灯珠的颜色
        LED.write()  # 写入数据

# 芯片内的温度传感器
def test_temp():
    import esp32
    while True:
        print(esp32.mcu_temperature())  # read the internal temperature of the MCU, in Celsius
        time.sleep(1)

# 测试电容引脚
def test_touch():

    t = TouchPad(Pin(14))
    while True:
        print(t.read())
        time.sleep(1)

# 测试触摸与LED  触摸亮，每次颜色不一样
def touch_and_led():
    import neopixel
    GPIO_IN = Pin(48, Pin.OUT)
    LED = neopixel.NeoPixel(pin=GPIO_IN, n=1)  # 创建控制对象
    t = TouchPad(Pin(14))
    is_touch = False
    while True:
        if t.read() > 40000 and is_touch == False:
            LED[0] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # 依次设置LED灯珠的颜色
            LED.write()  # 写入数据
            is_touch = True
        if t.read() < 40000 and is_touch == True:
            LED[0] = (0, 0, 0)  # 依次设置LED灯珠的颜色
            LED.write()  # 写入数据he
            is_touch = False


if __name__ == '__main__':
    touch_and_led()
