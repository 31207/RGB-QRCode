# RGB-QRCode
使用RGB三个通道存储二维码数据

在[ChromaQR](https://github.com/w-henderson/ChromaQR)的基础上修改, 改用zxingcpp库作为解码库, 因为pyzbar解码时会进行一次编码转换, 导致解码出的二进制数据不同, zxingcpp就没有这个问题
