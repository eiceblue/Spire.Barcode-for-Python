from spire.barcode import *

# Function to write all bytes to a file
def WriteAllBytes(fname:str,data):
    fp = open(fname,"wb")
    fp.write(data)
    fp.close()

# Initialize a new instance of BarcodeSettings
barcodeSettings = BarcodeSettings()

# Set the barcode type to QR Code
barcodeSettings.Type = BarCodeType.QRCode

# Specify the background color as WhiteSmoke
barcodeSettings.BackColor = Color.get_WhiteSmoke()

# Set the QR Code data mode to Byte
barcodeSettings.QRCodeDataMode = QRCodeDataMode.Byte

# Choose the error correction level (ECL) as M
barcodeSettings.QRCodeECL = QRCodeECL.M

# Set whether to display text at the bottom of the barcode
barcodeSettings.ShowTextOnBottom = True

# Define the horizontal offset (not sure what this does exactly)
barcodeSettings.X = 3

# Store the data to be encoded in variables and set it on the settings
data = "ABC 123456789"
barcodeSettings.Data2D = data
barcodeSettings.Data = data

# Add a logo image to the QR Code
barcodeSettings.SetQRCodeLogoImage("data/Logo.png")

# Create a new instance of BarCodeGenerator using the provided settings
barCodeGenerator = BarCodeGenerator(barcodeSettings)

# Generate the barcode image
barcodeimage = barCodeGenerator.GenerateImage()

# Write the resulting image to a file
WriteAllBytes("AddLogoImageQRCode.png", barcodeimage)
