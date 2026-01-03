from encode import Encoder
from decode import Decoder
import os
from PIL import Image


def decode_pics(pics_path: str, output_file: str):
    '''
    decode_pics 的 Docstring

    :param pics_path: 要解密的图片文件夹路径，注意最后要加斜杠
    :type pics_path: str
    :param output_file: 解密后输出的文件路径
    :type output_file: str
    '''
    file_count = len(os.listdir(pics_path))
    result_file = open(output_file, "wb+")
    file_sizes = []
    for file in range(file_count):
        image = Image.open(pics_path + str(file) + ".png")
        decoder = Decoder()
        result = decoder.decode(image)
        file_sizes.append(len(result))
        result_file.write(result)
    result_file.close()


def encode_file(pics_path: str, input_file: str, read_size=1000):
    '''
    encode_file 的 Docstring

    :param pics_path: 存放生成的彩色二维码图片的文件夹路径, 注意最后要加斜杠
    :type pics_path: str
    :param input_file: 需要转换为彩色二维码的文件路径
    :type input_file: str
    :param read_size: 每次读取的文件大小，默认为1000字节
    :type read_size: int
    '''

    file = open(input_file, "rb")

    index = 0
    data = file.read(read_size)
    while data:
        encoder = Encoder()
        images = encoder.encode(data)
        data = file.read(read_size)
        images.save(f"{pics_path}{index}.png")
        index += 1
    file.close()
