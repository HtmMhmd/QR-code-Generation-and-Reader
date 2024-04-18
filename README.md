<<<<<<< HEAD
# QR Code Generation and Reader

This repository contains packages for QR code generation and reading in Python programming languages.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
    - [qrcode reader](#1-qrcodereader-usage)
    - [qrcode generator](#2-qrcodegenerator-usage)
- [Code Examples](#code-examples)
    - [qrcode reader](#1-qrcodereader-code)
    - [qrcode generator](#2-qrcodegenerator-code)
- [Methods Testing](#methods-testing)
    - [qrcode reader test code](#1-qrcode-reader-test-code)
    - [qrcode generator test code](#2-qrcode-generator-test-code)

## Introduction

The QR Code Generation and Reader packages provide a convenient way to generate and read QR codes in your applications.

QR codes are two-dimensional barcodes that can store various types of data, such as URLs, text, or contact information.

## Usage

Once cloned, you can use the QR Code Generation and Reader packages in your projects. The packages provide simple and intuitive APIs for generating QR codes and reading them.

### 1. QRCodeReader usage

#### 1.1. Import the package and create a QRCodeReader object:
```python
from qr_reader import QRCodeReader

reader = QRCodeReader(return_detections=True)
```
#### 1.2. You can then use the read_qr_code method to read QR codes from an image
```python
QR = reader.read_qr_code(image=frame)
```
This method returns a tuple for each detected QR code. The first element of the tuple is the decoded content of the QR code, and the second element is its bounding box.

### 2. QRCodeGenerator usage
#### 2.1. import the package and create a QRCodeGenerator object:
```python
from qr_generator import QRCodeGenerator

generator = QRCodeGenerator()
```
#### 2.2. You can then use the generate_qr_code method to generate a QR code:
```python
qr_code_image = generator.generate_qr_code(data="Hello, World!") 
```
This method returns an image object representing the QR code.

## Code Examples

Here are some code examples to get you started:

### 1. QRCodeReader code
```python
from QRreader import QRCodeReader

# Create an instance of QRCodeReader with return_detections set to True
reader = QRCodeReader(return_detections=True)

# Read the QR code from the input image
QR = reader.read_qr_code(image=input_image)

# Get the decoded content of the QR code at qr_index
decoded_content = QR[0][qr_index]

# Get the bounding box coordinates of the QR code at qr_index
bounding_box = QR[1][qr_index]
```

### 2. QRCodeGenerator code
```python
from QRgenerator import QRCodeGenerator

# Create a QRCodeGenerator object
qr = QRCodeGenerator()

# Define the data to be encoded in the QR code
data = "Hello World"

# Generate the QR code using the QRCodeGenerator object
qr.generate_qr_code(data)
```
# Methods Testing
we are providing a test code which run the program as follows:
## Methods Testing

### 1. QRcode reader test code

- This [code](./qr_reader/qr%20reader%20test.py) captures video from the camera, uses a QRCodeReader to detect and decode QR codes in the video frames,
and displays the frames with the detected QR codes. 
- The QRCodeReader object is created with `return_detections` set to True,
which means it returns the detected QR codes along with their bounding boxes and decoded contents. 
- The code loops through each detected QR code, draws a rectangle around it, and puts the decoded content as text on top of it. 
- If no QR code is detected, it prints "No QR code detected". The code loops until 'q' is pressed, at which point it
releases the VideoCapture object and closes the windows.

### 2. QRcode generator test code

- This [code](./qr_generator/qr%20generator%20tester.py) prompts the user for a string, generates a QR code from it using `generate_qr_code` method, and then prints out the decoded string. The generated QR code is saved as `my_qr_code.png`.
    
=======
A generation and reading qrcode project
>>>>>>> 959b9fd886759e84797d809ce6424a2d925fec73
