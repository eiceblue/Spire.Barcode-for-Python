from spire.barcode import *

# Function to write all bytes to a file
def WriteAllBytes(fname: str, data):
    with open(fname, "wb") as fp:
        fp.write(data)
    fp.close()

# Create an instance of BarcodeSettings
barcodeSettings = BarcodeSettings()

# Set the type of barcode to Code128
barcodeSettings.Type = BarCodeType.Code128

# Set the data for the barcode
barcodeSettings.Data = "12345"

# Set the Code128SetMode type of barcode to Auto
barcodeSettings.Code128SetMode = Code128SetMode.Auto

# Create an instance of BarCodeGenerator with the specified settings
barCodeGenerator = BarCodeGenerator(barcodeSettings)

# Generate the image for the barcode
barcodeimage = barCodeGenerator.GenerateImage()

# Write the PNG image to disk
WriteAllBytes("Code128.png", barcodeimage)

