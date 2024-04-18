from QRreader import QRCodeReader  
import cv2  
import numpy as np  

# Create a VideoCapture object to capture video from the camera
cap = cv2.VideoCapture(0)

# Create a QRCodeReader object with return_detections set to True
reader = QRCodeReader(return_detections=True)

while True:
    # Read the frame from the camera
    ret, frame = cap.read()

    # Call the read_qr_code function with the frame
    QR = reader.read_qr_code(image=frame)
    
    try:
        # Loop through each detected QR code
        for qr_index in range(len(QR[0])):
            decoded_content = QR[0][qr_index]  # Get the decoded content of the QR code
            bounding_box = QR[1][qr_index]  # Get the bounding box of the QR code
            x_1, y_1, x_2, y_2  = np.uint16(bounding_box['bbox_xyxy'])
            # Draw a rectangle around the QR code
            cv2.rectangle(frame, (x_1, y_1), (x_2, y_2), (0, 255, 0), 2)
            # Put the decoded content as text on top of the QR code
            cv2.putText(frame, decoded_content, (x_1, y_1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    except:
        print("No QR code detected")
    
    # Display the frame with the QR code
    cv2.imshow('QR Code', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the windows
cap.release()
cv2.destroyAllWindows()