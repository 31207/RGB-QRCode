from PIL import Image
from qrcode import QRCode, constants
from enum import Enum
import math

# Error correction: LOW, MEDIUM, HIGH or MAX.
ErrorCorrection = Enum("ErrorCorrection", "LOW MED HIGH MAX")


class Encoder:
    """
    Base encoder for QR codes.
    Initialised by defining the error correction level.
    """

    def __init__(self, error_correction="LOW"):
        self.error_correction = ErrorCorrection[error_correction]

    def encode(self, data: bytearray) -> Image:
        """
        Encode a bytearray into a ChromaQR code.
        Returns a PIL Image which can be saved with `.save("filename.png")`.
        """

        code_pics = []
        section_length = math.ceil(len(data) / 3)
        split_data = [
            data[0: section_length],
            data[section_length: section_length * 2],
            data[section_length * 2:]
        ]

        error_correction_map = {
            ErrorCorrection.LOW: constants.ERROR_CORRECT_L,
            ErrorCorrection.MED: constants.ERROR_CORRECT_M,
            ErrorCorrection.HIGH: constants.ERROR_CORRECT_Q,
            ErrorCorrection.MAX: constants.ERROR_CORRECT_H
        }
        qr_codes = []
        versions = []

        for part in split_data:
            qr_code = QRCode(
                error_correction=error_correction_map[self.error_correction]
            )
            qr_code.add_data(part, optimize=0)
            qr_code.make()
            qr_codes.append(qr_code)
            versions.append(qr_code.version)
        if all(v == versions[0] for v in versions):
            for qr_code in qr_codes:
                qr_code_image = qr_code.make_image(
                    fill_color="black", back_color="white")
                code_pics.append(qr_code_image.convert("L"))
        else:
            max_version = max(versions)
            for i, qr_code in enumerate(qr_codes):
                if qr_code.version != max_version:
                    qr_code = QRCode(
                        version=max_version,
                        error_correction=error_correction_map[self.error_correction]
                    )
                    qr_code.add_data(split_data[i], optimize=0)
                    qr_code.make()
                qr_code_image = qr_code.make_image(
                    fill_color="black", back_color="white")
                code_pics.append(qr_code_image.convert("L"))
        
        

        return Image.merge("RGB", code_pics)

