from PIL import Image, ImageEnhance, ImageOps
import zxingcpp


class Decoder:
    """
    Base decoder for QR codes.
    Currently cannot be customised.
    """

    def __init__(self, debug=False):
        self.debug = debug
        self.result = None
        self.code_quad = None

    def decode(self, image: Image) -> bytearray:
        """
        Decode the given PIL Image containing a RGB-QRCode into a bytearray.
        If no QR code can be found, an empty bytearray will be returned.

        If the `Decoder` object has the property `debug` set to `True`, the program will save the processed image for each of the codes.
        """

        decoded_bytes = b""

        if image.mode == "RGBA":
            converted_image = Image.new("RGB", image.size, (255, 255, 255))
            mask = image.split()[3]
            mask = ImageOps.colorize(
                mask, "#000000", "#ffffff", blackpoint=254, whitepoint=255)
            mask = mask.convert("1")
            converted_image.paste(image, mask=mask)
        else:
            converted_image = image

        if converted_image.size[0] > 1280 or converted_image.size[1] > 1280:
            converted_image.thumbnail(
                (min(1280, converted_image.size[0]), min(1280, converted_image.size[1])))

        code_quad = None

        for i in range(3):
            rgb_image = ImageOps.autocontrast(converted_image.split()[i])
            rgb_image = ImageOps.colorize(
                rgb_image, "#000000", "#ffffff", blackpoint=100, whitepoint=180)
            decoded_codes = zxingcpp.read_barcodes(rgb_image)
            if self.debug:
                rgb_image.save("debug_{}.png".format(i))

            if len(decoded_codes) == 0:
                print("No code found in channel {}".format(i))
                return b""

            decoded_code = decoded_codes[0]
            decoded_bytes += decoded_code.bytes

        self.result = decoded_bytes
        return decoded_bytes
