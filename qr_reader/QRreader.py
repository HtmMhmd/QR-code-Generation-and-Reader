from qreader import QReader
import cv2
import numpy as np

class QRCodeReader:
    """
    A class for reading QR codes from images.

    """

    def __init__(self, return_detections : bool =False):
        """
        Initialize a QRCodeReader instance.

        """
        self.detector = QReader()
        self.return_detections = return_detections

    def read_qr_code(self, image_path : str = None, image : np.array = None) -> list:
        """
        Reads QR codes from an image file and returns the results.

        Args:
            :param image_path (str): The path to the image file.
            :param image (np.array): The image file.

            you should provide either image_path or image, if both the image_path is previlaged.

        Returns:
            :return QRs: A list of QR code strings detected in the image.

        This method reads the image, detects and decodes the QR codes within it, and returns the results.
        """

        if (image_path != None):
            # Read the image using OpenCV
            img = cv2.imread(image_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
        else :
            img = image
        
        # Detect and decode the QRs within the image
        # The QReader object detects and decodes the QR codes
        QRs = self.detector.detect_and_decode(image=img, return_detections=self.return_detections)
        
        return QRs
