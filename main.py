import utils
from decode import Decoder
from encode import Encoder
from PIL import Image

def example_usage():
    # Example usage:
    # Encode a file into images
    utils.encode_file(pics_path="output_images/",
                      input_file="test.gif", read_size=4096)

    # Decode images back into a file
    utils.decode_pics(pics_path="output_images/",
                      output_file="decoded_test.gif")


if __name__ == "__main__":
    # e = Encoder()
    # e.encode(b"1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz").save("example.png")
    # d = Decoder()
    # print(d.decode(Image.open("example.png")))

    example_usage()
