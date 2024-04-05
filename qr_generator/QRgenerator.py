import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

class QRCodeGenerator:
    """
    A class for generating and decoding QR codes.

    Attributes:
        :param filename (str): The name of the file to save the generated QR code image.
    """
    def __init__(self, filename : str ="my_qr_code.png"):
        """
        Initialize a QRCodeGenerator.
        """
        self.filename = filename

    def generate_qr_code(self, data : str ="GENERATED EXAMPLE")-> None:
        """
        Generate a QR code from the given data and save it as an image.

        Args:
            :param data (str): The data to encode in the QR code.
        """
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=2,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image
        img.save(self.filename)

    def decode_qr_code(self, filename : str =None) -> str:
        """
        Decode a QR code image and return the content as a string.

        Args:
            :param filename (str): The filename of the QR code image.
            If not provided, the filename specified in the constructor is used.

        Returns:
            :return str: The decoded content of the QR code.
        """
        # If no filename is provided.
        if filename is None:
            filename = self.filename

        # Open the QR code image.
        img = Image.open(filename)

        # Decode the QR code.
        result = decode(img)

        # Return the decoded content of the QR code.
        return result[0].data.decode("utf-8")

