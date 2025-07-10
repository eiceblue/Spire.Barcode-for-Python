from spire.barcode import *

# Function to write all bytes to a file
def WriteAllBytes(fname: str, data):
    with open(fname, "wb") as fp:
        fp.write(data)
    fp.close()


# Create an instance of BarcodeSettings
barcodeSettings = BarcodeSettings()

# Set the type of barcode to ITF14
barcodeSettings.Type = BarCodeType.ITF14

# Set the data for the barcode
barcodeSettings.Data = "12345"

# Set the ITF14BearerBars type of barcode to Frame
barcodeSettings.ITF14BearerBars = ITF14BorderType.Frame

# Create an instance of BarCodeGenerator with the specified settings
barCodeGenerator = BarCodeGenerator(barcodeSettings)

# Generate the image for the barcode
barcodeimage = barCodeGenerator.GenerateImage()

# Write the PNG image to disk
WriteAllBytes("ITF14.png", barcodeimage)

